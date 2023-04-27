Repo for CS232 Project - Memory/Cache hierarchy optimizations for Graph Analytics
Members:
* Dhananjay Raman (210050044)
* Adyasha Patra (210050007)
* Mridul Agarwal (210050100)

Description:


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

References:
* [Analysis and Optimization of the Memory Hierarchy for Graph Processing Workloads​​](https://seal.ece.ucsb.edu/sites/default/files/publications/hpca-2019-abanti.pdf)

-Abanti Basak, Shuangchen Li, Xing Hu, Sang Min Oh, Xinfeng Xie, Li Zhao, Xiaowei Jiang, Yuan Xie

* [Data-Aware Cache Management for Graph Analytics​](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=9774709)

-Neelam Sharma, Varun Venkitaraman, Newton, Vikash Kumar, Shubham Singhania, Chandan Kumar Jha ​

* [Graphfire: Synergizing Fetch, Insertion, and Replacement Policies for Graph Analytics​](https://mrmgroup.cs.princeton.edu/papers/amanocha-toc2022.pdf)

-Aninda Manocha, Student Member, IEEE, Juan L. Aragón, Member, IEEE, and Margaret Martonosi, Fellow, IEEE​

* [Gretch: A Hardware Prefetcher for Graph Analytics​](https://www.cs.toronto.edu/ecosystem/papers/TACO_21/Gretch.pdf)

-ANIRUDH MOHAN KAUSHIK, GENNADY PEKHIMENKO, HIREN PATEL​

* [Exploring Core and Cache Hierarchy Bottlenecks in Graph Processing Workloads​​](https://par.nsf.gov/servlets/purl/10080635)

-Abanti Basak , Xing Hu, Shuangchen Li, Sang Min Oh , and Yuan Xie

* [EVALUATION OF CACHE INCLUSION POLICIES IN CACHE MANAGEMENT​​](https://core.ac.uk/download/pdf/147122148.pdf)

-A Thesis by LUNA BACKES DRAULT

​