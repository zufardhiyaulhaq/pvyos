import pexpect
from pexpect import pxssh

from .router import telnet_connection,ssh_connection
from .routing import rip,ripv2,ospf

__version__ = "0.0.1"
