


class cpu:

    CPU_NUM = 0

    def __init__(self, MIPS, core_num):

      	self.Mips = MIPS
	self.Available_Mips = MIPS
	
	self.CPU_ID = cpu.CPU_NUM
   	cpu.CPU_NUM = cpu.CPU_NUM + 1
	
	self.vm_list = []
	self.vm_core_list = []
	self.Mips_per_core = MIPS/core_num
	
	self.core_num = core_num
	self.Available_core = core_num

    def get_available_core(self):
	
	return self.Available_core

    def allocate_core(self, core_num, vm_id):
			
	if core_num > self.Available_core :
	    return False
	
	if vm_id in self.vm_list :
	    k = self.vm_list.index(vm_id)	
	    self.vm_core_list[k] = self.vm_core_list[k] + core_num
	    
	else :
	    self.vm_list.append(vm_id)
	    self.vm_core_list.append(vm_id)
	    
	self.Available_Mips = self.Available_Mips - (core_num * self.Mips_per_core)
        self.Available_core = self.Available_core - core_num

	return core_num * self.Mips_per_core

    def deallocate_vm_all(self, vm_id):
	
	if vm_id in self.vm_list :
	    k = self.vm_list.index(vm_id)
	    self.Available_core = self.Available_core + self.vm_core_list[k]
	    self.Available_Mips = self.Available_Mips + self.vm_core_list[k] * self.Mips_per_core
	    self.vm_list[k] = None
	    self.vm_core_list[k] = None
	    self.vm_list = filter(None,self.vm_list)
	    self.vm_core_list = filter(None,self.vm_list)
	
	    return True
	else :
	    return False

    def deallocate_vm(self, vm_id, num):
	
	if vm_id in self.vm_list :
	   
	else :
	    return False
	
    
a = cpu (4,4)

print a.allocate_core(3,1)
print a.allocate_core(1,1)
print a.deallocate_vm_all(1)
