import ConfigParser

class Conf():
	SERVER_ADDRESS = "server_address" 
	SERVER_ADDRESS = "server_port"
	ICAP = "icap"
	SMTP = "smtp"
	MAIN = "main"
	LOG = "log"
	conf = None

	def __init__(self, config):
		self.conf = config
	
	def get(self, section, option):
		if self.conf.has_option(section, option):
			return self.conf.get(section, option)
		else:
			return None

	def getSmtp(self, option):
		return self.conf.get(self.SMTP, option)

	def getIcap(self, option):
		return self.conf.get(self.ICAP, option)

	def getLog(self):
		return self.conf.get(self.MAIN, self.LOG)

	def getSmtpPair():
		return (self.getSmtp(self.SERVER_ADDRESS), self.getSmtp(self.SERVER_PORT))

	def getIcapPair():
		return (self.getIcap(self.SERVER_ADDRESS), self.getIcap(self.SERVER_PORT))
