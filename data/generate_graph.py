import matplotlib.pyplot as plt
import re
import numpy as np
import glob

llcways=[2048,4096,8192,16384]
traces=['bfs-14.trace.gz','cc-14.trace.gz','sssp-14.trace.gz']
baselines=np.zeros(shape=(1,3))
speedups=np.zeros(shape=(3,4))
for i in range(len(llcways)):
    way=llcways[i]
    for j in range(len(traces)):
        trace=traces[j]
        with open(f"llc_way_{way}/{trace}-gshare-no-no-no-no-lru-1core.txt","r") as f:
            data = f.read()
        ipc = float(re.findall("CPU 0 cumulative IPC: [0-9\.]+",data)[0].split(" ")[-1])
        if i==0:
            baseline_ipc = ipc
            baselines[0,j] = baseline_ipc
        # print(ipc,baseline_ipc,baselines[0,j])
        speedups[j,i] = ipc/baselines[0,j]

x_axis = np.arange(len(traces))
for i in range(len(llcways)):
    plt.bar(x_axis-0.3+0.2*i, speedups[:,i], 0.2, label=f"LLC WAY = {llcways[i]}")
plt.xticks(x_axis,traces)
plt.ylabel("Speedup")
plt.xlabel("Trace")
plt.title("Speedup vs LLC WAY for various trace")
plt.legend()
plt.savefig("llc_ways.png")
plt.close()


l2ways=[1024,2048,4096,8192]
traces=['bfs-14.trace.gz','cc-14.trace.gz','sssp-14.trace.gz']
baselines=np.zeros(shape=(1,3))
speedups=np.zeros(shape=(3,4))
for i in range(len(l2ways)):
    way=l2ways[i]
    for j in range(len(traces)):
        trace=traces[j]
        with open(f"l2_way_{way}/{trace}-gshare-no-no-no-no-lru-1core.txt","r") as f:
            data = f.read()
        ipc = float(re.findall("CPU 0 cumulative IPC: [0-9\.]+",data)[0].split(" ")[-1])
        if i==0:
            baseline_ipc = ipc
            baselines[0,j] = baseline_ipc
        # print(ipc,baseline_ipc,baselines[0,j])
        speedups[j,i] = ipc/baselines[0,j]

x_axis = np.arange(len(traces))
for i in range(len(l2ways)):
    plt.bar(x_axis-0.3+0.2*i, speedups[:,i], 0.2, label=f"L2 WAY = {l2ways[i]}")
plt.xticks(x_axis,traces)
plt.ylabel("Speedup")
plt.xlabel("Trace")
plt.title("Speedup vs L2 WAY for various trace")
plt.legend()
plt.savefig("l2_ways.png")