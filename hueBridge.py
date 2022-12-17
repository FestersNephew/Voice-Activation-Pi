from phue import Bridge

# Connect to the bridge
b = Bridge('192.168.1.2')

# Get a list of all the lights
lights = b.lights

# Turn all the lights on
for light in lights:
    light.on = True

# Set the brightness of all the lights to 50%
for light in lights:
    light.brightness = 128

# Set the color of all the lights to green
for light in lights:
    light.xy = [0.41, 0.517]