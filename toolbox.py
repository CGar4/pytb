import urllib.request
import json
import os
#####################icons####################
def icon():
	print("\t\t   ___________________ ")
	print("\t\t /_____________________\ ")
	print("\t\t|           |           |")
	print("\t\t|_______________________| ")
###################menu######################
def menu():
	clear()
	print('\t\t*********ToolBoxPy*********')
	icon()
	menu = "\n1.) local net scan \n2.) Geoloc \n3.) Brute force \n4.) Target scan \n5.) Quit"
	print (menu)
	usr = input('\nChoose tool: ')
	usri = str(usr)
	if usri == '1':
		scan()
	if usri == '2':
		Geoloc()

def clear():
	os.system('clear')

def restart():
	menu()
###################scan#####################
def scan():
	clear()
	t = 0
	n =0
	x = 1
	ups = 0
	uplist = []
	downs = 0
	#################### Ping code ####################
	print('\n***********Netpy*********')
	usrin = input('\nEnter IP address (with subnet): ')
	usrin1 = input('\tEnter scan block: ')
	usrint = int(usrin1)
	inlen = len(usrin)
	spl = usrin.split('.')
	s1 = spl[0]
	s2 = spl[1]
	s3 = spl[2]
	s4 = spl[3]
	spl2 = s4.split('/')
	s5 = spl2[0]
	if spl2[1] == '24':
		print('Scanning...')
		while x <= usrint:
			full = s1 + '.' + s2 +'.'+s3+'.'+s5
			response = os.system("ping -c 1 -W .1 -q >/dev/null "+ full )
			x +=1
			y = str(x)
			s5 = y
			t +=1
			n +=1
			t1 = str(t)
			if n == 10 :
				print("Scanning...")
				n = 0
			if response == 0:
				uplist.append(full)
				ups +=1
				ups1 = str(ups)
			else:
				downs +=1
	downs1 = str(downs)
	print('\nScan Complete!!')
	if ups >= 1:
		this = uplist
		print('Hosts up:')
		print('\n'.join(this))
		print('Total hosts up: ', ups1)
	else:
		print('No hosts found :(')
	print('\nHosts down: '+ downs1)
	print('Time: Around '+ t1 +" seconds")
	restart()
####################GeoLoc########################
def Geoloc():
	clear()
	print('***********Geoloc************')
	ip = input("\nEnter public ip: ")
	if ip == 'quit':
		print("\n\t\t#####Goodbye#####")
	else:
		#########DB-ip.com#########
		DBapi = "http://api.db-ip.com/v2/fd3eecc6e834dfece9ee6a9c60b26722df567bd8/"+ip
		res = urllib.request.urlopen(DBapi)
		resb = res.read()
		j = json.loads(resb.decode("utf-8"))
		db1 = "\nipAddress: ", j['ipAddress']
		db3 = "countryName: ",j['countryName']
		db4 = "stateProv: ",j['stateProv']

		########ipinfo.io########
		ipinfoapi = "http://ipinfo.io/"+ip+"/json?token=4497151532cd90"
		res2 = urllib.request.urlopen(ipinfoapi)
		resb2 = res2.read()
		j2 = json.loads(resb2.decode("utf-8"))
		ipin5 = "city: ",j2['city']

		######DB output#####
		print(*db1, sep='')##ip
		if 'hostname' in j2:
			ipin1 = "Hostname: ", j2['hostname']
			print(*ipin1, sep='')##host
		if 'org' in j2:
			ipin3 = "Orginization: ", j2['org']
			print(*ipin3, sep='')##org
		if 'continentName' in j:
			db2 = "continentName: ", j['continentName']
			print(*db2, sep='')
		print(*db3, sep='')
		print(*db4, sep='')
		print(*ipin5, sep='')
		if 'postal' in j2:
			ipin4 = "Postal: ", j2['postal']
			print(*ipin4, sep='')
		if 'loc' in j2:
			ipin2 = "Coordinates: ",j2['loc']
			print(*ipin2, sep='')
		restart()

############# End od Geoloc ###########
menu()
