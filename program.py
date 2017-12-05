import pvyos

device = pvyos.protocols("192.168.1.10","vyos","vyos")
device.telnet_connection()
device.static("16.10.10.0","24","192.168.1.2")
device.commit()

