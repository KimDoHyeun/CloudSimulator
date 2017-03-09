import Host
import gpu
import cpu

class edge_switch:


    def __init__(self,ID):
	
	self.ID = ID
	self.Host = []

    def add_host(self,host):

	self.Host.append(host)	
