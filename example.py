# Requirements:  
#
#  - pip install web3
#  - Register account in https://www.alchemy.com/ to get Ethereum and Polygon API Keys
#
# Use: python3 example.py  -r <Provider> -e <providerKeyEth> -p <providerKeyPolygon> -a <addressAcount> -k <addressAccountKey> -n <networkToUse>
#
from web3 import Web3
from web3.middleware import geth_poa_middleware
import sys, getopt

abi = [{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":False,"inputs":[],"name":"DataSetted","type":"event"},{"inputs":[],"name":"destroySmartContract","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"get","outputs":[{"internalType":"string","name":"_data","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getVersion","outputs":[{"internalType":"string","name":"_version","type":"string"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"string","name":"newData","type":"string"}],"name":"set","outputs":[],"stateMutability":"nonpayable","type":"function"}]

sc_adr_eth = '0xb497D1572210AAF11D0C39b8307dC73EAB480cfC'
sc_adr_polygon = '0xf05eD004881fD8B0eeeAed908d53FDdD43525C12'
alchemy_url_eth = 'https://eth-rinkeby.alchemyapi.io/v2/'
infura_url_eth= "https://rinkeby.infura.io/v3/"
alchemy_url_polygon = 'https://polygon-mumbai.g.alchemy.com/v2/'
infura_url_polygon = 'https://polygon-mumbai.infura.io/v3'
chain_id_eth = 4
chain_id_polygon = 80001
gas = 200000
valueInEther = 0


def getTrxParameters(w3, addressFrom, chanId, simple):
  if (simple):
    return {
      'from': addressFrom, 
      'nonce': w3.eth.getTransactionCount(addressFrom),
      'value': w3.toWei(valueInEther, "ether")
    } 
  else: 
    return {
      'from': addressFrom, 
      #'to': scCheckSum, # avoid error when send 'to' parameter with buildTransaction
      'gasPrice': w3.eth.gasPrice,
      'gas': gas, 
      'chainId': chanId, 
      'nonce': w3.eth.getTransactionCount(addressFrom),
      'value': w3.toWei(valueInEther, "ether")
    }


def process(w3, acc, sk, scAddress, chanId):
  print('Connected to blockchain.')
  
  scCheckSum = w3.toChecksumAddress(scAddress)
  sc = w3.eth.contract(address=scCheckSum, abi=abi)
  accBalance = w3.fromWei(w3.eth.getBalance(acc), "ether")

  print('client verion:', w3.clientVersion)
  print('Contract Version:', sc.functions.getVersion().call())
  print('account balance:', accBalance)

  if (accBalance < 0.5):
    print('the account does not have enough funds. 0.5 ether needed')
    sys.exit()

  data = 'CODE123456'

  raw_transaction = sc.functions.set(data).buildTransaction(getTrxParameters(w3, acc, chanId, True))
  signed = w3.eth.account.signTransaction(raw_transaction, sk)
  receipt = w3.eth.sendRawTransaction(signed.rawTransaction)

  # non-blocking
  print ('preview trx hash (trx could be in pending status)', w3.toHex(w3.keccak(signed.rawTransaction)))

  # blocking: Wait for the transaction to be mined, and get the transaction receipt
  print('receipt with confirmed trx hash (after trx executed)', w3.eth.waitForTransactionReceipt(receipt))

  result = sc.functions.get().call()
  print('\n\nresult saved in contract', result)



def getWeb3(providerUrl, providerKey):
  w3 = Web3(Web3.HTTPProvider(providerUrl+providerKey))

  # web3.exceptions.ExtraDataLengthError: The field extraData is 97 bytes, 
  # but should be 32. It is quite likely that you are connected to a POA chain. 
  # Refer to http://web3py.readthedocs.io/en/stable/middleware.html#geth-style-proof-of-authority 
  # for more details.
  w3.middleware_onion.inject(geth_poa_middleware, layer=0)
  return w3


def getBlkParams(provider, network, providerKeyEth, providerKeyPolygon):
  if (network == 'RINKEBY'):
    providerUrl = alchemy_url_eth if provider == 'ALCHMEY' else infura_url_eth 
    providerKey = providerKeyEth
    scAddress = sc_adr_eth
    chanId = chain_id_eth

  if (network == 'POLYGON'):
    providerUrl = alchemy_url_polygon if provider == 'ALCHMEY' else infura_url_polygon  
    providerKey = providerKeyPolygon
    scAddress = sc_adr_polygon
    chanId = chain_id_polygon

  return (providerUrl, providerKey, scAddress, chanId)


def getInputParams(argv):
  providerKeyEth = ''
  providerKeyPolygon = ''
  account = ''
  accountKey = ''
  provider = ''
  network = ''

  try:
    opts, args = getopt.getopt(argv,"he:p:a:k:n:r:",["eproviderKeyEth=","pproviderKeyPolygon=", "aaccount", "kaccountKey", "nnetwork", "rprovider"])
  except getopt.GetoptError:
    print ('Number of arguments: ' + str(len(sys.argv)) +  ' arguments.')
    print ('Argument List: ' + str(sys.argv))
    print ('example.py  -r <Provider> -e <providerKeyEth> -p <providerKeyPolygon> -a <addressAcount> -k <addressAccountKey> -n <networkToUse>')
    sys.exit(2)
  
  for opt, arg in opts:
    if opt == '-h':
      print ('example.py  -r <Provider> -e <providerKeyEth> -p <providerKeyPolygon> -a <addressAcount> -k <addressAccountKey> -n <networkToUse>')
      sys.exit()
    elif opt in ("-e", "--eproviderKeyEth"):
      providerKeyEth = arg
    elif opt in ("-p", "--pproviderKeyPolygon"):
      providerKeyPolygon = arg
    elif opt in ("-a", "--aaccount"):
      account = arg
    elif opt in ("-k", "--kaccountKey"):
      accountKey = arg
    elif opt in ("-r", "--rprovider"):
      provider = arg
    elif opt in ("-n", "--nnetwork"):
      network = arg

  if (len(sys.argv) == 1):
      print ("Error: Must need Alchemy keys as argument")
      print ('example.py  -r <Provider> -e <providerKeyEth> -p <providerKeyPolygon> -a <addressAcount> -k <addressAccountKey> -n <networkToUse>')
      print('\n')
  elif (len(providerKeyEth) == 0):
      print ('Error: invalid providerKeyEth')
      sys.exit()
  elif (len(providerKeyPolygon) == 0):
      print ('Error: invalid providerKeyPolygon')
      sys.exit()
  elif (len(account) == 0):
      print ('Error: invalid account')
      sys.exit()
  elif (len(accountKey) == 0):
      print ('Error: invalid accountKey')
      sys.exit()
  elif (len(provider) == 0 or (provider != 'ALCHEMY' and provider != 'INFURA')):
      print ('Error: invalid provider. Use INFURA or ALCHEMY')
      sys.exit()
  elif (len(network) == 0 or (network != 'RINKEBY' and network != 'POLYGON')):
      print ('Error: invalid network. Use RINKEBY or POLYGON')
      sys.exit()

  return provider, providerKeyEth, providerKeyPolygon, account, accountKey, network


def main(argv):
  provider, providerKeyEth, providerKeyPolygon, acc, sk, network = getInputParams(argv)
  providerUrl, providerKey, scAddress, chanId  = getBlkParams(provider, network, providerKeyEth, providerKeyPolygon)
  w3 = getWeb3(providerUrl, providerKey)

  if(not w3.isConnected()):
    print('Cannot establish a connection to blockchain.')
    sys.exit()
  else:
    process(w3, acc, sk, scAddress, chanId)


if __name__ == "__main__":
  main(sys.argv[1:])
