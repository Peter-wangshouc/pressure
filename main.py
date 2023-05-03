BMP280.power_on()
BMP280.address(BMP280_I2C_ADDRESS.ADDR_0X76)

def on_forever():
    basic.show_number((101400 - BMP280.pressure()) * 0.328084 * 0.3048)
    basic.pause(100)
basic.forever(on_forever)
