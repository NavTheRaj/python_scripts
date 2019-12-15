import getpass
import time
from netmiko import ConnectHandler, file_transfer

host = "10.0.0.1"
u = "cisco"
p = "cisco"
source_file = "c800-universalk9-mz.SPA.155-3.M5.bin"

router = {
    'device_type': "cisco_ios",
    'ip': host,
    'username': u,
    'password': p,
}

try:
    ssh_conn = ConnectHandler(**router)
    print ("Connection successful\n")
except:
    print ("Login failure\n")
    sys.exit()


