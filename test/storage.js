/* eslint-disable */
const sc = artifacts.require('./Storage.sol') // eslint-disable-line

function addHours (date, hours) {
  const newDate = new Date(date)
  newDate.setHours(newDate.getHours() + hours)
  return newDate
}

contract('Storage', accounts => { // eslint-disable-line

  it('...should create the demo contract', async () => {
    const instance = await sc.deployed()
    const version = await instance.getVersion()
    assert.equal(version.toString(), "1.0", 'The version is wrong')
  })

  it('...should set data', async () => {
    const instance = await sc.deployed()

    const data = 'simple data'
    await instance.set(data)

    const dataSaved = await instance.get();
    console.log(dataSaved)

    assert.equal(dataSaved, data, 'Not data created correctly')
  })


})
