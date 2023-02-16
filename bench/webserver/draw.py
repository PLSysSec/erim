#!/usr/bin/python3
import sys
import numpy as np
import matplotlib
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure


def decode_log(filename):
    labels = []
    tps = []
    for line in open(filename):
        line = line.strip()
        if line.startswith("----"):
            labels.append(line[4:])
        if line.startswith("Requests per second"):
            tps.append(float(line.split()[3]))

    return (labels, tps)

l1, t1 = decode_log("native.log")
l2, t2 = decode_log("erim.log")
l3, t3 = decode_log("hfi.log")

print(t1)
print(t2)
print(t3)

data = [
    list(np.divide(t1, t1)),
    list(np.divide(t2, t1)),
    list(np.divide(t3, t1)),
]

print(data)

with open("data.txt", "w") as txt_file:
    txt_file.write("Native: " + str(data[0]) + "\n")
    txt_file.write("Erim: " + str(data[1]) + "\n")
    txt_file.write("HFI: " + str(data[2]) + "\n")
    txt_file.write("\n")
    txt_file.write("Erim min: " + str(min(data[1])) + "\n")
    txt_file.write("Erim max: " + str(max(data[1])) + "\n")
    txt_file.write("HFI min: " + str(min(data[2])) + "\n")
    txt_file.write("HFI max: " + str(max(data[2])) + "\n")

plt.rcParams['pdf.fonttype'] = 42 # true type font
# plt.rcParams['font.family'] = 'Linux Libertine'
plt.rcParams['font.size'] = '11'

X = np.arange(len(l1))
fig, ax = plt.subplots(ncols=1, nrows=1)
delta = 0.25
ax.bar(X, data[0], color = '#FFFFBF', width = delta, edgecolor = "black")
ax.bar(X + delta, data[1], color = '#D7191C', width = delta, edgecolor = "black")
ax.bar(X + 2*delta, data[2], color = '#2B83BA', width = delta, edgecolor = "black")


# ax.text(-1.3, 1.08, str("TPS\nNative"), color='black')


# for i, v in enumerate(t1):
#     ax.text(i-delta, 1.08, str("{:.2f}\n kB/s".format(v/1000)), color='black')


ax.set_ylabel('Norm. throughput')

ax.set_xlabel('File Size')
# ax.legend(labels=['Native', 'HFI'], ncol=2, frameon=False, bbox_to_anchor=(1.01, 1.28))
plt.legend(labels=['Unmodified Nginx', 'MPK', 'HFI emulation'], bbox_to_anchor=(1, 1.5), frameon=False, loc='upper right', ncol=3)
ax.set_xticks(X+delta/2)
ax.set_xticklabels(l1)
ax.set_yticks(np.arange(0, 1.1, 0.25))

fig.tight_layout(pad=2.5)
fig.set_size_inches(6.2, 2.1)
fig.savefig('nginx.pdf', format="pdf", bbox_inches="tight", pad_inches=0)
# plt.show()

# draw_heatmap()
