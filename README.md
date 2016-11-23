# Gingko

A batch processing self-install tool 
一个通过SFTP传输文件并在目标机中执行自动安装的工具
使用Python2.7实现

## 安装依赖包

使用前需要将winrar的目录添加到环境变量``path``中
并进行测试

    $ winrar

可以运行winrar程序

安装cryptography

    $ pip install cryptography
	
在[这里](https://nmap.org/download.html)下载windows版本的nmap，以及在[这里](https://riverbankcomputing.com/software/pyqt/download)下载PyQt（选择python2.7版本），并执行安装

## 使用方法

使用以下指令上传文件到SFTP Server
    
    >>> paramiko.SFTPClient.put(local_path, remote_path, selfinstall=True, Command='Your command', pathinfile='your path in file')

其中参数``command``和``pathinfile``用于自动安装

如果无需自动安装，将``selfinstall``设置成False
    
如果传输的是压缩包，服务器会自动识别安装包并解压，但是需要给定``pathinfile``，为可执行文件在压缩包中内容

另外允许用户指定安装命令，在``command``中输入安装参数。
比如``command``设置为 ``-s``
在客户端会自动执行

    $ path/to/exe -s
