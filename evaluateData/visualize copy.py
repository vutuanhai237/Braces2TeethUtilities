import matplotlib.pyplot as plt
import numpy as np

def reduceList(list, times):
    i = 0
    total = 0
    newList = []
    for elem in list:
        if i == times:
            newList.append(total)
            i = 0
            total = 0
        else:
            i = i + 1
            total = total + elem
    return newList



class Metric:
    def __init__(self, epoch, ggan, gl1, dreal, dfake):
        self.epoch = epoch
        self.ggan = ggan
        self.gl1 = gl1
        self.dreal = dreal
        self.dfake = dfake
    def __str__(self):
        return f'epoch:{self.epoch}, G_GAN:{self.ggan}, G_L1:{self.gl1}, D_real:{self.dreal}, D_fake:{self.dfake}'

file = open(
    r"./loss_log copy.txt",
    "r",
)
metric,epochs,ggans,gl1s, dreals, dfakes = [],[],[],[],[],[]

for line in file:
    print(line)
    if line[0] != "=":
        # (epoch: 1, iters: 100, time: 0.223, data: 0.295) G_GAN: 1.772 G_L1: 37.913 D_real: 0.652 D_fake: 0.238 
        epoch = line[line.find("epoch") + 7 : line.find(",")]
        epochs.append(int(epoch))
        ggan = line[line.find("G_GAN") + 6 : line.find("G_GAN") + 12]
        ggans.append(float(ggan))
        gl1 = line[line.find("G_L1") + 5 : line.find("G_L1") + 12]
        gl1s.append(float(gl1))
        dreal = line[line.find("D_real") + 8 : line.find("D_real") + 13]
        dreals.append(float(dreal))
        dfake = line[line.find("D_fake") + 8 : line.find("D_fake") + 13]
        dfakes.append(float(dfake))
        metric.append(Metric(epoch, ggan, gl1, dreal, dfake))
print(metric[0])
# A

plt.subplot(2,4,1)
plt.xlabel("Epoch")
plt.ylabel("G_GAN")
plt.xticks(np.arange(0, 200, 40))
plt.yticks(np.arange(min(ggans), max(ggans)+1, 5))
plt.plot(epochs, ggans)

plt.subplot(2,4,2)
plt.xlabel("Epoch")
plt.ylabel("G_L1")
plt.xticks(np.arange(0, 200, 40))
plt.yticks(np.arange(min(gl1s), max(gl1s)+1, 5))
plt.plot(epochs, gl1s)

plt.subplot(2,4,3)
plt.xlabel("Epoch")
plt.ylabel("D_real")
plt.xticks(np.arange(0, 200, 40))
plt.yticks(np.arange(min(dreals), max(dreals)+1, 0.5))
plt.plot(epochs, dreals)

plt.subplot(2,4,4)
plt.xlabel("Epoch")
plt.ylabel("D_fake")
plt.xticks(np.arange(0, 200, 40))
plt.yticks(np.arange(min(dfakes), max(dfakes)+1, 0.5))
plt.plot(epochs, dfakes)








plt.show()