import gpu
import cpu

class Host:

    Host_NUM = 0
    def __init__(self,ram,ID):
        self.CPU = []
        self.GPU = []
	self.switch = None
	self.Ram =ram
	self.Remaining_Ram = ram
	self.Host_ID = ID
	
    def add_cpu(self,MIPS,core_num):

	self.CPU.append(cpu(MIPS,core_num))

    def add_gpu(self,gflops,memory,bandwidth,sm):

	self.GPU.append(gpu(gflops,memory,bandwidth,sm))
# delete cpu, gpu
# allocate host resource to real vm instance
# deallocate host resource to vm instance
# ram memory allocation map with vm 
# cpu gpu ->record which vm use resource host -> need to record this data to vm instance






class vm_resource_map:

    def __init__(self, vmid):
	vm_id = vmid
