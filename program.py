import pvyos

# device = pvyos.protocols("192.168.1.10","vyos","vyos")
# device.telnet_connection()
# device.static("99.99.99.0","24","192.168.1.2")
# device.commit()
# device.closecon()

device = pvyos.services("192.168.1.10","vyos","vyos")
device.telnet_connection()
device.dnsforwarder("8.8.4.4","eth0")
device.commit()
device.closecon()

# device = pvyos.system("192.168.1.10","vyos","vyos")
# device.telnet_connection()
# device.user("zufar","zufar","zufard")
# device.commit()
# device.closecon()



