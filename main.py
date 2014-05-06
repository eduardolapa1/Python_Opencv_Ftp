import cv
import datetime
import time
import utils
import zipfile
import ConfigParser
import os
imgSave = 0
config = ConfigParser.ConfigParser()
config.read('teste.cfg')
time_sec  = config.getint('tempo','an_int')
count_img = config.getint('file','an_int')
if config.has_section('ftp'):
	ftp_url = config.get('ftp','url')
	ftp_user = config.get('ftp','user')
	ftp_passwd = config.get('ftp','passwd')
while True:
	today = datetime.datetime.now()
	filename = config.get('file','path')+str(today.day) + str(today.month) + str(today.year)+str(today.hour) + str(today.minute)+str(today.second)+'.jpg'
	camera = cv.CaptureFromCAM(0) #inicia captura no dispositivo padrao
	im = cv.QueryFrame(camera) #captura frame de dispostivo
	if imgSave == 0:
		zippath = config.get('file','path') + str(today.day) + str(today.month) + str(today.year)+str(today.hour) + str(today.minute)+str(today.second)+'.zip'
		zipfilename = str(today.day) + str(today.month) + str(today.year)+str(today.hour) + str(today.minute)+str(today.second)+'.zip'
		zf = zipfile.ZipFile(zippath,mode = 'w')
	
	cv.SaveImage(filename,im) #grava frame
	zf.write(filename)
	os.remove(filename)
	
	imgSave=imgSave+1
	del(camera) #desativa a captura
	
	if imgSave == count_img:
		print '%s' % zippath
		utils.transfer_ftp(ftp_url,ftp_user,ftp_passwd,zipfilename,zippath)
		zf.close()
		imgSave = 0
		
	time.sleep(time_sec)
	

