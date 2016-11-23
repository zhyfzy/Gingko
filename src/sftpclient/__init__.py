import paramiko

RSA_key_path = 'D:/tmp/private.key'
remote_path = 'cloudmusic.exe'
local_path = 'cloudmusic.exe'

def main():
    pkey = paramiko.RSAKey.from_private_key_file(RSA_key_path)
    with paramiko.Transport(('localhost', 1996)) as transport:
        transport.connect(username='admin', password='admin', pkey=pkey)
        sftp = paramiko.SFTPClient.from_transport(transport)
        sftp.put(local_path,remote_path,selfinstall=True)

if __name__ == '__main__':
    main()
