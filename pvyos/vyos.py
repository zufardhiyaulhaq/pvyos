class vyos():

    type = "vyos-devices"

    def __init__(self,ipaddr,username,password):
        self.ipaddr=ipaddr
        self.username=username
        self.password=password
    
    def telnet_connection(self):
        session = pexpect.spawn("telnet "+self.ipaddr,timeout=5)
        result = session.expect(["login: ",pexpect.TIMEOUT])

        if (result!=0):
            return False

        session.sendline(self.username)
        result = session.expect(["Password: ",pexpect.TIMEOUT])

        if (result!=0):
            return False

        session.sendline(self.password)

        result = session.expect(["$ ",pexpect.TIMEOUT])

        if (result!=0):
            return False

        else:
            self.session = session
            return True

        