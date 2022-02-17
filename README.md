![GitHub Actions](https://img.shields.io/badge/githubactions-%232671E5.svg?style=for-the-badge&logo=githubactions&logoColor=white)
![Ethereum](https://img.shields.io/badge/Ethereum-3C3C3D?style=for-the-badge&logo=Ethereum&logoColor=white)
![Solidity](https://img.shields.io/badge/Solidity-%23363636.svg?style=for-the-badge&logo=solidity&logoColor=white)
![Jest](https://img.shields.io/badge/-jest-%23C21325?style=for-the-badge&logo=jest&logoColor=white)

# Solidity with python

A simple example to show how to connect python with blockchain smart contracts.

## Prerequisites

- [node and npm](https://nodejs.org/en/download/)

* [Truffle framework](https://trufflesuite.com/)

- [Infura](https://infura.io/): Account and Key to access to a blockchain's node.

* [Alchemy](https://www.alchemy.com/): Alternative to infura.

- [Python and pip](https://www.python.org/downloads/)

## Installation

1. Clone this repository with git

2. Install nodeJs, npm and python

3. Create an Infura or Alchemy Accounts

4. Install truffle framework (npm install -g truffle)

5. Install python dependencies (pip install web3)

6. Install dependencies (npm i)

7. Compile and migrate contracts

```sh
truffle develop
```

After truffle console start:

```sh
compile
migrate
```

Those steps will create the smart contracts binaries inside the `./compiled/contracts` folder. You could change that in trufle-config.js.

## Testing

In this repo, only we could create the smart contracts binaries and run tests over them. Inside truffle console (truffle develop):

```sh
truffle develop
test
```

## Deploy to testnet

To deploy to test network.

```sh
# replace <NET> with desire network: rinkeby, goerli, mainnet
truffle migrate --reset --network <NET>
```

## Run example in python

```py
python3 example.py  -r <Provider> -e <providerKeyEth> -p <providerKeyPolygon> -a <addressAcount> -k <addressAccountKey> -n <networkToUse>

# Provider: INFURA or ALCHEMY
# Provider Key Eth: Your Key (in Infura is your projectId)
# Provider Key Polygon: Your Key
# Address Account: An Address to use with contract
# Address Key: Key from Address Account
# Network To Use: RINKEBy or POLYGON (if you need other network, you have yo change example code in example.py)
```

## Contract Addresses

These are the networks and addresses where contract is deployed:

- Ethereum testnet (rinkeby): [0xb497D1572210AAF11D0C39b8307dC73EAB480cfC](https://rinkeby.etherscan.io/address/0xb497D1572210AAF11D0C39b8307dC73EAB480cfC)
- Polygon testnet (mumbai): [0xf05eD004881fD8B0eeeAed908d53FDdD43525C12](https://mumbai.polygonscan.com/address/0xf05eD004881fD8B0eeeAed908d53FDdD43525C12)

## More Details

- [Linters and Formatters](./.doc/linters.md)

* [Networks y Faucets](networks.md)
