import sys
import threading
import pexpect
from PyQt5.QtWidgets import *


class MyMain(QMainWindow):
    def __init__(self):
        super().__init__()
        self.threadActive = True;
        self.proc = pexpect.spawn( "/hdd/Lizzie/leelaz",["-w","/hdd/Lizzie/network.gz","-g"],timeout=None)
        self.thread = threading.Thread(target=self.readProc)
        self.thread.start()
        self.thread.join()
        self.statusbar = self.statusBar()
        
        print(self.hasMouseTracking())
        #quit = QAction("Quit", self)
        #quit.triggered.connect(self.close)
        self.setGeometry(300, 200, 400, 200)
        self.show()

    def readProc(self):
        while self.threadActive:
            print("ok: ",self.proc.readline().decode())
        print("stopped")

    def mouseMoveEvent(self, event):
        
        txt = "Mouse 위치 ; x={0},y={1}, global={2},{3}".format(event.x(), event.y(), event.globalX(), event.globalY())
        self.statusbar.showMessage(txt)
        #print(event.globalX())

    def mouseReleaseEvent(self, event):
        cmd = "showboard"
        self.proc.sendline(cmd)
        print("mouse released")
        #self.testSignal.emit('mouse release')
        #super(MyWidget, self).mouseReleaseEvent(event)

    def closeEvent(self, event):
        close = QMessageBox()
        close.setText("You sure?")
        close.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        close = close.exec()

        if close == QMessageBox.Yes:
            self.threadActive = False
            self.proc.sendline("quit")
            event.accept()
            print("closing ok")
        else:
            event.ignore()
            print("closing canceled")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyMain()
    sys.exit(app.exec_())