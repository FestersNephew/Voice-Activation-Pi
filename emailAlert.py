import smtplib

# Set the threshold values for the sensors
moisture_threshold = 50
temperature_threshold = 30
humidity_threshold = 70
pH_threshold = 7

# Set up the email server
server = smtplib.SMTP('smtp.example.com')
server.starttls()
server.login("your_email_address", "your_email_password")

# Set up the I2C bus
bus = smbus.SMBus(1)

while True:
    # Read the sensor data
    moisture = read_moisture_sensor()
    temperature = read_temperature_sensor()
    humidity = read_humidity_sensor()
    pH = read_pH_sensor()

    # Check if any of the sensor values are outside the threshold
    if moisture < moisture_threshold:
        message = (f"Moisture Alert!\n"
                   f"Moisture level is currently {moisture}%, which is below the threshold of {moisture_threshold}%.")
        server.sendmail("sender_email_address", "recipient_email_address", message)
    if temperature > temperature_threshold:
        message = (f"Temperature Alert!\n"
                   f"Temperature is currently {temperature}°C, which is above the threshold of {temperature_threshold}°C.")
        server.sendmail("sender_email_address", "recipient_email_address", message)
    if humidity < humidity_threshold:
        message = (f"Humidity Alert!\n"
                   f"Humidity is currently {humidity}%, which is below the threshold of {humidity_threshold}%.")
        server.sendmail("sender_email_address", "recipient_email_address", message)
    if pH < pH_threshold:
        message = (f"pH Alert!\n"
                   f"pH is currently {pH}, which is below the threshold of {pH_threshold}.")
        server.sendmail("sender_email_address", "recipient_email_address", message)


##if you want to send to multiple recipients:
#server.sendmail("sender_email_address", ["recipient_email_address_1", "recipient_email_address_2"], message)
