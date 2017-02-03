


class gpu:

    GPU_ID = -1
    Gflops = 0
    Memory = 0
    Bandwidth = 0
    SM_number = 0
    VM_list = []

    def __init__(self,ID,GFLOPS,MEMORY,BANDWIDTH,SM) :

	self.GPU_ID = ID
	self.Gflops = GFLOPS
	self.Memory = MEMORY
	self.Bandwidth = BANDWIDTH
	self.SM_NUMBER = SM


