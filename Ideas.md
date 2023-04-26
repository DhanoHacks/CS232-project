# Replacement policies implemented and plotted:
* LRU
* LFU
* FIFO
* RANDOM
* MRU
* SRRIP


About **SSRIP**: 
High Performance Cache Replacement Using Re-Reference Interval Prediction (RRIP)
Aamer Jaleel † Kevin B. Theobald ‡ Simon C. Steely Jr. † Joel Emer †

Fig 3 explains the working of SRRIP
1. We propose cache replacement using Re-reference Interval Prediction (RRIP). RRIP statically predicts the re-reference interval of all missing cache blocks to be an intermediate re-reference interval that is between a near-immediate re-reference interval and a distant re-reference interval. RRIP updates the re-reference prediction to be shorter than the previous prediction upon a re-reference. We call this policy as Static RRIP (SRRIP). We show that SRRIP is scan-resistant and only requires 2-bits per cache block.
2. We propose two SRRIP policies: SRRIP-Hit Priority (SRRIP-HP) and SRRIP-Frequency Priority (SRRIP-FP). SRRIP-HP predicts that any cache block that receives a hit will have a near-immediate re-reference and thus should be retained in the cache for an extended period of time. SRRIP-FP on the other hand predicts that frequently referenced cache blocks will have a near-immediate re-reference and thus they should be retained in the cache for an extended period of time. We show that SRRIP-HP performs significantly better than SRRIP-FP and conclude that scan-resistance is not from precisely detecting frequently referenced blocks but from preventing blocks that receive hits from getting evicted by blocks that do not receive hits (i.e., scan blocks).


**IMP** -- two policies to update the re-reference prediction: Hit Priority (HP) and Frequency Priority (FP). The RRIP-HP policy
predicts that the block receiving a hit will be re-referenced in the near-immediate future and updates the RRPV of the associated block
to zero. The goal of the HP policy is to prioritize replacement of blocks that do not receive cache hits over any cache block that receives a hit. However, the HP policy can potentially degrade cache performance when a cache block is re-referenced only once after cache insertion. In such situations, the HP policy incorrectly predicts a near-immediate re-reference prediction instead of distant re-reference prediction for the block and causes the block to occupy valuable cache space without receiving any hits. To address this problem, the RRIP-FP policy uses more information (i.e., cache hits) to update the re-reference prediction. Instead of updating the re-reference prediction to be near-immediate on a hit, RRIP-FP updates the predicted re-reference interval to be shorter than the previous re-reference interval each time a block receives a hit. The FP policy accomplishes this by decrementing the RRPV register (unless the RRPV register is already zero) on cache hits. The goal of the FP policy is to prioritize replacement of infrequently re-referenced cache blocks over frequently re-referenced cache blocks.

Other papers read which provide similar insight as Paper 1 but use software solutions in their core -- therefore we can't implement those
* GRASP
* GRACE
* CAGRA


ChampSim by default uses **NON-INCLUSIVE** cache hierarchy.
We implement :
1. INCLUSIVE
2. EXCLUSIVE


