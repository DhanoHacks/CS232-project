Repo for CS232 Project - Memory/Cache hierarchy optimizations for Graph Analytics
Members:
* Dhananjay Raman (210050044)
* Adyasha Patra (210050007)
* Mridul Agarwal (210050100)

Usage:
* Move all relevant files for any metric you want to test for, to the relevant ChampSim folder
* Put either bash script in ChampSim folder to generate bulk data
* Already generated data is in data/ directory
* All results generated from relevant functions in data/generate_plot.py

Key Points:
* Traces used: bfs-14.trace.gz, cc-14.trace.gz ,sssp-14.trace.gz
* Cache sizes tested for L2C: 512 KB, 1 MB, 2 MB, 4 MB; for LLC: 2 MB, 4 MB, 8 MB, 16 MB
* Tested 0 size L2C and 0 size LLC caches by completely bypassing them
* Replacement policies tested: lru, random, lfu, fifo, mru, drrip, srrip, ship
* Inclusive, Exclusive and Noninclusive caches implemented and tested against all replacement policies
  
[results](results.md)