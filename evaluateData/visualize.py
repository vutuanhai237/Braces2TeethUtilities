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
    def __init__(self, epoch, da, ga, ca, ia, db, gb, cb, ib):
        self.epoch = epoch
        self.da = da
        self.ga = ga
        self.ca = ca
        self.ia = ia
        self.db = db
        self.gb = gb
        self.cb = cb
        self.ib = ib
    def __str__(self):
        return f'epoch:{self.epoch}, D_A:{self.da}, G_A:{self.ga}, cycle_A:{self.ca}, idt_A:{self.ia}, D_B:{self.db}, G_B:{self.gb}, cycle_B:{self.cb}, idt_B:{self.ib}'

file = open(
    r"./loss_log.txt",
    "r",
)
metric,epochs,das,gas,cas,ias,dbs,gbs,cbs,ibs = [],[],[],[],[],[],[],[],[],[]

for line in file:
    print(line)
    if line[0] != "=":
        epoch = line[line.find("epoch") + 7 : line.find(",")]
        epochs.append(int(epoch))
        da = line[line.find("D_A") + 5 : line.find("D_A") + 10]
        print(da)
        das.append(float(da))
        ga = line[line.find("G_A") + 5 : line.find("G_A") + 10]
        gas.append(float(ga))
        ca = line[line.find("cycle_A") + 9 : line.find("cycle_A") + 14]
        cas.append(float(ca))
        ia = line[line.find("idt_A") + 7 : line.find("idt_A") + 12]
        ias.append(float(ia))
        db = line[line.find("D_B") + 5 : line.find("D_B") + 10]
        dbs.append(float(db))
        gb = line[line.find("G_B") + 5 : line.find("G_B") + 10]
        gbs.append(float(gb))
        cb = line[line.find("cycle_B") + 9 : line.find("cycle_B") + 14]
        cbs.append(float(cb))
        ib = line[line.find("idt_B") + 7 : line.find("idt_B") + 12]
        ibs.append(float(ib))
        metric.append(Metric(epoch, da, ga, ca, ia, db, gb, cb, ib))

# A

plt.subplot(2,4,1)
plt.xlabel("Epoch")
plt.ylabel("D_A")
plt.xticks(np.arange(min(epochs), max(epochs)+1, 20))
plt.yticks(np.arange(min(das), max(das)+1, 0.5))
plt.plot(epochs, das)

plt.subplot(2,4,2)
plt.xlabel("Epoch")
plt.ylabel("G_A")
plt.xticks(np.arange(min(epochs), max(epochs)+1, 20))
plt.yticks(np.arange(min(gas), max(gas)+1, 0.5))
plt.plot(epochs, gas)

plt.subplot(2,4,3)
plt.xlabel("Epoch")
plt.ylabel("cycle_A")
plt.xticks(np.arange(min(epochs), max(epochs)+1, 20))
plt.yticks(np.arange(min(cas), max(cas)+1, 0.5))
plt.plot(epochs, cas)

plt.subplot(2,4,4)
plt.xlabel("Epoch")
plt.ylabel("idt_A")
plt.xticks(np.arange(min(epochs), max(epochs)+1, 20))
plt.yticks(np.arange(min(ias), max(ias)+1, 0.5))
plt.plot(epochs, ias)

# B

plt.subplot(2,4,5)
plt.xlabel("Epoch")
plt.ylabel("D_B")
plt.xticks(np.arange(min(epochs), max(epochs)+1, 20))
plt.yticks(np.arange(min(dbs), max(dbs)+1, 0.5))
plt.plot(epochs, dbs)

plt.subplot(2,4,6)
plt.xlabel("Epoch")
plt.ylabel("G_B")
plt.xticks(np.arange(min(epochs), max(epochs)+1, 20))
plt.yticks(np.arange(min(gbs), max(gbs)+1, 0.5))
plt.plot(epochs, gbs)

plt.subplot(2,4,7)
plt.xlabel("Epoch")
plt.ylabel("cycle_A")
plt.xticks(np.arange(min(epochs), max(epochs)+1, 20))
plt.yticks(np.arange(min(cbs), max(cbs)+1, 0.5))
plt.plot(epochs, cbs)

plt.subplot(2,4,8)
plt.xlabel("Epoch")
plt.ylabel("idt_B")
plt.xticks(np.arange(min(epochs), max(epochs)+1, 20))
plt.yticks(np.arange(min(ibs), max(ibs)+1, 0.5))
plt.plot(epochs, ibs)







plt.show()