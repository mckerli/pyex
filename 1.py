import subprocess as sp
import sys

proc = sp.Popen(["/hdd/Lizzie/leelaz","-w","/hdd/Lizzie/network.gz","-g"], stderr=sp.PIPE, universal_newlines=True)
#out,err = proc.communicate()
while True:    
    print("ok: ",proc.stderr.readline().rstrip('\r\n'))
##print(out)
#print(out.decode('utf-8'))