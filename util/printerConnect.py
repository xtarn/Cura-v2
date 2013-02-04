from ftplib import FTP

class printerConnect(object):
	def __init__(self):
		self.ftp = FTP('130.102.87.49')
		# self.filepath = filename[:filename.rfind('/')+1]
		# self.filename = filename[filename.rfind('/')+1:filename.rfind('.stl')]
	
	def connect(self):
		return self.ftp.login()

	def getQueue(self):
		self.ftp.retrbinary("RETR queue.txt", open('queue.txt', 'w').write)
		queue = open('queue.txt', 'r').readlines()
		return queue

	def sendJob(self, filename, uid):
		name = filename[filename.rfind('/')+1:-4]
		self.ftp.storbinary("STOR Jobs/" + name + "." + uid + ".gcode", open(filename[:-4]+".gcode"))

	def sendJobInfo(self, filename, uid):
		name = filename[filename.rfind('/')+1:-4]
		self.ftp.storbinary("STOR JobInfo/" + name + "." + uid + ".info", open(filename[:-4]+".info"))

	def closeConnection(self):
		self.ftp.quit()

		

		
		
		
