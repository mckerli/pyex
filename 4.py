import sys
import threading
import pexpect
import math
from PyQt5 import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
"""
sdfksjlksdf
sdf
sdf
sdfsdfsdf
"""

class CPan(QWidget):
    def __init__(self,parent=None):
        super(CPan, self).__init__(parent)
        self.setMouseTracking(True)
    
    def mouseMoveEvent(self, event):
        
        sz = self.size()
        ww = sz.width() 
        w = math.trunc(ww / 20)
        s = math.trunc((ww - w * 20) / 2)
        x = math.trunc((event.x() - (s+w/2)) / w)
        y = math.trunc((event.y() - (s+w/2)) / w)
        
        txt = "Mouse 위치 ; x={0},y={1}, global={2},{3}".format(event.x(), event.y(), x,y)
        ex.statusbar.showMessage(txt)
        #print(event.globalX())

    def _pos(self,x,y):
        ar = "ABCDEFGHJKLMNOPQRST"
        print(ar[x],19-y)
        return "{0}{1}".format(ar[x],19-y)

    def mouseReleaseEvent(self, event):
        sz = self.size()
        ww = sz.width() 
        w = int(ww / 20)
        s = int((ww - w * 20) / 2)

        if(event.x() < s+w/2):
            return 
        if(event.y() < s+w/2):
            return
        
        x = int((event.x() - (s+w/2)) / w)
        y = int((event.y() - (s+w/2)) / w)
        if(x>18 or y>18):
            return
        s = self._pos(x,y)
        ex.proc.sendline("play b "+s)
        ex.proc.sendline("showboard")
        
        print(x,y,s)

    def paintEvent(self,event):
        
        painter = QPainter()
        painter.begin(self)
        painter.setPen(QPen(Qt.yellow))
        painter.setBrush(QBrush(Qt.gray, Qt.SolidPattern))
        sz = self.size()
        ww = sz.width() 
        hh = sz.height()
        painter.drawRect(QRectF(0, 0, ww-1, hh-1) )
        zz = math.trunc(min(ww,hh))
        w = math.trunc(zz / 20)
        sx = math.trunc((ww - w * 20) / 2)
        sy = math.trunc((hh - w * 20) / 2)
        #painter.drawRect(QRectF(sx,sy,sx+w*20-1,sy+w*20-1) )

        for i in range(19):
            painter.drawLine(sx+w,sy+w+i*w,sx+w*19,sy+w+i*w)
            painter.drawLine(sx+w+i*w,sy+w,sx+w+i*w,sy+19*w)
        
        painter.end()
        print(w,sx,sy)


class MyMain(QMainWindow):
    def __init__(self):
        super().__init__()
        self.threadActive = True;
        self.proc = pexpect.spawn( "/hdd/Lizzie/leelaz",["-w","/hdd/Lizzie/network.gz","-g"],timeout=None)
        self.thread = threading.Thread(target=self.readProc)
        self.thread.start()
        self.statusbar = self.statusBar()
        
        self.cpan = CPan()
        self.cpan.setParent(self)
        #print(self.hasMouseTracking())
        #self.resized.connect(self.someFunction)
        self.setGeometry(300, 200, 400, 200)
        #self.show()
        self.showMaximized()

    def readProc(self):
        while self.threadActive:
            print("ok: ",self.proc.readline())
        print("process stopping...")

    

    def resizeEvent(self, event):
        #self.resized.emit()
        #self.cpan.resize(self,event.size().width,event.size().height)
        w = event.size().width()
        h = event.size().height()  - self.statusBar().height() 
        
        sz = int(min(w,h))
        self.cpan.move((w-sz)/2,(h-sz)/2)
        
        self.cpan.resize(sz,sz)
        print(event.size().width(),event.size().height(),sz,w,h)
        return super(MyMain, self).resizeEvent(event)
       
    
       
    def closeEvent(self, event):
        """
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
        """
        self.threadActive = False
        self.proc.sendline("quit")
        
        event.accept()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyMain()
    sys.exit(app.exec_())