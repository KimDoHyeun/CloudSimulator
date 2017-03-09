class vm:

    vm_num = 0
    def __init__(self,vm_id):

	self.cpu = []
	self.gpu = []
	self.workload = []
	self.Workload_handler = None
	self.ram = 0
	self.vm_id = vm_id
	self.state = -1
