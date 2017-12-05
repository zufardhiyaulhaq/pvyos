from .router import vyos
import pexpect
from pexpect import pxssh

class protocols(vyos):

    def __init__(self,ipaddr,username,password):
        super().__init__(ipaddr,username,password)

    def static(self,network,netmask,nexthop,distance="1"):
        if (self.session == None):
            return False
        else:
            session = self.session

        session.sendline("set protocols static route %s/%s next-hop %s distance '%s'"%(network,netmask,nexthop,distance))

    def rip(self):
        pass
    
    def ripv2(self):
        pass
    
    def ospf(self):
        pass