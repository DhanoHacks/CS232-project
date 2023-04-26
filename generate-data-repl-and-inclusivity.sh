rm results_30M/*
# for way in {"drrip","srrip","lru","random","lfu","fifo","mru","ship"}
sed -i 's/#define .*HIERARCHY/#define NONINCLUSIVE_CACHE_HIERARCHY/' inc/champsim.h
for way in {"drrip","srrip","lru","random","lfu","fifo","mru","ship"}
do
    ./build_champsim.sh gshare no no no no $way 1
    ./run_champsim.sh gshare-no-no-no-no-$way-1core 30 30 bfs-14.trace.gz &
    ./run_champsim.sh gshare-no-no-no-no-$way-1core 30 30 cc-14.trace.gz &
    ./run_champsim.sh gshare-no-no-no-no-$way-1core 30 30 sssp-14.trace.gz &
    wait
done
cp results_30M/* ~/data/noninclusive/

sed -i 's/#define .*HIERARCHY/#define INCLUSIVE_CACHE_HIERARCHY/' inc/champsim.h
for way in {"drrip","srrip","lru","random","lfu","fifo","mru","ship"}
do
    ./build_champsim.sh gshare no no no no $way 1
    ./run_champsim.sh gshare-no-no-no-no-$way-1core 30 30 bfs-14.trace.gz &
    ./run_champsim.sh gshare-no-no-no-no-$way-1core 30 30 cc-14.trace.gz &
    ./run_champsim.sh gshare-no-no-no-no-$way-1core 30 30 sssp-14.trace.gz &
    wait
done
cp results_30M/* ~/data/inclusive/

sed -i 's/#define .*HIERARCHY/#define EXCLUSIVE_CACHE_HIERARCHY/' inc/champsim.h
for way in {"drrip","srrip","lru","random","lfu","fifo","mru","ship"}
do
    ./build_champsim.sh gshare no no no no $way 1
    ./run_champsim.sh gshare-no-no-no-no-$way-1core 30 30 bfs-14.trace.gz &
    ./run_champsim.sh gshare-no-no-no-no-$way-1core 30 30 cc-14.trace.gz &
    ./run_champsim.sh gshare-no-no-no-no-$way-1core 30 30 sssp-14.trace.gz &
    wait
done
cp results_30M/* ~/data/exclusive/
sed -i 's/#define .*HIERARCHY/#define NONINCLUSIVE_CACHE_HIERARCHY/' inc/champsim.h