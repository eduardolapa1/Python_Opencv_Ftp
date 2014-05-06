from ftplib import *
def transfer_ftp(url,user,passwd,filename,filepath):
 STOR = 'STOR ' + filename
 ftp = FTP(url,user,passwd) 
 ftp.set_pasv(True) 
 ftp.storbinary(STOR,open(filepath,'r'))
 ftp.quit() #termina a conexao

