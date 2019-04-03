import sys
import subprocess
import threading

from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit,

    QInputDialog, QApplication)

proc = subprocess.Popen(["/hdd/Lizzie/leelaz","-w","/hdd/Lizzie/network.gz","-g"], stderr=subprocess.PIPE, universal_newlines=True)
#out,err = proc.communicate()

def readProc():
    while True:    
        print("ok: ",proc.stderr.readline().rstrip('\r\n'))

t = threading.Thread(target=readProc)
t.start()

app = QApplication([])

dialog = QInputDialog()

dialog.show()

app.exec_()



