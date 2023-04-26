import matplotlib.pyplot as plt
import re
import numpy as np

# varying LLC SIZE
def plot_llc_size():
    llcsizes=[2048,4096,8192,16384,0]
    traces=['bfs-14.trace.gz','cc-14.trace.gz','sssp-14.trace.gz']
    baselines=np.zeros(shape=(1,len(traces)))
    speedups=np.zeros(shape=(len(traces),len(llcsizes)))
    mpkis=np.zeros(shape=(len(traces),len(llcsizes)))
    for i in range(len(llcsizes)):
        size=llcsizes[i]
        for j in range(len(traces)):
            trace=traces[j]
            with open(f"llc_size_{size}/{trace}-gshare-no-no-no-no-lru-1core.txt","r") as f:
                data = f.read()
            ipc = float(re.findall("CPU 0 cumulative IPC: [0-9\.]+",data)[0].split(" ")[-1])
            instructions = int(re.findall("CPU 0 cumulative IPC: [0-9\.]+ instructions: [0-9\.]+",data)[0].split(" ")[-1])
            missrate_line = re.findall("LLC TOTAL .*",data)[0]
            mpki = int(re.findall("MISS:[ ]*[0-9]+",missrate_line)[0].split(" ")[-1])/(instructions/1000)
            if i==0:
                baseline_ipc = ipc
                baselines[0,j] = baseline_ipc
            # print(ipc,baseline_ipc,baselines[0,j])
            speedups[j,i] = ipc/baselines[0,j]
            mpkis[j,i] = mpki

    x_axis = np.arange(len(traces))
    plt.figure(figsize=(12,8))
    for i in range(len(llcsizes)):
        plt.bar(x_axis-0.3+0.15*i, speedups[:,i], 0.15, label=f"LLC SIZE = {llcsizes[i]}")
    plt.xticks(x_axis,traces)
    plt.ylabel("Speedup")
    plt.xlabel("Trace")
    plt.title("Speedup vs LLC SIZE for various trace")
    plt.legend()
    plt.savefig("llc_sizes_speedup.png")
    plt.show()
    plt.close()

    plt.figure(figsize=(12,8))
    for i in range(len(llcsizes)-1):
        plt.bar(x_axis-0.3+0.2*i, mpkis[:,i], 0.2, label=f"LLC SIZE = {llcsizes[i]}")
    plt.xticks(x_axis,traces)
    plt.ylabel("MPKI")
    plt.xlabel("Trace")
    plt.title("MPKI vs LLC SIZE for various trace")
    plt.legend()
    plt.savefig("llc_sizes_mpki.png")
    plt.show()
    plt.close()


# varying L2 SIZE
def plot_l2_size():
    l2sizes=[1024,2048,4096,8192,0]
    traces=['bfs-14.trace.gz','cc-14.trace.gz','sssp-14.trace.gz']
    baselines=np.zeros(shape=(1,len(traces)))
    speedups=np.zeros(shape=(len(traces),len(l2sizes)))
    mpkis=np.zeros(shape=(len(traces),len(l2sizes)))
    for i in range(len(l2sizes)):
        size=l2sizes[i]
        for j in range(len(traces)):
            trace=traces[j]
            with open(f"l2_size_{size}/{trace}-gshare-no-no-no-no-lru-1core.txt","r") as f:
                data = f.read()
            ipc = float(re.findall("CPU 0 cumulative IPC: [0-9\.]+",data)[0].split(" ")[-1])
            instructions = int(re.findall("CPU 0 cumulative IPC: [0-9\.]+ instructions: [0-9\.]+",data)[0].split(" ")[-1])
            missrate_line = re.findall("L2C TOTAL .*",data)[0]
            mpki = int(re.findall("MISS:[ ]*[0-9]+",missrate_line)[0].split(" ")[-1])/(instructions/1000)
            if i==0:
                baseline_ipc = ipc
                baselines[0,j] = baseline_ipc
            # print(ipc,baseline_ipc,baselines[0,j])
            speedups[j,i] = ipc/baselines[0,j]
            mpkis[j,i] = mpki

    x_axis = np.arange(len(traces))
    plt.figure(figsize=(12,8))
    for i in range(len(l2sizes)):
        plt.bar(x_axis-0.3+0.15*i, speedups[:,i], 0.15, label=f"L2 SIZE = {l2sizes[i]}")
    plt.xticks(x_axis,traces)
    plt.ylabel("Speedup")
    plt.xlabel("Trace")
    plt.title("Speedup vs L2 SIZE for various trace")
    plt.legend()
    plt.savefig("l2_sizes_speedup.png")
    plt.show()
    plt.close()

    plt.figure(figsize=(12,9))
    for i in range(len(l2sizes)-1):
        plt.bar(x_axis-0.3+0.2*i, mpkis[:,i], 0.2, label=f"L2 SIZE = {l2sizes[i]}")
    plt.xticks(x_axis,traces)
    plt.ylabel("MPKI")
    plt.xlabel("Trace")
    plt.title("MPKI vs L2 SIZE for various trace")
    plt.legend()
    plt.savefig("l2_sizes_mpki.png")
    plt.show()
    plt.close()


