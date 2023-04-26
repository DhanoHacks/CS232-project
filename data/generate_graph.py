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
            with open(f"llc_size_change/llc_size_{size}/{trace}-gshare-no-no-no-no-lru-1core.txt","r") as f:
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
    plt.savefig("figures/llc_sizes_speedup.png")
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
    plt.savefig("figures/llc_sizes_mpki.png")
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
            with open(f"l2_size_change/l2_size_{size}/{trace}-gshare-no-no-no-no-lru-1core.txt","r") as f:
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
    plt.savefig("figures/l2_sizes_speedup.png")
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
    plt.savefig("figures/l2_sizes_mpki.png")
    plt.show()
    plt.close()


# varying REPLACEMENT POLICY
def plot_repl(inclusivity):
    repls=np.array(["lru","lfu","random","fifo","mru","srrip","drrip","ship"])
    traces=['bfs-14.trace.gz','cc-14.trace.gz','sssp-14.trace.gz']
    baselines=np.zeros(shape=(1,len(traces)))
    speedups=np.zeros(shape=(len(traces),len(repls)))
    mpkis=np.zeros(shape=(len(traces),len(repls)))
    for i in range(len(repls)):
        policy=repls[i]
        for j in range(len(traces)):
            trace=traces[j]
            with open(f"{inclusivity.lower()}/{trace}-gshare-no-no-no-no-{policy}-1core.txt","r") as f:
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
    # print(speedups)
    for i in range(len(repls)):
        plt.bar(x_axis-0.35+0.1*i, np.transpose(np.transpose(speedups)[speedups[1, :].argsort()])[:,i], 0.1, label=repls[speedups[1, :].argsort()][i])
    plt.xticks(x_axis,traces)
    plt.ylabel("Speedup")
    plt.xlabel("Trace")
    plt.ylim((0.6,1.2))
    plt.title(f"Speedup vs Replacement Policy for various traces using {inclusivity} Cache Hierarchy")
    plt.legend(loc='upper left')
    plt.savefig(f"figures/{inclusivity.lower()}_speedup.png")
    plt.show()
    plt.close()

    plt.figure(figsize=(12,8))
    for i in range(len(repls)):
        plt.bar(x_axis-0.35+0.1*i, np.flip(np.transpose(np.transpose(mpkis)[mpkis[1, :].argsort()]))[:,i], 0.1, label=np.flip(repls[mpkis[1, :].argsort()])[i])
    plt.xticks(x_axis,traces)
    plt.ylabel("MPKI")
    plt.xlabel("Trace")
    plt.title(f"MPKI vs Replacement Policy for various traces using {inclusivity} Cache Hierarchy")
    plt.legend()
    plt.savefig(f"figures/{inclusivity.lower()}_mpki.png")
    plt.show()
    plt.close()


# varying CACHE INCLUSIVITY
def plot_incl():
    incs=["NonInclusive","Inclusive","Exclusive"]
    traces=['bfs-14.trace.gz','cc-14.trace.gz','sssp-14.trace.gz']
    baselines=np.zeros(shape=(1,len(traces)))
    speedups=np.zeros(shape=(len(traces),len(incs)))
    mpkis=np.zeros(shape=(len(traces),len(incs)))
    for i in range(len(incs)):
        inclusivity=incs[i]
        for j in range(len(traces)):
            trace=traces[j]
            with open(f"{inclusivity.lower()}/{trace}-gshare-no-no-no-no-lru-1core.txt","r") as f:
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
    for i in range(len(incs)):
        plt.bar(x_axis-0.25+0.25*i, speedups[:,i], 0.25, label=incs[i])
    plt.xticks(x_axis,traces)
    plt.ylabel("Speedup")
    plt.xlabel("Trace")
    plt.title("Speedup vs Cache Inclusion Policy for various traces")
    plt.legend()
    plt.savefig("figures/inclusivity_speedup.png")
    plt.show()
    plt.close()

    plt.figure(figsize=(12,8))
    for i in range(len(incs)):
        plt.bar(x_axis-0.25+0.25*i, mpkis[:,i], 0.25, label=incs[i])
    plt.xticks(x_axis,traces)
    plt.ylabel("MPKI")
    plt.xlabel("Trace")
    plt.title("MPKI vs Cache Inclusion Policy for various traces")
    plt.legend()
    plt.savefig("figures/inclusivity_mpki.png")
    plt.show()
    plt.close()

# varying BLOCK SIZE
def plot_block():
    blocksizes=[64,32,16,8]
    traces=['bfs','cc','sssp']
    baselines=np.zeros(shape=(1,len(traces)))
    speedups=np.zeros(shape=(len(traces),len(blocksizes)))
    mpkis=np.zeros(shape=(len(traces),len(blocksizes)))
    for i in range(len(blocksizes)):
        blocksize=blocksizes[i]
        for j in range(len(traces)):
            trace=traces[j]
            with open(f"block_size_change/{trace}_{blocksize}BytesBlock.txt","r") as f:
                data = f.read()
            ipc = float(re.findall("CPU 0 cumulative IPC: [0-9\.]+",data)[0].split(" ")[-1])
            instructions = int(re.findall("CPU 0 cumulative IPC: [0-9\.]+ instructions: [0-9\.]+",data)[0].split(" ")[-1])
            missrate_line = re.findall("LLC TOTAL .*",data)[0]
            mpki = int(re.findall("MISS:[ ]*[0-9]+",missrate_line)[0].split(" ")[-1])/(instructions/1000)
            if i==0:
                baseline_ipc = ipc
                baselines[0,j] = baseline_ipc
            # print(ipc,baseline_ipc,baselines[0,j])
            speedups[j,i] = ipc
            mpkis[j,i] = mpki
    for i in range(len(blocksizes)):
        for j in range(len(traces)):
            speedups[j,i] = speedups[j,i]/baselines[0,j]

    x_axis = np.arange(len(traces))
    plt.figure(figsize=(12,8))
    for i in range(len(blocksizes)):
        plt.bar(x_axis-0.3+0.2*i, speedups[:,i], 0.2, label=f"BLOCK SIZE={blocksizes[i]}")
    plt.xticks(x_axis,traces)
    plt.ylabel("Speedup")
    plt.xlabel("Trace")
    plt.title("Speedup vs Block Size for various traces")
    plt.legend()
    plt.savefig("figures/block_size_speedup.png")
    plt.show()
    plt.close()

    for i in range(len(blocksizes)):
        plt.bar(x_axis-0.3+0.2*i, mpkis[:,i], 0.2, label=f"BLOCK SIZE={blocksizes[i]}")
    plt.xticks(x_axis,traces)
    plt.ylabel("MPKI")
    plt.xlabel("Trace")
    plt.title("MPKI vs Block Size for various traces")
    plt.legend()
    plt.savefig("figures/block_size_mpki.png")
    plt.show()
    plt.close()

# plot_repl("Inclusive")
# plot_repl("NonInclusive")
# plot_repl("Exclusive")
plot_incl()