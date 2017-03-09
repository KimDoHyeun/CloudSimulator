


class gpu:

    gpu_num = 0
    def __init__(self,GFLOPS,MEMORY,BANDWIDTH,SM) :

	self.GPU_ID = gpu.gpu_num
	self.Gflops = GFLOPS
	self.Memory = MEMORY
	self.Bandwidth = BANDWIDTH
	self.SM_NUMBER = SM
	self.vm_list = []
	gpu.gpu_num = gpu.gpu_num + 1
