import libvirt

conn = libvirt.openReadOnly(None)  # $LIBVIRT_DEFAULT_URI, or give a URI here
assert conn, 'Failed to open connection'

names = conn.listDefinedDomains()
domains = map(conn.lookupByName, names)

ids = conn.listDomainsID()
running = map(conn.lookupByID, ids)

columns = 3

states = {
    libvirt.VIR_DOMAIN_NOSTATE: 'no state',
    libvirt.VIR_DOMAIN_RUNNING: 'running',
    libvirt.VIR_DOMAIN_BLOCKED: 'blocked on resource',
    libvirt.VIR_DOMAIN_PAUSED: 'paused by user',
    libvirt.VIR_DOMAIN_SHUTDOWN: 'being shut down',
    libvirt.VIR_DOMAIN_SHUTOFF: 'shut off',
    libvirt.VIR_DOMAIN_CRASHED: 'crashed',
}
def info(dom):
    [state, maxmem, mem, ncpu, cputime] = dom.info()
    info = dom.info()
    print 'Name : %s' % dom.name()    
    print 'State : %s' % info[0]
    print 'Max Memory : %d' % info[1]
    print 'Current Memory Usage : %d' % info[2]
    print 'Number of CPUs : %d' % info[3]
    print 'CPU UpTime (in ns) : %d' % info[4]

print 'Defined domains:'
for row in map(None, *[iter(domains)] * columns):
    for domain in row:
        if domain:
            info(domain)
	    print '---------------------------------------------------------------'
    print
print

print 'Running domains:'
for row in map(None, *[iter(running)] * columns):
    for domain in row:
        if domain:
            info(domain)
	    print '----------------------------------------------------------------'
    print
