from Wallet import Wallet
from BlockchainUtils import BlockchainUtils
import requests


def postTransaction(sender, receiver, amount, type):
    transaction = sender.createTransaction(
        receiver.publicKeyString(), amount, type)
    url = "http://localhost:5000/transaction"
    package = {'transaction': BlockchainUtils.encode(transaction)}
    request = requests.post(url, json=package)


if __name__ == '__main__':

    anurodh = Wallet()
    vamsi = Wallet()
    vamsi.fromKey('keys/stakerPrivateKey.pem')
    exchange = Wallet()

    #forger: genesis
    postTransaction(exchange, vamsi, 100, 'EXCHANGE')
    postTransaction(exchange, anurodh, 100, 'EXCHANGE')
    postTransaction(exchange, anurodh, 10, 'EXCHANGE')

    # forger: probably vamsi
    postTransaction(vamsi, vamsi, 25, 'STAKE')
    postTransaction(vamsi, anurodh, 1, 'TRANSFER')
    postTransaction(vamsi, anurodh, 1, 'TRANSFER')