# varying REPLACEMENT POLICY
def plot_repl():
    repls=["lru","random","lfu","fifo","mru","srrip","drrip"]
    traces=['bfs-14.trace.gz','cc-14.trace.gz','sssp-14.trace.gz']
    baselines=np.zeros(shape=(1,len(traces)))
    speedups=np.zeros(shape=(len(traces),len(repls)))
    mpkis=np.zeros(shape=(len(traces),len(repls)))
    for i in range(len(repls)):
        policy=repls[i]
        for j in range(len(traces)):
            trace=traces[j]
            with open(f"repl_policies/{trace}-gshare-no-no-no-no-{policy}-1core.txt","r") as f:
                data = f.read()
            ipc = float(re.findall("CPU 0 cumulative IPC: [0-9\.]+",data)[0].split(" ")[-1])
            instructions = int(re.findall("CPU 0 cumulative IPC: [0-9\.]+ instructions: [0-9\.]+",data)[0].split(" ")[-1])
            missrate_line = re.findall("LLC TOTAL .*",data)[0]
            mpki = int(re.findall("MISS:[ ]*[0-9]+",missrate_line)[0].split(" ")[-1])/(instructions/1000)
            if i==0:
                baseline_ipc = ipc
                baselines[0,j] = baseline_ipc
            # print(ipc,baseline_ipc,baselines[0,j])
            speedups[j,i] = ipc/baselines[0,j]
            mpkis[j,i] = mpki

    x_axis = np.arange(len(traces))
    plt.figure(figsize=(12,8))
    for i in range(len(repls)):
        plt.bar(x_axis-0.33+0.11*i, speedups[:,i], 0.11, label=repls[i])
    plt.xticks(x_axis,traces)
    plt.ylabel("Speedup")
    plt.xlabel("Trace")
    plt.ylim((0.6,1.2))
    plt.title("Speedup vs Replacement Policy for various trace")
    plt.legend(loc='upper left')
    plt.savefig("replacement_policies_speedup.png")
    plt.show()
    plt.close()

    for i in range(len(repls)):
        plt.bar(x_axis-0.39+0.13/2+0.13*i, mpkis[:,i], 0.13, label=repls[i])
    plt.xticks(x_axis,traces)
    plt.ylabel("MPKI")
    plt.xlabel("Trace")
    plt.title("MPKI vs Replacement Policy for various trace")
    plt.legend()
    plt.savefig("replacement_policies_mpki.png")
    plt.show()
    plt.close()


# varying CACHE INCLUSIVITY
def plot_incl():
    incs=["noninclusive","inclusive"]
    traces=['bfs-14.trace.gz','cc-14.trace.gz','sssp-14.trace.gz']
    baselines=np.zeros(shape=(1,len(traces)))
    speedups=np.zeros(shape=(len(traces),len(incs)))
    mpkis=np.zeros(shape=(len(traces),len(incs)))
    for i in range(len(incs)):
        inclusivity=incs[i]
        for j in range(len(traces)):
            trace=traces[j]
            with open(f"{inclusivity}/{trace}-gshare-no-no-no-no-lru-1core.txt","r") as f:
                data = f.read()
            ipc = float(re.findall("CPU 0 cumulative IPC: [0-9\.]+",data)[0].split(" ")[-1])
            instructions = int(re.findall("CPU 0 cumulative IPC: [0-9\.]+ instructions: [0-9\.]+",data)[0].split(" ")[-1])
            missrate_line = re.findall("LLC TOTAL .*",data)[0]
            mpki = int(re.findall("MISS:[ ]*[0-9]+",missrate_line)[0].split(" ")[-1])/(instructions/1000)
            if i==0:
                baseline_ipc = ipc
                baselines[0,j] = baseline_ipc
            # print(ipc,baseline_ipc,baselines[0,j])
            speedups[j,i] = ipc/baselines[0,j]
            mpkis[j,i] = mpki

    x_axis = np.arange(len(traces))
    for i in range(len(incs)):
        plt.bar(x_axis-0.15+0.3*i, speedups[:,i], 0.3, label=incs[i])
    plt.xticks(x_axis,traces)
    plt.ylabel("Speedup")
    plt.xlabel("Trace")
    plt.title("Speedup vs Inclusion Policy for various trace")
    plt.legend()
    plt.savefig("inclusivity_speedup.png")
    plt.show()
    plt.close()

    for i in range(len(incs)):
        plt.bar(x_axis-0.15+0.3*i, mpkis[:,i], 0.3, label=incs[i])
    plt.xticks(x_axis,traces)
    plt.ylabel("MPKI")
    plt.xlabel("Trace")
    plt.title("MPKI vs Inclusion Policy for various trace")
    plt.legend()
    plt.savefig("inclusivity_mpki.png")
    plt.show()
    plt.close()

plot_incl()