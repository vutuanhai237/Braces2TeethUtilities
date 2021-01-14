import numpy as np
from matplotlib import pyplot as plt
import cv2
import scipy.misc
import os, glob
from PIL import Image

def averageMultiImage(path):
    list_images = [cv2.imread(file) for file in glob.glob(path)]

    # Assuming all images are the same size, get dimensions of first image
    w, h = 256, 256
    N = len(list_images)

    # Create a numpy array of floats to store the average (assume RGB images)
    arr = np.zeros((h, w, 3), np.float)

    # Build up average pixel intensities, casting each image as an array of floats
    for image in list_images:
        
        imarr = np.array(image, dtype=np.float)
        arr = arr + imarr
    arr = arr / N
    print(N)
    # Round values in array and cast as 16-bit integer
    arr = np.array(np.round(arr), dtype=np.uint16)

    # Generate, save and preview final image
    return arr


def hist_norm(source, template):

    olddtype = source.dtype
    oldshape = source.shape
    source = source.ravel()
    template = template.ravel()

    s_values, bin_idx, s_counts = np.unique(
        source, return_inverse=True, return_counts=True
    )
    t_values, t_counts = np.unique(template, return_counts=True)
    s_quantiles = np.cumsum(s_counts).astype(np.float64)
    s_quantiles /= s_quantiles[-1]
    t_quantiles = np.cumsum(t_counts).astype(np.float64)
    t_quantiles /= t_quantiles[-1]
    interp_t_values = np.interp(s_quantiles, t_quantiles, t_values)
    interp_t_values = interp_t_values.astype(olddtype)
    return interp_t_values[bin_idx].reshape(oldshape)


def hist_match(source, template):
    """
    Adjust the pixel values of a grayscale image such that its histogram
    matches that of a target image

    Arguments:
    -----------
        source: np.ndarray
            Image to transform; the histogram is computed over the flattened
            array
        template: np.ndarray
            Template image; can have different dimensions to source
    Returns:
    -----------
        matched: np.ndarray
            The transformed output image
    """

    oldshape = source.shape
    source = source.ravel()
    template = template.ravel()

    # get the set of unique pixel values and their corresponding indices and
    # counts
    s_values, bin_idx, s_counts = np.unique(
        source, return_inverse=True, return_counts=True
    )
    t_values, t_counts = np.unique(template, return_counts=True)

    # take the cumsum of the counts and normalize by the number of pixels to
    # get the empirical cumulative distribution functions for the source and
    # template images (maps pixel value --> quantile)
    s_quantiles = np.cumsum(s_counts).astype(np.float64)
    s_quantiles /= s_quantiles[-1]
    t_quantiles = np.cumsum(t_counts).astype(np.float64)
    t_quantiles /= t_quantiles[-1]

    # interpolate linearly to find the pixel values in the template image
    # that correspond most closely to the quantiles in the source image
    interp_t_values = np.interp(s_quantiles, t_quantiles, t_values)

    return interp_t_values[bin_idx].reshape(oldshape)

def ecdf(x):
    """convenience function for computing the empirical CDF"""
    vals, counts = np.unique(x, return_counts=True)
    ecdf = np.cumsum(counts).astype(np.float64)
    ecdf /= ecdf[-1]
    return vals, ecdf

def arrayToImage(arr):
    img = np.zeros([256,256,3])

    img[:,:,0] = np.ones([200,200])*255
    img[:,:,1] = np.ones([200,200])*255
    img[:,:,2] = np.ones([200,200])*0

    r,g,b = cv2.split(img)
    img_bgr = cv2.merge([b,g,r])



source = cv2.imread("./crop_mouth/failureGT/33_real.png")
sink = averageMultiImage("./crop_mouth/successGT/*.png")
template = np.array(sink, dtype = np.uint8 )

template = cv2.imread("./crop_mouth/successGT/10_real.png")
matched = hist_norm(source, template)
cv2.imwrite("matched.png", matched)





x1, y1 = ecdf(source.ravel())
x2, y2 = ecdf(template.ravel())
x3, y3 = ecdf(matched.ravel())

fig = plt.figure()
gs = plt.GridSpec(2, 3)
ax1 = fig.add_subplot(gs[0, 0])
ax2 = fig.add_subplot(gs[0, 1], sharex=ax1, sharey=ax1)
ax3 = fig.add_subplot(gs[0, 2], sharex=ax1, sharey=ax1)
ax4 = fig.add_subplot(gs[1, :])
for aa in (ax1, ax2, ax3):
    aa.set_axis_off()

ax1.imshow(cv2.cvtColor(source, cv2.COLOR_BGR2RGB))
ax1.set_title("Source")
ax2.imshow(cv2.cvtColor(template, cv2.COLOR_BGR2RGB))
ax2.set_title("template")
ax3.imshow(cv2.cvtColor(matched, cv2.COLOR_BGR2RGB))
ax3.set_title("Matched")

# ax4.plot(x1, y1 * 100, "-r", lw=3, label="Source")
# ax4.plot(x2, y2 * 100, "-k", lw=3, label="Template")
# ax4.plot(x3, y3 * 100, "--r", lw=3, label="Matched")
# ax4.set_xlim(x1[0], x1[-1])
# ax4.set_xlabel("Pixel value")
# ax4.set_ylabel("Cumulative %")
# ax4.legend(loc=5)

ax4.plot(cv2.calcHist([source], [0], None, [256], [0, 256]), "-r",label="Source")
ax4.plot(cv2.calcHist([template], [0], None, [256], [0, 256]), "-b", label="Template")
ax4.plot(cv2.calcHist([matched], [0], None, [256], [0, 256]), "-g", label="Matched")
ax4.legend(loc=5)
plt.show()
