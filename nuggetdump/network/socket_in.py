import socket as s
from nuggetdump.utils.validators import ServerValidators

class ServerKinda(object):
    def __init__(self, myaddr, blacklist=None, whitelist=None, redirect=None):
        ServerValidators.validate_server_instantiation_args(myaddr, blacklist, whitelist, redirect)
        super(ServerKinda, self).__init__()




    def init_sock(self, alt_port):
        #TODO: THIS.
        pass
