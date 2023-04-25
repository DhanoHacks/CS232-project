rm results_30M/*

# for way in {"lru","random","lfu","fifo"}
for way in {"srrip",}
do
    ./build_champsim.sh gshare no no no no $way 1
    ./run_champsim.sh gshare-no-no-no-no-$way-1core 30 30 bfs-14.trace.gz
    ./run_champsim.sh gshare-no-no-no-no-$way-1core 30 30 cc-14.trace.gz
    ./run_champsim.sh gshare-no-no-no-no-$way-1core 30 30 sssp-14.trace.gz
done
cp results_30M/* ~/data/repl_policies/