import time
import copy


class Block():
    """
    block parameters
    blockCount: serial number of blocks mined
    transactions: transactions stored in a block
    lastHash: hash of the previous block in the blockchain
    timestamp: time of creation of the block
    forger: validator who mined the block
    signature: signature of the forger
    """
    def _init_(self, transactions, lastHash, forger, blockCount):
        self.blockCount = blockCount
        self.transactions = transactions
        self.lastHash = lastHash
        self.timestamp = time.time()
        self.forger = forger
        self.signature = ''

    """
    Genesis block details
    timestamp = 0. Time of creation of blockchain.
    returns genesis block
    """
    @staticmethod
    def genesis():
        genesisBlock = Block([], 'genesisHash', 'genesis', 0)
        genesisBlock.timestamp = 0
        return genesisBlock

    """
    appends valid transactions to the block
    returns the list of transactions
    """
    def toJson(self):
        data = {}
        data['blockCount'] = self.blockCount
        data['lastHash'] = self.lastHash
        data['signature'] = self.signature
        data['forger'] = self.forger
        data['timestamp'] = self.timestamp
        jsonTransactions = []
        for transaction in self.transactions:
            jsonTransactions.append(transaction.toJson())
        data['transactions'] = jsonTransactions
        return data

    def payload(self):
        jsonRepresentation = copy.deepcopy(self.toJson())
        jsonRepresentation['signature'] = ''
        return jsonRepresentation

    """
    signature of the forger
    """
    def sign(self, signature):
        self.signature = signature