import libvirt
import sys

conn = libvirt.open("qemu:///system")
print conn.listDomainsID()
dom1 = conn.lookupByName('centos07')
print dom1.info()
for id in conn.listDomainsID():
	print 'Close'
	dom = conn.lookupByID(id)
	info = dom0.info()
	print 'ID = ', id
	print 'Name = ', dom.name()
	print 'State = ', info[0]
	print 'Max Memory = ', info[0]
	print 'Current Memory Usage = ', info[1]
	print 'Number of virt CPUs = ', info[2]
	print 'CPU Time = ', info[3]
	print ''

#state: one of the state values (virDomainState)
#maxMemory: the maximum memory used by the domain
#memory: the current amount of memory used by the domain
#nbVirtCPU: the number of virtual CPU
#cpuTime: the time used by the domain in nanoseconds
#http://stackoverflow.com/questions/4986076/alternative-to-virsh-libvirt
