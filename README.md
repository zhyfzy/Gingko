# Gingko

A batch processing self-install tool 

一个通过SFTP传输文件并在目标机中执行自动安装的工具

使用Python2.7实现

## SFTPClient使用前的准备

SFTPClient 用于给多个```SFTPserver```批量分发安装包，并在运行```SFTPserver```的主机中安装这些文件

SFTPClient 已经实现了与用户的交互```UI```

使用前需要安装```cryptography```、```nmap```和```PyQt4```

安装cryptography

    $ pip install cryptography
	
在[这里](https://nmap.org/download.html)下载windows版本的nmap，以及在[这里](https://riverbankcomputing.com/software/pyqt/download)下载PyQt（选择python2.7版本），并执行安装

## SFTPserver使用前准备

SFTPserver接受来自```SFTPclient```的安装包以及自动安装命令（该命令通过修改```paramiko```底层代码实现，所以需要事先删除通过```pip```等安装的原版```paramiko```，并使用src目录中修改过的）

SFTPserver既可以在```Windows```中使用(Windows7和Windows10中测试通过)，也可以在linux中使用(Ubuntu 16.04 LTS 测试通过)

使用前需要将winrar的目录添加到环境变量``path``中，并进行测试

    $ winrar

可以运行winrar程序

安装cryptography

    $ pip install cryptography
	

## 使用方法

参数``command``和``path in file``用于自动安装
    
如果传输的是压缩包，服务器会自动识别安装包并解压，但是需要给定``path in file``，为可执行文件在压缩包中位置

另外允许用户指定安装命令，在``command``中输入安装参数。
比如``command``设置为 ``-s``
在客户端会自动执行

    $ path/to/exe -s
