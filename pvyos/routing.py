from .router import vyos
import pexpect
from pexpect import pxssh

class routing(vyos):

    def __init__(self,ipaddr,username,password):
        super().__init__(ipaddr,username,password)

    def static(self,network,netmask,nexthop,distance="1"):
        if (self.session == None):
            return False
        else:
            session = self.session

        session.sendline("set protocols static route %s/%s next-hop %s distance '%s'"%(network,netmask,nexthop,distance))

    def rip(self,network):
        if (self.session == None):
            return False
        else:
            session = self.session

        session.sendline("set protocols rip network %s"%(network))
    
    def ospf(self,network,area):
        if (self.session == None):
            return False
        else:
            session = self.session

        session.sendline("set protocols ospf area %s network %s"%(area,network))
        