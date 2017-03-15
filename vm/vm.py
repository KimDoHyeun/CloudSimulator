class vm:

    def __init__(self,vm_id):

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


    def allocate_core(self, Host, num):
	if Host.get_core(num) is True:
	    tmp = True
	    for k in self.hostlist:
		if k.Host_ID == Host.Host_ID
		    tmp = False
	    if tmp :
		self.hostlist.append(Host)
	    self.core_num = self.core_num + num
	    self.mips = self.mips + Host

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
