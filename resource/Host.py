import gpu
import cpu

class Host:

    def __init__(self,ram,ID):
        self.CPU = []
        self.GPU = []
	self.switch = None
	self.Ram =ram
	self.Remaining_Ram = ram
	self.Host_ID = ID

    def add_cpu(self,cpu):

	self.CPU.append(cpu)

    def add_gpu(self,gpu):

	self.GPU.append(gpu)
