rm results_30M/*

l2_size=(1024 2048 4096 8192)
l2_latencies=(10 20 30 40)

# for x in {0,}
for i in ${!l2_size[@]}
do
    x=${l2_size[$i]}
    latency=${l2_latencies[$i]}
    sed -i 's/L2C_SET [0-9]*/L2C_SET '$x'/' inc/cache.h
    sed -i 's/L2C_LATENCY [0-9]*/L2C_LATENCY '$latency'/' inc/cache.h
    ./build_champsim.sh gshare no no no no lru 1
    ./run_champsim.sh gshare-no-no-no-no-lru-1core 30 30 bfs-14.trace.gz
    ./run_champsim.sh gshare-no-no-no-no-lru-1core 30 30 cc-14.trace.gz
    ./run_champsim.sh gshare-no-no-no-no-lru-1core 30 30 sssp-14.trace.gz
    cp results_30M/* ~/data/l2_size_$x/
done
sed -i 's/L2C_SET [0-9]*/L2C_SET 1024/' inc/cache.h
sed -i 's/L2C_LATENCY [0-9]*/L2C_LATENCY 10/' inc/cache.h

# for x in {0,}

# llc_size=(2048 4096 8192 16384)
# latencies=(20 30 40 50)
# for i in ${!llc_size[@]}
# do
#     x=${llc_size[$i]}
#     latency=${latencies[$i]}
#     sed -i 's/LLC_SET NUM_CPUS\*[0-9]*/LLC_SET NUM_CPUS\*'$x'/' inc/cache.h
#     sed -i 's/LLC_LATENCY [0-9]*/LLC_LATENCY '$latency'/' inc/cache.h
#     ./build_champsim.sh gshare no no no no lru 1
#     ./run_champsim.sh gshare-no-no-no-no-lru-1core 30 30 bfs-14.trace.gz
#     ./run_champsim.sh gshare-no-no-no-no-lru-1core 30 30 cc-14.trace.gz
#     ./run_champsim.sh gshare-no-no-no-no-lru-1core 30 30 sssp-14.trace.gz
#     cp results_30M/* ~/data/llc_size_$x/
# done
# sed -i 's/LLC_SET NUM_CPUS\*[0-9]*/LLC_SET NUM_CPUS\*2048/' inc/cache.h
# sed -i 's/LLC_LATENCY [0-9]*/LLC_LATENCY 20/' inc/cache.h