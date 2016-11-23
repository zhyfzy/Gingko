import paramiko
import os
import xml.dom.minidom
import time
import threading

import sys
from PyQt4 import QtCore, QtGui, uic

qtCreatorFile = "src\\sftpclient\\sftp.ui"  # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class sftp(threading.Thread):
    def __init__(self,addr, port, pkey, local_path, remote_path, command, pathinfile):
        threading.Thread.__init__(self)
        self.addr = addr
        self.port = port
        self.pkey = pkey
        self.local_path = local_path
        self.remote_path = remote_path
        self.command = command
        self.pathinfile = pathinfile

    def run(self):
        with paramiko.Transport((self.addr, int(self.port))) as transport:
            transport.connect(username='admin', password='admin', pkey=self.pkey)
            sftp = paramiko.SFTPClient.from_transport(transport)
            sftp.put(self.local_path, self.remote_path, selfinstall=True, command=self.command, pathinfile=self.pathinfile)


class MyApp(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self._ok.clicked.connect(self.__ok)
        self._add.clicked.connect(self.__add)
        self._del.clicked.connect(self.__del)
        self._choose.clicked.connect(self.__choose)
        self._run.clicked.connect(self.__run)
        self._additem.clicked.connect(self.__additem)
        self._item.setText('127.0.0.1')
        self._net.setText('192.168.201.1-255')
        self._port.setText('1996')
        self._installor.setText('asset\\client\\cloudmusic.exe')
        self._key.setText('asset\\rsa_demo.key')
        self.itemnum = 0

    def __ok(self):
        print('input content = %s' %self._net.text())
        command = "nmap -sP " + str(self._net.text()) + " -oX result.xml"
        ret = os.system(command)
        dom = xml.dom.minidom.parse('result.xml')
        root = dom.documentElement
        bb = root.getElementsByTagName('host')
        i = 0
        addr = []
        while (i <= len(bb) - 1):
            cc = bb[i].getElementsByTagName('address')
            addr.append(str(cc[0].getAttribute("addr")))
            i = i + 1
        self._list1.addItems(addr)

    def __add(self):
        self._list2.addItem(str(self._list1.currentItem().text()))
        self.itemnum = self.itemnum + 1

    def __del(self):
        item = self._list2.takeItem(self._list2.currentRow())
        item = None
        self.itemnum = self.itemnum - 1

    def __choose(self):
        print('ok')

    def __additem(self):
        self._list2.addItem(str(self._item.text()))
        self.itemnum = self.itemnum + 1

    def __run(self):
        self._state.addItem("Starting...")
        port = int(self._port.text())
        command = str(self._command.text())
        pathinfile = str(self._pathinfile.text())
        local_path = str(self._installor.text())
        remote_path = local_path.split('\\')[-1]
        key = self._key.text()
        pkey = paramiko.RSAKey.from_private_key_file(key)

        if command=="":
            command = 'none'

        if pathinfile=="":
            pathinfile = 'none'

        i = 0


        while (i <= self.itemnum - 1):
            item = self._list2.item(i)
            addr = str(item.text())

            self._state.addItem("processing "+ str(addr) + " ...")
            print("processing %s ..." %addr)

            try:
                trans = sftp(addr, port, pkey, local_path, remote_path, command, pathinfile)
                trans.setDaemon(True)
                trans.start()
                self._state.addItem('Start transport ' + str(addr) + ' successfully')
            except:
                self._state.addItem('Transportation to '+ str(addr) + ' failed')

            i = i + 1

        print('Done')
        self._state.addItem("Done.")



if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())