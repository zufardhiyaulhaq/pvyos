import router
import pexpect
from pexpect import pxssh

class routing(router.vyos):

    def static(self,network,netmask,nexthop,distance="1"):
        
        if (self.session == None):
            return False
        else:
            session = self.session

        session.sendline("set protocols static route %s/%i next-hop %s distance '%s'",network,netmask,nexthop,distance)

    def rip(self):
        pass
    
    def ripv2(self):
        pass
    
    def ospf(self):
        pass