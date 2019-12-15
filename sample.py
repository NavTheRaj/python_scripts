mystring="Dec 10 10:27:45 test-server dhcpd: rid: 60:2a:d0:76:2a:91"
rid_loc=mystring.rfind("rid:")
if rid_loc > 0:
    print('Mac: ',mystring[rid_loc+5:])
