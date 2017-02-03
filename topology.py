import resource.cpu
import resource.gpu
import resource.Switch
import resource.Host

class Topology :

     
     def __init__(self):
	self.Switch_num = 0
        self.Switch_list = []
        self.Host_num = 0
        self.cpu_num = 0
        self.gpu_num = 0


     def create_host(self, ram):

	host = resource.Host.Host(ram, self.Host_num)
	self.Host_num = self.Host_num + 1
	return host
	
     def create_cpu(self,mips):
	
	cpu = resource.cpu.cpu(mips,self.cpu_num)
	self.cpu_num = self.cpu_num + 1

	return cpu

     def create_gpu(self,gflops, memory, bandwidth, sm) :

	gpu = resource.gpu.gpu(self.gpu_num, gflops, memory, bandwidth, sm)
	self.gpu_num = self.gpu_num + 1

 	return gpu

     def create_switch(self):

	switch = resource.Switch.Switch(self.Switch_num)
	self.Switch_num = self.Switch_num + 1
	self.Switch_list.append(switch)
        return switch

     def connect_switch(self,id_1,id_2,cost) :
	tmp=[]
	tmp.append(self.Switch_list[id_2])
	tmp.append(cost)
	self.Switch_list[id_1].add_switch(tmp)
	tmp=[]
	tmp.append(self.Switch_list[id_1])
        tmp.append(cost)
	self.Switch_list[id_2].add_switch(tmp)

def Fat_tree(k,mips,cpu_number,gflops,gpu_number,gpu_memory,bandwidth,sm_num,ram,cost):

    topology = Topology()
    
    for i in range((k/2)*(k/2)):
	
	topology.create_switch()

    j = 0

    for i in range((k/2)*k):

	switch = topology.create_switch()
	for q in range((k/2)):
	
	    topology.connect_switch(switch.Switch_ID ,j,1)
	
            print str(i)+" "+str(q) +" "+ str(j)+" " +str(switch.Switch_ID)
	    j = j + 1
        j = j % ((k/2)*(k/2)) 

    for i in range((k/2)*k):

	switch = topology.create_switch()

	for q in range((k/2)):

	    topology.connect_switch(switch.Switch_ID,switch.Switch_ID - switch.Switch_ID % (k/2) - ((k/2)*2) + q ,1)
	    print str(switch.Switch_ID)+" "+str(switch.Switch_ID - switch.Switch_ID % (k/2) - ((k/2)*2) + q)
	for q in range((k/2)):
	    
	    host = topology.create_host(ram)
	    
	    for x in range(cpu_number):

		cpu = topology.create_cpu(mips)
		host.add_cpu(cpu)

            for x in range(gpu_number):

                gpu = topology.create_gpu(gflops,gpu_memory,bandwidth,sm_num)
                host.add_gpu(gpu)



	    switch.add_Host(host)

    return topology     

top= Fat_tree(22,1,1,1,1,1,1,1,1,1)

for k in top.Switch_list:

    print(str(k.Switch_ID)+" connected with")
    for q in k.connection:
	print(q[0].Switch_ID)
