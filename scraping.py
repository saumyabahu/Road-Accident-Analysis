import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtWebKit import *
from lxml import html
from bs4 import BeautifulSoup 
import csv 

class Render(QWebPage):  
	def __init__(self, url):  
		self.app = QApplication(sys.argv)  
		QWebPage.__init__(self)  
		self.loadFinished.connect(self._loadFinished)  
		self.mainFrame().load(QUrl(url))  
		self.app.exec_()  
  
	def _loadFinished(self, result):  
		self.frame = self.mainFrame()  
		self.app.quit()

url =  
r = Render(url)  
result = r.frame.toHtml()
formatted_result = str(result.toAscii())

soup = BeautifulSoup(formatted_result)
a=[]


table = soup.find('tbody')  
for row in table.findAll('tr'):
    u = row.td.text.encode("utf-8") 
    a.append(u)

print(a);