[![PyPI](https://img.shields.io/badge/pypi-0.2-blue.svg)](https://pypi.python.org/pypi/pvyos/0.2)

# pvyos
"Pvyos" is a combination of "python" and "vyos". Pvyos is a simple library build on pexpect to connect and configure Vyos OS.

Python 3.5.2

#### Requires:
pexpect >= 4.2.1+

#### Support:
- Routing (Static,RIP,OSPF)
- System (User,Hostname)
- Service (SSH,Telnet,DNS)
- Interface (Ethernet, Loopback)

# Instalation
```
python3 -m pip install pvyos
```

# Example

##### Static Routing
```
import pvyos

device = pvyos.routing("192.168.1.10","vyos","vyos")
device.telnet_connection()
device.static("99.99.99.0","24","192.168.1.2")
device.commit()
device.closecon()
```

# Documentation
Pvyos is a library that can be use as easy as possible. Pvyos have 4 main component.

## Routing
The first thing you need to configure routing is declare a variable.

```
device = pvyos.routing("ipaddress","username","password")
```

after that, use telnet_connection() fungtion to connect to the device with telnet protocol.

```
device.telnet_connection()
```

then you can configure static,rip, or ospf routing protocol.

#### Static
after establish a connection, use this following command to configure static route.
```
device.static("ipnetwork","netmask","nexthop","distance")
```

* ipnetwork format  : x.x.x.x
* netmask format    : 0-32
* nexthop format    : x.x.x.x
* distance format   : 1-255

#### RIP
after establish a connection, use this following command to configure RIP.
```
device.rip("network/netmask")
```
* network netmask format : x.x.x.x/y

#### OSPF

## Interfaces
The first thing you need to configure interfaces is declare a variable.

```
device = pvyos.interfaces("ipaddress","username","password")
```

after that, use telnet_connection() fungtion to connect to the device with telnet protocol.

```
device.telnet_connection()
```
#### ethernet
after establish a connection, use this following command to configure ethernet interfaces.
```
device.ethernet("ethernet name","ipaddress","description")
```
* ipaddress format  : x.x.x.x/y
* ethernet name     : ethx
* description       : string

#### loopback
after establish a connection, use this following command to configure loopback interfaces.
```
device.loopback("loopback name","ipaddress")
```
* ipaddress format  : x.x.x.x/y
* loopback name     : lox (see your device config)
