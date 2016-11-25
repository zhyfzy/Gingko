# Gingko

A batch processing self-install tool 

一个通过SFTP传输文件并在目标机中执行自动安装的工具

使用```Python 2.7```实现

## SFTPClient使用前的准备

SFTPClient 用于给多个```SFTPserver```批量分发安装包，并在运行```SFTPserver```的主机中安装这些文件

SFTPClient 已经实现了与用户的交互```UI```

使用前需要安装```cryptography```、```nmap```和```PyQt4```

安装cryptography

    $ pip install cryptography
	
在[这里](https://nmap.org/download.html)下载windows版本的```nmap```，以及在[这里](https://riverbankcomputing.com/software/pyqt/download)下载```PyQt```（选择python2.7版本），并执行安装

## SFTPserver使用前准备

SFTPserver接受来自```SFTPclient```的安装包以及自动安装命令（该命令通过修改```paramiko```底层代码实现，所以需要事先删除通过```pip```等安装的原版```paramiko```，并使用src目录中修改过的）

SFTPserver既可以在```Windows```中使用(```Windows 7```和```Windows 10```中测试通过)，也可以在```linux```中使用(```Ubuntu 16.04 LTS```测试通过)

（仅 windows 下）使用前需要将 winrar 的目录添加到环境变量``path``中，并进行测试

    $ winrar

安装cryptography

    $ pip install cryptography
	
启动SFTPserver

    $ ./src/sftpserver/__init__.py -k ./asset/rsa_demo.key -p 1996 --host=192.168.102.130

请设置```-k```为您自己的rsa私钥文件地址，```-p```为端口号，```--host server```服务器ip地址

注意，因为涉及程序的安装，需要为 SFTPserver 提供管理员权限

## 使用方法

参数``command``和``path in file``用于自动安装
    
如果传输的是压缩包，服务器会自动识别安装包并解压，但是需要给定``path in file``，为可执行文件在压缩包中位置

另外允许用户指定安装命令，在``command``中输入安装参数。
比如``command``设置为 ``-s``
在客户端会自动执行

    $ path/to/exe -s
