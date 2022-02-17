/* eslint-disable */
const sc = artifacts.require('storage')

module.exports = async (deployer, network, accounts) => {
  // unlock account
  if (network.startsWith('develop')) {
    web3.eth.personal.unlockAccount(accounts[0], null, 36000)
  }

  // Se puede usar async/await, pero dentro de un primer then, por issue 713
  // https://github.com/trufflesuite/truffle/issues/713
  deployer.then(async () => {
    console.log('\n***** Deploying contracts begin *****\n')

    let deployAddress
    
    if (network.startsWith('develop')) {
      deployAddress = accounts[0]
    } else {
      deployAddress = accounts[0]
    }
    console.log('\Deploy address: '+ deployAddress)

    await deployer.deploy(sc)

    console.log('\n***** Deploying contracts end *****\n')

  }).then(async () => {
    await DoSomething(deployer, network, accounts)
  })

}

DoSomething = async (deployer, network, accounts) => {
  // Nothing for now, maybe some intialize or mock
  const instance = await sc.deployed();
  console.log('contrat version => ', await instance.getVersion())
}
