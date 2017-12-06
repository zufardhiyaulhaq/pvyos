from .router import vyos
import pexpect
from pexpect import pxssh

class system(vyos):

    def __init__(self,ipaddr,username,password):
        super().__init__(ipaddr,username,password)

    def user(self,username,passwd,fullname="fullname"):

        if (self.session == None):
            return False
        else:
            session = self.session

        session.sendline("set system login user %s full-name '%s'"%(username,fullname))
        session.sendline("set system login user %s authentication plaintext-password %s"%(username,passwd))
        session.sendline("set system login user %s level admin"%(username))
    
    def hostname(self,name):

        if (self.session == None):
            return False
        else:
            session = self.session

        session.sendline("set system hostname %s"%(name))

    
