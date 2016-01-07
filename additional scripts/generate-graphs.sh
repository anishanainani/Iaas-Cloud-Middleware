while [ true ]
do
    python monitor.py --graph --hour 1 cpu_wio node0 > /dev/null 2>&1
    python monitor.py --graph --hour 1 cpu_idle node0 > /dev/null 2>&1
    python monitor.py --graph --hour 1 cpu_system node0 > /dev/null 2>&1
    python monitor.py --graph --hour 1 cpu_user node0 > /dev/null 2>&1
    python monitor.py --graph --hour 1 mem_free node0 > /dev/null 2>&1
    python monitor.py --graph --hour 1 mem_total node0 > /dev/null 2>&1
    python monitor.py --graph --hour 1 mem_cached node0 > /dev/null 2>&1
    python monitor.py --graph --hour 1 disk_free node0 > /dev/null 2>&1
    python monitor.py --graph --hour 1 disk_total node0 > /dev/null 2>&1

    python monitor.py --graph --hour 1 cpu_wio node1 > /dev/null 2>&1
    python monitor.py --graph --hour 1 cpu_idle node1 > /dev/null 2>&1
    python monitor.py --graph --hour 1 cpu_system node1 > /dev/null 2>&1
    python monitor.py --graph --hour 1 cpu_user node1 > /dev/null 2>&1
    python monitor.py --graph --hour 1 mem_free node1 > /dev/null 2>&1
    python monitor.py --graph --hour 1 mem_total node1 > /dev/null 2>&1
    python monitor.py --graph --hour 1 mem_cached node1 > /dev/null 2>&1
    python monitor.py --graph --hour 1 disk_free node1 > /dev/null 2>&1
    python monitor.py --graph --hour 1 disk_total node1 > /dev/null 2>&1

    python monitor.py --graph --hour 1 cpu_wio node2 > /dev/null 2>&1
    python monitor.py --graph --hour 1 cpu_idle node2 > /dev/null 2>&1
    python monitor.py --graph --hour 1 cpu_system node2 > /dev/null 2>&1
    python monitor.py --graph --hour 1 cpu_user node2 > /dev/null 2>&1
    python monitor.py --graph --hour 1 mem_free node2 > /dev/null 2>&1
    python monitor.py --graph --hour 1 mem_total node2 > /dev/null 2>&1
    python monitor.py --graph --hour 1 mem_cached node2 > /dev/null 2>&1
    python monitor.py --graph --hour 1 disk_free node2 > /dev/null 2>&1
    python monitor.py --graph --hour 1 disk_total node2 > /dev/null 2>&1
    sleep 5
done
