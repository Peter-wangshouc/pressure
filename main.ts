BMP280.Address(BMP280_I2C_ADDRESS.ADDR_0x77)
basic.forever(function () {
    basic.showNumber(BMP280.pressure())
    basic.pause(100)
})
