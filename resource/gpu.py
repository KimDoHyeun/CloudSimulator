


class gpu:

    gpu_num = 0
    def __init__(self,GFLOPS,MEMORY,BANDWIDTH,SM) :

	self.GPU_ID = gpu.gpu_num
	self.Gflops = GFLOPS
	self.Memory = MEMORY
	self.Bandwidth = BANDWIDTH
	self.SM_NUMBER = SM
	self.vm_list = []
	self.vm_resource_list = []
	gpu.gpu_num = gpu.gpu_num + 1

        self.Available_sm = SM
	self.Gflops_per_sm = GFLOPS/SM
	self.Available_mem = MEMORY
	self.Available_Gflops = GFLOPS

    def get_available_sm(self):

	return self.Available_sm

    def get_available_mem(self):

	return self.Available_mem

    def allocate_sm_mem(self, sm_num,mem ,vm_id):

        if sm_num > self.Available_sm :
            return False
	if mem > self.Available_mem:
	    return False
        if vm_id in self.vm_list :
            k = self.vm_list.index(vm_id)
            self.vm_resource_list[k].sm = self.vm_resource_list[k].sm + sm_num
	    self.vm_resource_list[k].mem = self.vm_resource_list[k].sm +mem
        else :
            self.vm_list.append(vm_id)
            self.vm_resource_list.append(gpu_resource(sm_num,mem))

        self.Available_Gflops = self.Available_Gflops - (sm_num * self.Gflops_per_sm)
        self.Available_sm = self.Available_sm - sm_num
	self.Available_mem = self.Available_mem - mem

        return sm_num * self.Gflops_per_sm , mem

    def deallocate_sm_mem_all(self, vm_id):

        if vm_id in self.vm_list :
            k = self.vm_list.index(vm_id)
            self.Available_sm = self.Available_sm + self.vm_resource_list[k].sm
            self.Available_Gflops = self.Available_Gflops + self.vm_resource_list[k].sm * self.Gflops_per_sm
	    self.Available_mem = self.Available_mem +self.vm_resource_list[k].mem
            self.vm_list[k] = None
            self.vm_resource_list[k] = None
            self.vm_list = filter(None,self.vm_list)
            self.vm_resource_list = filter(None,self.vm_resource_list)

            return True
        else :
            return False

    def deallocate_sm_mem(self, sm_num,mem, vm_id):

        if vm_id in self.vm_list :
            k = self.vm_list.index(vm_id)

            if self.vm_sm_list[k].sm < sm_num :
                dec = self.vm_sm_list[k].sm
            else :
                dec = sm_num
	    if self.vm_sm_list[k].mem < mem :
                dec_mem = self.vm_sm_list[k].mem
            else :
                dec_mem = mem

            self.Available_sm = self.Available_sm + dec
	    self.Available_mem = self.Available_mem + dec_mem
            self.Available_Gflops = self.Available_Gflops + (dec*self.Gflops_per_sm)
            self.vm_resource_list[k].sm = self.vm_resource_list[k].sm - dec
	    self.vm_resource_list[k].mem = self.vm_resource_list[k].mem - dec
            if self.vm_resource_list[k].sm == 0 and self.vm_resource_list[k].mem == 0:
                self.vm_list[k] = None
                self.vm_resource_list[k] = None
                self.vm_list = filter(None,self.vm_list)
                self.vm_sm_list = filter(None,self.vm_core_list)
            return dec,dec_mem

        else :
            return False

class gpu_resource:

    def __init__(self,sm,mem):
	
	self.sm = sm
	self.mem = mem



a = gpu (10,10,10,10)

print a.allocate_sm_mem(1,1,1)
print a.vm_resource_list
print a.allocate_sm_mem(1,1,1)
print a.allocate_sm_mem(1,1,2)
print a.allocate_sm_mem(1,1,3)
print a.allocate_sm_mem(1,1,4)
print a.vm_resource_list[0].sm
