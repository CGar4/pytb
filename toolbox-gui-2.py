from PyQt5.Qt import *
from PyQt5.QtWebEngineWidgets import *
import sys
import urllib.request
import json
import os
import googlemaps
class ToolBox(QMainWindow):
	def __init__(self):
		QDialog.__init__(self)
		##### Window Geometry #####
		self.left = 0
		self.top = 0
		self.width = 1100
		self.hight = 900
		self.setGeometry(self.left, self.top, self.width, self.hight)
		#self.tab2UI()
		#self.tab3UI()
		self.setWindowTitle("PYToolBox")
		self.table_widget = MyTableWidget(self)
		self.setCentralWidget(self.table_widget)
class MyTableWidget(QWidget):
	def __init__(self, parent):
		super(QWidget, self).__init__(parent)
		self.layout = QGridLayout(self)
		##### Initialize tab screen #####
		self.tabs = QTabWidget()
		self.tab1 = QWidget()
		self.tab2 = QWidget()
		self.tabs.resize(600,500)
		##### Add tabs #####
		self.tabs.addTab(self.tab1,"GeoPy")
		self.tabs.addTab(self.tab2,"Tab 2")
		##### Geoloc tab #####
		self.tab1.layout = QGridLayout(self)
		self.map = QWebEngineView()
		#self.map.setUrl(QUrl("https://maps.tilehosting.com/c/60127d7e-52c2-4b6c-9c9a-6934e197dfb0/styles/streets/?key=LUzQrA8HElXvZxe6AKz5#14.02/29.75868/-95.3657/25.6/60"))
		self.map.setUrl(QUrl("file:///home/los/pytb/mtilermap.html"))
		self.geotitle = QLabel('***** GeoPy *****')
		self.geotitle.setAlignment(Qt.AlignHCenter)
		self.results1label = QLabel('Results:')
		self.results1label.setAlignment(Qt.AlignTop)
		self.results1label.setAlignment(Qt.AlignRight)
		self.inputlabel = QLabel('IP Address:')
		self.closebutton = QPushButton('Close')
		self.enterbutton = QPushButton('Submit')
		self.results = QTextEdit()
		self.usrin = QLineEdit()
		##### Layout #####
		self.tab1.setLayout(self.tab1.layout)
		self.tab1.layout.addWidget(self.geotitle, 1, 1)
		self.tab1.layout.addWidget(self.inputlabel, 6, 0)
		self.tab1.layout.addWidget(self.usrin, 6, 1)
		self.tab1.layout.addWidget(self.enterbutton, 6, 2)
		self.tab1.layout.addWidget(self.map, 2, 0, 2, 3)
		self.tab1.layout.addWidget(self.results1label, 4, 0)
		self.tab1.layout.addWidget(self.results, 4, 1)
		##### NetPy tab #####
		##### Events #####
		self.enterbutton.clicked.connect(self.erchk)
		# Add tabs to widget
		self.layout.addWidget(self.tabs)
		self.setLayout(self.layout)
	def erchk(self):
		if self.usrin.text() == '':
			self.results.setText('no input')
		else:
			self.Geoloc()
	def Geoloc(self):
		##### DB-ip.com #####
		ip = self.usrin.text()
		readfile = open('results.txt').read()
		DBapi = "http://api.db-ip.com/v2/fd3eecc6e834dfece9ee6a9c60b26722df567bd8/"+ip
		res = urllib.request.urlopen(DBapi)
		resb = res.read()
		j = json.loads(resb.decode("utf-8"))
		db1 = "\nipAddress: ", j['ipAddress']
		db3 = "countryName: ",j['countryName']
		db4 = "stateProv: ",j['stateProv']
		##### ipinfo.io #####
		ipinfoapi = "http://ipinfo.io/"+ip
		res2 = urllib.request.urlopen(ipinfoapi)
		resb2 = res2.read()
		j2 = json.loads(resb2.decode("utf-8"))
		cords = j2['loc']
		spl2 = cords.split(',')
		loc0 = spl2[0]+"/"+spl2[1]
		ipin5 = "city: ",j2['city']
		##### Write to File #####
		print(*db1, sep='', file=open('results.txt', 'w'))##ip
		if 'hostname' in j2:
			ipin1 = "Hostname: ", j2['hostname']
			print(*ipin1, sep='', file=open('results.txt', 'a'))##host
		if 'org' in j2:
			ipin3 = "Orginization: ", j2['org']
			print(*ipin3, sep='', file=open('results.txt', 'a'))##org
		if 'continentName' in j:
			db2 = "continentName: ", j['continentName']
			print(*db2, sep='', file=open('results.txt', 'a'))
		print(*db3, sep='', file=open('results.txt', 'a'))
		print(*db4, sep='', file=open('results.txt', 'a'))
		print(*ipin5, sep='', file=open('results.txt', 'a'))
		if 'postal' in j2:
			ipin4 = "Postal: ", j2['postal']
			print(*ipin4, sep='', file=open('results.txt', 'a'))
		if 'loc' in j2:#self.layout.addWidget(results, 2, 1, 2, 5)
			ipin2 = "Coordinates: ",j2['loc']
			print(*ipin2, sep='', file=open('results.txt', 'a'))
		##### Display Results #####
		self.results.setText(readfile)
		#self.map.setUrl(QUrl("https://maps.tilehosting.com/c/60127d7e-52c2-4b6c-9c9a-6934e197dfb0/styles/darkmatter/?key=LUzQrA8HElXvZxe6AKz5#1/"+loc0))
		##### Clear usrin #####
		self.usrin.setText('')
	@pyqtSlot()
	def on_click(self):
		print("\n")
		for currentQTableWidgetItem in self.tableWidget.selectedItems():
			print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())
##### Qt call #####
def start():
	app = QApplication(sys.argv)
	ex = ToolBox()
	ex.show()
	app.exec_()
start()
