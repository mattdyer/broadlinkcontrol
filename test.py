import broadlink

devices = broadlink.discover(timeout=5)

print devices[0].auth()

print devices[0].check_temperature()
