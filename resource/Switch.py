import Host
import gpu
import cpu

class Switch:


    def __init__(self,ID):
	self.connection = []
	self.Host = []
	self.Switch_ID = -1

	self.Switch_ID = ID

    def add_Host(self,host):

	self.Host.append(host)
	host.switch = self

    def add_switch(self,switch):

	self.connection.append(switch)
	print("connected "+str(switch[0].Switch_ID)+"-"+str(self.Switch_ID))
	print(len(self.connection))
