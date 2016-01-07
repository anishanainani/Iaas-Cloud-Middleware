virsh reboot $1
virsh migrate --live $1 qemu+ssh://$2/system --unsafe
