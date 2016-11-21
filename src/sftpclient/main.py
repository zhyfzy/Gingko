import paramiko
import os
import xml.dom.minidom
import time
import datetime

if __name__ == '__main__':
    com = raw_input("Enter your network segment like 192.168.1.1-255: ")
    command ="nmap -sP "+com+" -oX D:\\result.xml"
    ret = os.system(command)


    dom = xml.dom.minidom.parse('D:\\result.xml')
    root = dom.documentElement
    bb = root.getElementsByTagName('host')
    i = 0
    addr = []
    while(i <= len(bb)-1):
        cc = bb[i].getElementsByTagName('address')
        addr.append(str(cc[0].getAttribute("addr")))
        i = i + 1

    print addr

    pkey = paramiko.RSAKey.from_private_key_file('D:\si\private.key')

    trans = []
    i = 0
    while (i <= len(bb)-1):
        transport = paramiko.Transport((addr[i], 1996))
        transport.connect(username = 'admin', password = 'admin', pkey = pkey)
        sftp = paramiko.SFTPClient.from_transport(transport)

        # sftp.mkdir('Ctest/',mode=777)
        #sftp.chdir('/Users/klloshar/Desktop/test/')
        sftp.put('./cloudmusic.exe','./cloudmusic.exe')

        # files = sftp.listdir('/Users/klloshar/Desktop/yinxinghuang')
        # for f in files:
        #     print'Beginning to download file from %s %s ' % (addr[i], datetime.datetime.now())
        #     print'Downloading file:', os.path.join('/Users/klloshar/Desktop/yinxinghuang', f)
        #     sftp.get(os.path.join('/Users/klloshar/Desktop/yinxinghuang', f), os.path.join('/Users/klloshar/Desktop', f))
        #     print'Download file success %s ' % datetime.datetime.now()
        trans.append(sftp)
        i = i + 1

    while True:
        time.sleep(5)