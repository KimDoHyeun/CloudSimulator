import gpu
import cpu

class Host:

    CPU = []
    GPU = []
    Ram = 0
    Remaining_Ram = 0
    Host_ID = 0

    def __init__(self,ram,ID):

	self.Ram =ram
	self.Remaining_Ram = ram
	self.Host_ID = ID

    def add_cpu(self,cpu):

	self.CPU.append(cpu)

    def add_gpu(self,gpu):

	self.GPU.append(gpu)
