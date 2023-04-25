rm results_30M/*

./build_champsim.sh gshare no no no no lru 1
./run_champsim.sh gshare-no-no-no-no-lru-1core 30 30 bfs-14.trace.gz
./run_champsim.sh gshare-no-no-no-no-lru-1core 30 30 cc-14.trace.gz
./run_champsim.sh gshare-no-no-no-no-lru-1core 30 30 sssp-14.trace.gz

cp results_30M/* ~/data/inclusive/