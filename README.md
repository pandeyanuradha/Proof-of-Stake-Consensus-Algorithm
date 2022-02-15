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

<img src = "https://github.com/pandeyanuradha/Proof-of-Stake-in-Python/blob/main/images/image-010.jpg" width = "550" height = "440" />

*validatorLots()* fills the *Lots[]* with their values. <br /> *winnerLots()* is the random selection process, which selects the winner based on the least offset compared to referenceHashIntValue.

Once the miner is selected as a forger, the block is mined by the miner and distributed across the network.

<img src = "https://github.com/pandeyanuradha/Proof-of-Stake-in-Python/blob/main/images/image-011.jpg" width = "550" height = "440" />

## Working

The genesis block is the miner of the first non-genesis block.

<img src = "https://github.com/pandeyanuradha/Proof-of-Stake-in-Python/blob/main/images/image-001.png" width = "600" height = "300" />


The screenshots show, initially the block running at 10001 port (genesis block) is the validator, while the other block at 10002 port is not a validator.


<img src = "https://github.com/pandeyanuradha/Proof-of-Stake-in-Python/blob/main/images/image-002.png" width = "600" height = "300" />


Blocks added to the chain can be viewed at http://localhost:(apiPort)/blockchain.

<img src = "https://github.com/pandeyanuradha/Proof-of-Stake-in-Python/blob/main/images/image-003.png" width = "600" height = "300" />
<img src = "https://github.com/pandeyanuradha/Proof-of-Stake-in-Python/blob/main/images/image-004.png" width = "600" height = "300" />


Using Postman API, one can add transactions, mine blocks, view transactions pool, verify transactions and connect to new nodes. The complete blockchain history can be accessed at http://localhost:5000/blockchain.


<img src = "https://github.com/pandeyanuradha/Proof-of-Stake-in-Python/blob/main/images/image-005.png" width = "700" height = "400" />
<img src = "https://github.com/pandeyanuradha/Proof-of-Stake-in-Python/blob/main/images/image-006.png" width = "700" height = "400" />

The information about the blockchain network can be viewed at http://localhost:5000/info.

<img src = "https://github.com/pandeyanuradha/Proof-of-Stake-in-Python/blob/main/images/image-007.png" width = "900" height = "300" />

At http://localhost:5000/transactionPool, all the transactions which have been validated but not mined yet are present.

<img src = "https://github.com/pandeyanuradha/Proof-of-Stake-in-Python/blob/main/images/image-008.png" width = "700" height = "300" />

<img src = "https://github.com/pandeyanuradha/Proof-of-Stake-in-Python/blob/main/images/image-009.png" width = "700" height = "300" />


