import pexpect
from pexpect import pxssh
from .router import vyos

class interface(vyos):

    def __init__(self,ipaddr,username,password):
        super().__init__(ipaddr,username,password)

    def ethernet(self,interface,address,description,duplex='auto',speed='auto'):
        if (self.session == None):
            return False
        else:
            session = self.session

        session.sendline("set interfaces ethernet %s address '%s'"%(interface,address))
        session.sendline("set interfaces ethernet %s description '%s'"%(interface,description))
        session.sendline("set interfaces ethernet %s duplex '%s'"%(interface,duplex))
        session.sendline("set interfaces ethernet %s speed '%s'"%(interface,speed))


    def loopback(self,interface,address):
        if (self.session == None):
            return False
        else:
            session = self.session

        session.sendline("set interfaces ethernet %s address '%s'"%(interface,address))
        session.sendline("set interfaces ethernet %s description '%s'"%(interface,description))
