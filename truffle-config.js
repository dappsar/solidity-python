require('babel-register')
require('babel-polyfill')
require('dotenv').config() // Store environment-specific variable from '.env' to process.env

const HDWalletProvider = require('@truffle/hdwallet-provider')
const path = require('path')

const PROVIDER = process.env.PROVIDER || 'INFURA'
const PROJECT_ID = process.env.PROJECT_ID || 'dummy' // dummy to avoid error en empty envirnment variable
const ALCHEMY_KEY = process.env.ALCHEMY_KEY || 'dumyy' // dummy to avoid error en empty envirnment variable
const MNENOMIC = process.env.MNENOMIC || 'dummy' // dummy to avoid error en empty envirnment variable
const INFURA_URL = process.env.INFURA_URL || 'https://kovan.NETWORK.io/v3/'
const ALCHEMY_URL = process.env.ALCHEMY_URL || 'https://eth-NETWORK.alchemyapi.io/v2/'
const FROM = process.env.FROM || '0x8A691b1B213843e7B66142b8EC3c8F07031689CE'

const PROVIDER_KEY = (PROVIDER && PROVIDER === 'ALCHEMY') ? ALCHEMY_KEY : PROJECT_ID // infura use project_id as jey
const PROVIDER_URL = (PROVIDER && PROVIDER === 'ALCHEMY') ? ALCHEMY_URL : INFURA_URL

if (!MNENOMIC || !PROJECT_ID || !PROVIDER_KEY) {
  console.error('********************************************************************************************')
  console.error('********************************************************************************************')
  console.error('')
  console.error('Please set a MNENOMIC, PROJECT_ID and INFURA/ALCHEMY KEY in an environment file (.env)')
  console.error('(if you want to use another network that localhost)')
  console.error('')
  console.error('********************************************************************************************')
  console.error('********************************************************************************************')
}

const PROVIDER_COMPLETE_URL = PROVIDER_URL + PROVIDER_KEY

module.exports = {
  networks: {
    // local network
    develop: {
      host: '127.0.0.1',
      port: 8545,
      network_id: 5777,
      gas: 29000000,
      gasPrice: 0x01, // low gas price
      confirmations: 2,
      BlockLimit: 0x6691b7
    },
    // test ethereum network
    ropsten: {
      networkCheckTimeout: 90000,
      provider: () => new HDWalletProvider(MNENOMIC, PROVIDER_COMPLETE_URL.replace('NETWORK', 'ropsten')),
      network_id: 3,
      gas: 29000000,
      gasPrice: 10000000000,
      from: FROM
    },
    // test ethereum network
    kovan: {
      networkCheckTimeout: 90000,
      provider: () => new HDWalletProvider(MNENOMIC, PROVIDER_COMPLETE_URL.replace('NETWORK', 'kovan')),
      network_id: 42,
      gas: 29000000,
      gasPrice: 10000000000,
      from: FROM
    },
    // test ethereum network
    rinkeby: {
      networkCheckTimeout: 90000,
      provider: () => new HDWalletProvider(MNENOMIC, PROVIDER_COMPLETE_URL.replace('NETWORK', 'rinkeby')),
      skipDryRun: true,
      confirmations: 2,
      timeoutBlocks: 50000,
      network_id: 4,
      gas: 29000000,
      gasPrice: 10000000000,
      from: FROM
    },
    // main ethereum network
    mainnet: {
      networkCheckTimeout: 90000,
      provider: () => new HDWalletProvider(MNENOMIC, PROVIDER_COMPLETE_URL.replace('NETWORK', 'mainnet')),
      skipDryRun: true,
      confirmations: 2,
      timeoutBlocks: 50000,
      network_id: 1,
      gas: 29000000,
      gasPrice: 10000000000,
      from: FROM
    },
    // test polygon network
    mumbai: {
      provider: () => new HDWalletProvider(MNENOMIC, PROVIDER_COMPLETE_URL.replace('NETWORK', 'polygon-mumbai')),
      network_id: 80001,
      confirmations: 2,
      timeoutBlocks: 200,
      skipDryRun: true,
      chainId: 80001
    },
    // main polygon network
    matic: {
      provider: () => new HDWalletProvider(MNENOMIC, PROVIDER_COMPLETE_URL.replace('NETWORK', 'polygon-mainnet')),
      network_id: 137,
      confirmations: 2,
      timeoutBlocks: 200,
      skipDryRun: true,
      chainId: 137
    }
  },
  contracts_build_directory: path.join(__dirname, './compiled/contracts'),
  contracts_directory: path.join(__dirname, './contracts/'),
  compilers: {
    solc: {
      version: '0.6.0',
      optimizer: {
        enabled: true,
        runs: 1500
      }
    }
  }
}
