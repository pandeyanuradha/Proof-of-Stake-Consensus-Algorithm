# Proof of Stake Consensus Algorithm

Proof of Stake consensus requires nodes to have enough stake to become a validator. Validators are **selected at random** to validate and mine blocks. Greater the stake, greater are the chances of getting selected.

## Requirements

1. Python 3.x
2. Flask
3. Requests
4. Postman
5. Pycryptodome module
6. p2pnetwork module

## Overview of Code

All the nodes having a stake are considered for random selection for mining a block. Nodes having greater stake, have a greater chance of selection. Stakers is a dictionary which maps the account of a miner to the number of token held by that account. Lots are created for each token (stake) available at the miner. A lot is a unit, representing the miner’s opportunity to get selected in the random selectionprocess of the miner. More the number of tokens, means more number of lots, which indicates greater probability of selection. *Lots[]* is an array of lots of each individual miner.

<img src = "https://github.com/pandeyanuradha/Proof-of-Stake-in-Python/blob/main/images/image-010.jpg" width = "550" height = "500" />

*validatorLots()* fills the *Lots[]* with their values.
*winnerLots()* is the random selection process, which selects the winner based on the least offset compared to referenceHashIntValue.

Once the miner is selected as a forger, the block is mined by the miner and distributed across the network.

<img src = "https://github.com/pandeyanuradha/Proof-of-Stake-in-Python/blob/main/images/image-011.jpg" width = "550" height = "500" />

