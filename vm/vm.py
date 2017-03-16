class vm:

    def __init__(self,vm_id):

	self.host_id = []
	self.host_list = []
	self.resource_list = []
	self.workload = []
	self.Workload_handler = None
	self.core_num = 0
	self.sm_num = 0
	self.gpu_mem = 0
	self.mem = 0
	self.ram = 0
	self.gflops = 0
	self.mips = 0
	self.vm_id = vm_id
	self.state = -1

    def allocate_workload(self, workload):
	self.workload.append(workload)

    def register_host(Host):
	self.host_id.append(Host.Host_ID)
	self.host_list.append(Host)
	self.resource_list.append(vm_host_resource(0,0,0,0))
    def unregister_host(Host):
	k = self.host_id.index(Host.Host_ID)
	self.host_id[k] = None
	self.host_list[k] =None
	self.resource_list[k] = None
	self.host_id = filter(None,self.host_id)
	self.host_list = filter(None,self.host_list)
	self.resource_list = filter (None,self.resource_list)

    def allocate_core(self, Host, num):

	if Host.Host_ID in self.host_id:
	    if Host.get_core(self.vm_id):
		k= self.host_id.index(Host.Host_ID)
		self.resource_list[k].core = self.resource_list[k].core + num
	 	self.core = self.core + num
		return True
	    else :
		return False
	else :
	    return False
		    
    def allocate_mem(self,Host , num):

    def allocate_gpu(self,Host,num,mem):  

    def process_vm():

	return 0

class vm_host_resource:

    def __init__(self, core,ram,sm,gpu_ram):
	self.core = core
	self.sm = sm
	self.ram = ram
	self.gpu_ram = ram
