rm results_30M/*

# for x in {1024,2048,4096,8192}
for x in {0,}
do
    # sed -i 's/L2C_SET [0-9]*/L2C_SET '$x'/' inc/cache.h
    ./build_champsim.sh gshare no no no no lru 1
    ./run_champsim.sh gshare-no-no-no-no-lru-1core 30 30 bfs-14.trace.gz
    ./run_champsim.sh gshare-no-no-no-no-lru-1core 30 30 cc-14.trace.gz
    ./run_champsim.sh gshare-no-no-no-no-lru-1core 30 30 sssp-14.trace.gz
    cp results_30M/* ~/data/l2_way_$x/
done
# sed -i 's/L2C_SET [0-9]*/L2C_SET 1024/' inc/cache.h

# for x in {2048,4096,8192,16384}
# for x in {0,}
# do
#     sed -i 's/LLC_SET NUM_CPUS\*[0-9]*/LLC_SET NUM_CPUS\*'$x'/' inc/cache.h
#     ./build_champsim.sh gshare no no no no lru 1
#     ./run_champsim.sh gshare-no-no-no-no-lru-1core 30 30 bfs-14.trace.gz
#     ./run_champsim.sh gshare-no-no-no-no-lru-1core 30 30 cc-14.trace.gz
#     ./run_champsim.sh gshare-no-no-no-no-lru-1core 30 30 sssp-14.trace.gz
#     cp results_30M/* ~/data/llc_way_$x/
# done
# sed -i 's/LLC_SET NUM_CPUS\*[0-9]*/LLC_SET NUM_CPUS\*2048/' inc/cache.h