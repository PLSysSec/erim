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
l2, t2 = decode_log("hfi.log")

data = [
    list(np.divide(t1, t1)),
    list(np.divide(t2, t1)),        
]

print(data)
X = np.arange(len(l1))    
fig, ax = plt.subplots(ncols=1, nrows=1)
delta = 0.25
ax.bar(X, data[0], color = 'g', width = delta, hatch='/')
ax.bar(X + delta, data[1], color = 'r', width = delta, hatch='-')



# ax.set_ylabel('Leaked bytes percentile')
ax.legend(labels=['Unprotected', 'HFI'])
ax.set_xticks(X+delta)
ax.set_xticklabels(l1)

#     # ax.set_title('Scores by group and gender')
    
#     ax.set_yticks(np.arange(0, 2.5, 0.2))

    
fig.tight_layout()
fig.set_size_inches(6, 4)
fig.savefig('nginx.png', dpi=100)
# plt.show()

# draw_heatmap()
