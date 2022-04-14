from email.charset import BASE64
import os
import re

class pyllutu:

	YTBASE: str = "youtube-dl "
	URL: str = ""
	TEMPLATE = "%(title)s"
	WRITE_THUMBNAIL: bool = False
	SKIP_DOWNLOAD: bool = False
	LOCATION = "./"

	def setWriteThumbnail(self, stt: bool) -> None:
		if type(stt) is bool:
			self.WRITE_THUMBNAIL = stt;
		else:
			self.printNonFatalError("setWriteThumbnail")
		return None
	
	def setSkipDownload(self, stt: bool) -> None:
		if type(stt) is bool:
			self.SKIP_DOWNLOAD = stt;
		else:
			self.printNonFatalError("setSkipDownload")
		return None
	
	def setURL(self, url: str) -> None:
		if type(url) is str:
			self.URL = url
		elif url == "":
			print("Non Fatal Error: Empty string, ignored.")
		else:
			self.printNonFatalError("setURL")
		return None
	
	def setName(self, template: str) -> None:
		if type(template) is str:
			self.TEMPLATE = str.lower(re.sub(r'\W+', '', template.replace(" ","_")))
		else:
			self.printNonFatalError("printNonFatalError")
		return self.TEMPLATE

	def setPath(self, path: str) -> None:
		if type(path) is str:
			self.LOCATION = path
		else:
			self.printNonFatalError("printNonFatalError")
		return None
	
	def printNonFatalError(self, functionName: str) -> None:
		if type(functionName) is str:
			print("Non Fatal Error: invalid type passed to " + functionName + "(), ignored.")
		else:
			self.printNonFatalError("printNonFatalError")
		return None
	
	def buildCommand(self) -> str:
		temp: str = ""
		temp = temp + self.YTBASE
		
		if self.WRITE_THUMBNAIL:
			temp = temp + "--write-thumbnail --embed-thumbnail "
		
		if self.SKIP_DOWNLOAD:
			temp = temp + "--skip-download "
		
		temp = temp + "--output " + self.LOCATION + self.TEMPLATE + ".%(ext)s "

		if self.URL != "":
			temp = temp + self.URL
		else:
			print("Warning: Empty URL!")
			return ""
		return temp
	
	def runCommand(self) -> None:
		cmd: str = self.buildCommand()
		output:str = os.popen(cmd).read()
		filename:str = output.split("\n")[-2].split("Writing thumbnail to: ")[-1].split("\\")[-1]
		return filename

