import paramiko


RSA_key_path = 'D:/si/private.key'
pkey = paramiko.RSAKey.from_private_key_file(RSA_key_path)
transport = paramiko.Transport(('localhost', 1996))
transport.connect(username='admin', password='admin', pkey=pkey)
sftp = paramiko.SFTPClient.from_transport(transport)
sftp.mkdir('tmp')
sftp.chdir('tmp')
sftp.put('')