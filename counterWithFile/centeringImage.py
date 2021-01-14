from PIL import Image
import os
def centeringAndSave(folder):
    for file in os.listdir(folder):
        img = Image.open(folder + '/' + file)
        print(file)
        crop = img
        width, height = img.size   # Get dimensions
        new_height, new_width = 0, 0
        flag = 0
        if width > height:
            new_height = height
            new_width = height
        else:
            if width < height:
                new_height = width
                new_width = width
            else:
                flag = 1
      
        left = (width - new_width)/2
        top = (height - new_height)/2
        right = (width + new_width)/2
        bottom = (height + new_height)/2

        # Crop the center of the image
        if flag == 0:
            img = img.crop((left, top, right, bottom))
            img = img.save(folder + '/' + file[0:len(file)-4] + '.png')
            
centeringAndSave('result') 