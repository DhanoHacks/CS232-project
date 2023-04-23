import matplotlib.pyplot as plt
import re
import numpy as np

# varying LLC WAY
def plot_llc_way():
    llcways=[2048,4096,8192,16384]
    traces=['bfs-14.trace.gz','cc-14.trace.gz','sssp-14.trace.gz']
    baselines=np.zeros(shape=(1,len(traces)))
    speedups=np.zeros(shape=(len(traces),len(llcways)))
    mpkis=np.zeros(shape=(len(traces),len(llcways)))
    for i in range(len(llcways)):
        way=llcways[i]
        for j in range(len(traces)):
            trace=traces[j]
            with open(f"llc_way_{way}/{trace}-gshare-no-no-no-no-lru-1core.txt","r") as f:
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
    for i in range(len(llcways)):
        plt.bar(x_axis-0.3+0.2*i, speedups[:,i], 0.2, label=f"LLC WAY = {llcways[i]}")
    plt.xticks(x_axis,traces)
    plt.ylabel("Speedup")
    plt.xlabel("Trace")
    plt.title("Speedup vs LLC WAY for various trace")
    plt.legend()
    plt.savefig("llc_ways_speedup.png")
    plt.show()
    plt.close()

    for i in range(len(llcways)):
        plt.bar(x_axis-0.3+0.2*i, mpkis[:,i], 0.2, label=f"LLC WAY = {llcways[i]}")
    plt.xticks(x_axis,traces)
    plt.ylabel("MPKI")
    plt.xlabel("Trace")
    plt.title("MPKI vs LLC WAY for various trace")
    plt.legend()
    plt.savefig("llc_ways_mpki.png")
    plt.show()
    plt.close()


# varying L2 WAY
def plot_l2_way():
    l2ways=[1024,2048,4096,8192]
    traces=['bfs-14.trace.gz','cc-14.trace.gz','sssp-14.trace.gz']
    baselines=np.zeros(shape=(1,len(traces)))
    speedups=np.zeros(shape=(len(traces),len(l2ways)))
    mpkis=np.zeros(shape=(len(traces),len(l2ways)))
    for i in range(len(l2ways)):
        way=l2ways[i]
        for j in range(len(traces)):
            trace=traces[j]
            with open(f"l2_way_{way}/{trace}-gshare-no-no-no-no-lru-1core.txt","r") as f:
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
    for i in range(len(l2ways)):
        plt.bar(x_axis-0.3+0.2*i, speedups[:,i], 0.2, label=f"L2 WAY = {l2ways[i]}")
    plt.xticks(x_axis,traces)
    plt.ylabel("Speedup")
    plt.xlabel("Trace")
    plt.title("Speedup vs L2 WAY for various trace")
    plt.legend()
    plt.savefig("l2_ways_speedup.png")
    plt.show()
    plt.close()

    for i in range(len(l2ways)):
        plt.bar(x_axis-0.3+0.2*i, mpkis[:,i], 0.2, label=f"L2 WAY = {l2ways[i]}")
    plt.xticks(x_axis,traces)
    plt.ylabel("MPKI")
    plt.xlabel("Trace")
    plt.title("MPKI vs L2 WAY for various trace")
    plt.legend()
    plt.savefig("l2_ways_mpki.png")
    plt.show()
    plt.close()


# varying REPLACEMENT POLICY
def plot_repl():
    repls=["lru","random","lfu","fifo","mru","srrip"]
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
    for i in range(len(repls)):
        plt.bar(x_axis-0.39+0.13/2+0.13*i, speedups[:,i], 0.13, label=repls[i])
    plt.xticks(x_axis,traces)
    plt.ylabel("Speedup")
    plt.xlabel("Trace")
    plt.title("Speedup vs Replacement Policy for various trace")
    plt.legend()
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