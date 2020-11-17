import ftplib
host = 'localhost'
port = 8080
ftp = ftplib.FTP()
ftp.connect(host,port)
ftp.login('SE','123')
uploadfile= open('C:\\Users\\alexi\\Server\\upload.html', 'upload.html')

ftp.storlines('STOR ' + filename, uploadfile)
