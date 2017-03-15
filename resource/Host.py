import gpu
import cpu

class Host:

    Host_NUM = 0
    def __init__(self,ram):
        self.CPU = []
        self.GPU = []
	self.switch = None
	self.Ram =ram
	self.Remaining_Ram = ram
	self.Host_ID = Host.Host_NUM
	Host.Host_NUM = Host.Host_NUM + 1
	self.vm_list = []
	self.available_core = 0
	self.available_sm = 0
	self.available_gpu_mem = 0
    def add_cpu(self,MIPS,core_num):

	self.CPU.append(cpu(MIPS,core_num))
	self.available_core = self.available_core + core_num

    def add_gpu(self,gflops,memory,bandwidth,sm):

	self.GPU.append(gpu(gflops,memory,bandwidth,sm))
	self.available_gpu_mem = self.available_gpu_mem + memory
	self.available_sm = self.available_sm + sm


# delete cpu, gpu
# allocate host resource to real vm instance
# deallocate host resource to vm instance
# ram memory allocation map with vm 
# cpu gpu ->record which vm use resource host -> need to record this data to vm instance

    def get_core(self,vm_id,num):
	mips_tmp = 0
	if self.available_core <num :
	    
	    return None
	else :
	    for k in self.CPU:
		if k.Available_core >0 :
		    if k.Available_core < tmp:
			tmp = tmp - k.Available_core
			self.available_core= self.available_core - k.Available_core
			k.allocate_core(k.Available_core,vm_id)
			cpu_list.append(k)
		    else :
			k.allocate_core(tmp,vm_id)
			self.available_core = self.availalbe_core - tmp
			tmp = 0
			cpu_list.append(k)
		if tmp == 0 :
		    break

	    return cpu_list
    def get_gpu(self,vm_id,num,mem):

    def release_core(self,vm_id,num):
	
    def release_gpu(self,vm_id,num,mem):




