from BlockchainUtils import BlockchainUtils


class Lot():
    def __init__(self, publicKey, iteration, lastBlockHash):
        self.publicKey = str(publicKey)
        self.iteration = iteration
        self.lastBlockHash = str(lastBlockHash)

    def lotHash(self):
        hashData = self.publicKey + self.lastBlockHash
        for _ in range(self.iteration):
            hashData = BlockchainUtils.hash(hashData).hexdigest()
        return hashData


"""Keeps track of stake amongst nodes"""

class ProofOfStake():

    """
    stakers maintains a dictionary which map account to node
    """
    def _init_(self):
        self.stakers = {}
        self.setGenesisNodeStake()

    def setGenesisNodeStake(self):
        genesisPublicKey = open('keys/genesisPublicKey.pem', 'r').read()
        self.stakers[genesisPublicKey] = 1

    """
    updates stakes in the nodes
    """
    def update(self, publicKeyString, stake):
        if publicKeyString in self.stakers.keys():
            self.stakers[publicKeyString] += stake
        else:
            self.stakers[publicKeyString] = stake

    """
    returns stake to publicKeyString
    """
    def get(self, publicKeyString):
        if publicKeyString in self.stakers.keys():
            return self.stakers[publicKeyString]
        else:
            return None

    """
    generating all the lots for the specific validator
    lots[] : list consisting of all the lots
    """
    def validatorLots(self, seed):
        lots = []
        for validator in self.stakers.keys():
            for stake in range(self.get(validator)):
                lots.append(Lot(validator, stake+1, seed))
        return lots

    """
    takes the list of lots to select a winner
    selected: winner of the lot
    referenceHashIntValue: it is the hash value compared to all lots
    leastOffset: holds the value of lowest offset value between lots and referenceHashIntValue
    """
    def winnerLot(self, lots, seed):
        winnerLot = None
        leastOffset = None
        referenceHashIntValue = int(BlockchainUtils.hash(seed).hexdigest(), 16)
        for lot in lots:
            lotIntValue = int(lot.lotHash(), 16)
            offset = abs(lotIntValue - referenceHashIntValue)
            if leastOffset is None or offset < leastOffset:
                leastOffset = offset
                winnerLot = lot
        return winnerLot

    """
    this class generates the winner by calling the rest of the functions
    """
    def forger(self, lastBlockHash):
        lots = self.validatorLots(lastBlockHash)
        winnerLot = self.winnerLot(lots, lastBlockHash)
        return winnerLot.publicKey