import smbus

# Set up the I2C bus
bus = smbus.SMBus(1)

# Read the moisture sensor
def read_moisture_sensor():
    # Replace with the correct address and register for your sensor
    moisture = bus.read_word_data(0x20, 0x00)
    return moisture

# Read the temperature sensor
def read_temperature_sensor():
    # Replace with the correct address and register for your sensor
    temperature = bus.read_word_data(0x40, 0x00)
    return temperature

# Read the humidity sensor
def read_humidity_sensor():
    # Replace with the correct address and register for your sensor
    humidity = bus.read_word_data(0x50, 0x00)
    return humidity

# Read the pH sensor
def read_pH_sensor():
    # Replace with the correct address and register for your sensor
    pH = bus.read_word_data(0x60, 0x00)
    return pH
