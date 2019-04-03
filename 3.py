import sys
import subprocess
import threading
from PyQt5.QtWidgets import *


class MyMain(QMainWindow):
    def __init__(self):
        super().__init__()


        self.proc = subprocess.Popen(["/hdd/Lizzie/leelaz","-w","/hdd/Lizzie/network.gz","-g"], stderr=subprocess.PIPE,stdin = subprocess.PIPE, universal_newlines=True)
        #out,err = proc.communicate()
        self.t = threading.Thread(target=self.readProc)
        self.t.start()
        self.statusbar = self.statusBar()

        print(self.hasMouseTracking())
        self.setMouseTracking(True)   # True 면, mouse button 안눌러도 , mouse move event 추적함.
        print(self.hasMouseTracking())

        self.setGeometry(300, 200, 400, 200)
        self.show()

    def readProc(self):
        while True:    
            print("ok: ",self.proc.stderr.readline().rstrip('\r\n'))

    def mouseMoveEvent(self, event):
        
        txt = "Mouse 위치 ; x={0},y={1}, global={2},{3}".format(event.x(), event.y(), event.globalX(), event.globalY())
        self.statusbar.showMessage(txt)
        #print(event.globalX())

    def mouseReleaseEvent(self, event):
        cmd = "showboard\n"
        self.proc.stdin.write(cmd)
        shprint("mouse released")
        #self.testSignal.emit('mouse release')
        #super(MyWidget, self).mouseReleaseEvent(event)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyMain()
    sys.exit(app.exec_())