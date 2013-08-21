#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#   reader.py (test version 0.8.0.9)
#  
#  Copyright 2013 Wolf Halton <wolf@sourcefreedom.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
import csv
import errno
import time 
import sqlite3 as lite
import sys
import os

con = None
'''                *** Help File ***\n
	Choices 1 through 5 produce csv files broken down into the "Title 
	Block" with the details of the test, requester, date of test, 
	business unit and so on; and the content of the individual 
	vulnerabilities, differentiated by OS - specifically Linux, Windows 
	and Other.  There is also an "ALL OS" choice, which is likely to be 
	the one you want to use to load the database, where you might want 
	counts and specifics by various operating system platforms.\n
	The next three choices, 6 through 8 are related to the database.  
	If you want to run the system by hand, you can type the platform 
	number and then "7" to load the title block to a database table, 
	then your choice of platform and "8" to run all modules.  Choosing 
	"9" runs the modules in #8 inside a callable module called "process"
	as in "import from csv-edit process".
	\n
	The TODO list is to create a GUI interface..
	'''
	

def main():
	#--start constants--
	__version__ = "0.8.0.8"
	#--end constants--
	
	choice = "chew"
	
	filename=raw_input("enter the filename==>  ")
	outFileT = ''
	outFileL = '' 
	outFileC = ''
	outFileQ = ''
	outFileM = ''
	outFileE = ''
	current_db = filename[:-4]+'.db' 
	outdir = filename[:-4]
	ensure_dir(outdir)

	while choice != "swallow":
		os_choice = "100099"
		while os_choice != "99" :

			print('\nEnter   "1"  for Linux')
			print('        "2"  for Windows')
			print('        "3"  for all other platforms')
			print('        "4"  for all platforms')
			print('        "5"  for all QIDs (builds a better database load)')
			print('      ******************************')
			print('        "6"  Check SQLite3 version')
			print('        "7"  Load Titleblock to DB from csv File')
			print('        "8"  Load Content to DB from csv File')
			print('        "9"  Fully automates function for #8')
			print('      ******************************')
			print('       "88"  Display Help File')
			print('       "99"  to exit the script')
				
			os_choice = raw_input('      \n     =>  ')
			qu = ""
			if os_choice == "1":
				qu = "lin"
				(filename, outdir, outFileT) = titleblock(filename, outdir,  outFileT)
				(filename, outdir,  outFileL) = labels(filename,  outdir, outFileL)
				(filename,  outdir, qu, outFileC) = content(filename,  outdir, qu, outFileC)
			elif os_choice == "2":
				qu = "win"
				(filename, outdir,  outFileT) = titleblock(filename, outdir, outFileT)
				(filename,  outdir, outFileL) = labels(filename, outdir, outFileL)
				(filename,  outdir, qu, outFileC) = content(filename, outdir, qu, outFileC)
			elif os_choice == "3":
				qu = "other"
				(filename,  outdir, outFileT) = titleblock(filename,  outdir, outFileT)
				(filename,  outdir, outFileL) = labels(filename, outdir, outFileL)
				(filename,  outdir, qu, outFileC) = content(filename,  outdir, qu, outFileC)
			elif os_choice == "4":
				qu = "all"
				(filename,  outdir, outFileT) = titleblock(filename,  outdir, outFileT)
				(filename,  outdir, outFileL) = labels(filename,  outdir, outFileL)
				(filename,  outdir, qu, outFileC) = content(filename,  outdir, qu, outFileC)
			elif os_choice == "5":
				qu = "all"
				(filename,  outdir, outFileT) = titleblock(filename,  outdir, outFileT)
				(filename,  outdir, qu, outFileQ) = qidling(filename,  outdir, qu, outFileQ)
				(filename,  outdir, qu, outFileM) = mhost(filename,  outdir, qu, outFileM)
				(filename,  outdir, qu, outFileE) = event(filename,  outdir, qu, outFileE)
				(filename,  outdir, outFileL) = labels(filename,  outdir, outFileL)
				(filename,  outdir, qu, outFileC) = content(filename,  outdir, qu, outFileC)
			elif os_choice == "6":
				lite_ver = litever(outdir, current_db)
			elif os_choice == "7":
				print(filename, outdir,  current_db)
				load_titles(filename, outdir,  current_db)
			elif os_choice == "8":
				qu = "all"
				(filename, outdir,  outFileT) = titleblock(filename, outdir, outFileT)
				(filename, outdir,  outFileL) = labels(filename, outdir, outFileL)
				(filename, outdir,  qu, outFileC) = content(filename, outdir, qu, outFileC)
				(filename, outdir, qu, outFileQ) = qidling(filename, outdir, qu, outFileQ)
				(filename, outdir, qu, outFileM) = mhost(filename, outdir, qu, outFileM)
				(filename, outdir, qu, outFileE) = event(filename, outdir,  qu, outFileE)
				load_titles(filename, outdir, current_db)
				load_content(outFileC, outdir, current_db)
				load_qid(outFileQ, outdir, current_db)
				load_mhost(outFileM, outdir, qu, current_db)
				load_events(outFileE, outdir, current_db)
			elif os_choice == "9":
				process(filename, outdir, qu, outFileT, outFileL, outFileC, outFileQ, outFileM, outFileE, current_db)
			elif os_choice == "88":
				help_me()
			elif os_choice == "99":
				break
			else: continue
			print("\n Input File                 = %s,\n Current Platform           = %s,\n Output Title File          = %s\n Output Label File          = %s,\n Output Content File        = %s,\n Output QID File            = %s,\n Output Machine(Host) File  = %s,\n Output Event File          = %s" % (filename, qu, outFileT, outFileL, outFileC, outFileQ, outFileM, outFileE))

		run_away = raw_input("if you would like to run with a different source-file, type 'y'\nIf you would like to run away, type 'r' :=>  ")
		if run_away == 'y':
			filename=raw_input("enter the filename==>  ")
		elif run_away == 'r':
			print("Thanks for using the csv-edit scripts.")
			time.sleep(2)
			choice = "swallow"
		else:
			print("Either 'y' or 'r' please")
			
	return 0

#make an output directory
def ensure_dir(f):
	d = os.path.dirname(f)
	try:
		os.makedirs(f)
	except OSError as exception:
		if exception.errno != errno.EEXIST:
			raise
			
	return 0

def titleblock(filename,  outdir, outFileT):
	with open(outdir+'/titleblock_'+filename, 'wb') as title:
		outFileT = 'titleblock_'+filename
		writer = csv.writer(title) 
		with open(filename, 'rb') as mycsv:
			reader = csv.reader(mycsv)
			counter = 0
			for counter,row in enumerate(reader):
				if counter < 1: continue
				if counter > 6: break
				writer.writerow(row)
	return (filename,  outdir, outFileT)

def labels(filename, outdir,  outFileL):
	with open(outdir+'/labels_'+filename, 'wb') as labels:
		outFileL = 'labels_'+filename
		writer = csv.writer(labels)
		with open(filename, 'rb') as mycsv:
			reader = csv.reader(mycsv)
			counter = 0
			for counter,row in enumerate(reader):
				if counter == 7:
					rowEdit = [row[0],row[22],row[2], row[4], row[6], row[15], row[16], row[17], row[11], row[18], row[19], row[20], row[25], row[26], row[27], row[28], row[29], row[30], row[31]]
					writer.writerow(rowEdit)
	return (filename, outdir,  outFileL)

def qidling(filename,  outdir, qu, outFileQ):
	chklist=["OS","Red Hat Enterprise Linux ES 3", "Linux 2.4-2.6 / Embedded Device / F5 Networks Big-IP", "Linux 2.4-2.6 / SonicWALL", "Linux 2.6", "Red Hat Enterprise Linux ES 4", "Red Hat Enterprise Linux Server 5.8", "Linux*"]
	wchklist=["OS", "Windows 2003 Service Pack 2", "Windows 2008 R2 Enterprise Service Pack 1", "Windows Server 2003 Service Pack 2", "Windows Server 2008 R2 Enterprise 64 bit Edition Service Pack 1","Windows"]
	ochklist=chklist+wchklist
	written = 0
	with open(outdir+'/QIDs_'+filename, 'wb') as qidly:
		outFileQ = 'QIDs_'+filename
		writer = csv.writer(qidly)
		with open(filename, 'rb') as mycsv:
			reader = csv.reader(mycsv)
			counter = 0
			for counter,row in enumerate(reader):
				if counter < 8: continue
				rowEdit = [row[6], row[18], row[19], row[20], row[21], row[22], row[23], row[25], row[26], row[27], row[28], row[29], row[31]]
				if qu == "all": 
					if  len(str(row[0])) <= 16:
						# keeps the last 2 irrelevant rows from printing to the output
						writer.writerow(rowEdit)
						written = written +1
	return (filename, outdir, qu, outFileQ)

def mhost(filename,  outdir, qu, outFileM):
	chklist=["OS","Red Hat Enterprise Linux ES 3", "Linux 2.4-2.6 / Embedded Device / F5 Networks Big-IP", "Linux 2.4-2.6 / SonicWALL", "Linux 2.6", "Red Hat Enterprise Linux ES 4", "Red Hat Enterprise Linux Server 5.8", "Linux*"]
	wchklist=["OS", "Windows 2003 Service Pack 2", "Windows 2008 R2 Enterprise Service Pack 1", "Windows Server 2003 Service Pack 2", "Windows Server 2008 R2 Enterprise 64 bit Edition Service Pack 1","Windows"]
	ochklist=chklist+wchklist
	written = 0
	with open(outdir+'/MHosts_'+filename, 'wb') as mhost:
		outFileM = 'MHosts_'+filename
		writer = csv.writer(mhost)
		with open(filename, 'rb') as mycsv:
			reader = csv.reader(mycsv)
			counter = 0
			for counter,row in enumerate(reader):
				if counter < 8: continue
				rowEdit = [row[0], row[2], row[4]]
				if qu == "all": 
					if  len(str(row[0])) <= 16:
						# keeps the last 2 irrelevant rows from printing to the output
						writer.writerow(rowEdit)
						written = written +1
	return (filename, outdir, qu, outFileM)

def event(filename,  outdir, qu, outFileE):
	chklist=["OS","Red Hat Enterprise Linux ES 3", "Linux 2.4-2.6 / Embedded Device / F5 Networks Big-IP", "Linux 2.4-2.6 / SonicWALL", "Linux 2.6", "Red Hat Enterprise Linux ES 4", "Red Hat Enterprise Linux Server 5.8", "Linux*"]
	wchklist=["OS", "Windows 2003 Service Pack 2", "Windows 2008 R2 Enterprise Service Pack 1", "Windows Server 2003 Service Pack 2", "Windows Server 2008 R2 Enterprise 64 bit Edition Service Pack 1","Windows"]
	ochklist=chklist+wchklist
	written = 0
	with open(outdir+'/Events_'+filename, 'wb') as event:
		outFileE = 'Events_'+filename
		writer = csv.writer(event)
		with open(filename, 'rb') as mycsv:
			reader = csv.reader(mycsv)
			counter = 0
			for counter,row in enumerate(reader):
				if counter < 8: continue
				rowEdit = [row[0], row[6], row[15], row[16], row[17], row[11], row[30]]
#				print(rowEdit)
				if qu == "all": 
					if  len(str(row[0])) <= 16:
						# keeps the last 2 irrelevant rows from printing to the output
						writer.writerow(rowEdit)
						written = written +1
	return (filename,  outdir, qu, outFileE)

def content(filename, outdir,  qu, outFileC):
	chklist=["OS","Red Hat Enterprise Linux ES 3", "Linux 2.4-2.6 / Embedded Device / F5 Networks Big-IP", "Linux 2.4-2.6 / SonicWALL", "Linux 2.6", "Red Hat Enterprise Linux ES 4", "Red Hat Enterprise Linux Server 5.8", "Linux*"]
	wchklist=["OS", "Windows 2003 Service Pack 2", "Windows 2008 R2 Enterprise Service Pack 1", "Windows Server 2003 Service Pack 2", "Windows Server 2008 R2 Enterprise 64 bit Edition Service Pack 1","Windows"]
	ochklist=chklist+wchklist
	written = 0
	with open(outdir+'/'+qu+'_content_'+filename, 'wb') as content:
		outFileC = qu+'_content_'+filename
		writer = csv.writer(content)
		with open(filename, 'rb') as mycsv:
			reader = csv.reader(mycsv)
			counter = 0
			for counter,row in enumerate(reader):
				if counter < 8: continue
				rowEdit = [row[0],row[22],row[2], row[4], row[6], row[15], row[16], row[17], row[11], row[18], row[19], row[20], row[25], row[26], row[27], row[28], row[29], row[30], row[31]]
				if qu == "lin":
					lisst = chklist
					if any(item in row[4] for item in lisst):
						writer.writerow(rowEdit)
						written = written +1
				elif qu == "win":
					lisst = wchklist
					if any(item in row[4] for item in lisst):
						writer.writerow(rowEdit)
						written = written + 1
				elif qu == "other": 
					lisst = ochklist
					if row[4] not in lisst:
						writer.writerow(rowEdit)
						written = written +1
				elif qu == "all": 
					if  len(str(row[0])) <= 16:
						writer.writerow(rowEdit)
						written = written +1
	return (filename, outdir, qu, outFileC)

def litever(outdir, current_db):
	try:
		con = lite.connect(outdir+'/'+current_db)
		print(current_db)
		cur = con.cursor()    
		cur.execute('SELECT SQLITE_VERSION()')
		data = cur.fetchone()
		print "SQLite version: %s" % data                

	except lite.Error, e:
		print "Error %s:" % e.args[0]
		sys.exit(1)

	finally:
		if con:
			con.close()

def load_titles(f, outdir,  d):
	filename = f
	current_db = outdir+'/'+d
	titles=[]
	with open(filename, 'rb') as mycsv:
			reader = csv.reader(mycsv)
			counter = 0
			for counter,row in enumerate(reader):
				if counter < 1: continue
				if counter > 6: break
				titles.append(row)
				 
			tests = (titles[0][0], titles[0][1], titles[0][2], titles[0][3], titles[0][4], titles[0][5], titles[0][6], titles[1][0], titles[1][1], titles[1][2], titles[4][0], titles[4][1], titles[4][2], titles[4][3], titles[4][4], titles[4][5], titles[4][6]),
			
	try:
		con = lite.connect(outdir+'/'+d)
		with con:
			cur = con.cursor()    
			cur.execute("DROP TABLE IF EXISTS test_detail")
			cur.execute("CREATE TABLE test_detail(Id INTEGER PRIMARY KEY, Corp TEXT, Address_1 TEXT, Address_2 TEXT, City TEXT, State TEXT, Country TEXT, Postal_Code TEXT, Requester TEXT, Code_1 TEXT, Role TEXT, Asset_Groups TEXT, IPs TEXT, Active_Hosts INT, Hosts_Matching_Filters INT, Trend_Analysis TEXT, Date_Range TEXT, Asset_Tags TEXT)")
			cur.executemany("INSERT INTO test_detail(Corp, Address_1, Address_2, City, State, Country, Postal_Code, Requester, Code_1, Role, Asset_Groups, IPs, Active_Hosts, Hosts_Matching_Filters, Trend_Analysis, Date_Range, Asset_Tags) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", tests)
	
	except lite.Error, e:
		if con:
			con.rollback()
		print "Error %s:" % e.args[0]
		sys.exit(1)

	finally:
		if con:
			con.close() 
#	return filename,  outdir, current_db

def load_content(f, outdir, d):
	filename = f
	current_db = outdir+'/'+d
	with open(outdir+'/'+filename, 'rb') as mycsv:
		con = lite.connect(outdir+'/'+d)
		cur = con.cursor() 
		cur.execute("PRAGMA foreign_keys = ON")
		cur = con.commit()
		reader = csv.reader(mycsv)
		counter = 0
		counter2 = 0
#		cur.execute("DROP TABLE IF EXISTS vulnerabilities")
		for counter,row in enumerate(reader):

			vuln = (row[0],row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18])

			try:
				con = lite.connect(outdir+'/'+d)

				with con:
					cur = con.cursor()    
#					cur.execute("DROP TABLE IF EXISTS vulnerabilities")
					cur.execute("CREATE TABLE IF NOT EXISTS vulnerabilities(Id INTEGER PRIMARY KEY, IP TEXT, CVSS_Base INT, NetBIOS TEXT, OS TEXT,  QID INT, First_Detected DATE, Last_Detected DATE, Times_Detected INT, Port TEXT, CVE_ID TEXT, Vendor_Reference TEXT, Bug_traq_ID TEXT, Threat TEXT, Impacts TEXT, Solution TEXT, Exploitability TEXT, Associated_Malware TEXT, Results TEXT, PCI_Vuln TEXT)")
					cur.execute("INSERT INTO vulnerabilities(IP, CVSS_Base, NetBIOS, OS, QID, First_Detected, Last_Detected, Times_Detected, Port, CVE_ID, Vendor_Reference, Bug_traq_ID, Threat, Impacts, Solution, Exploitability, Associated_Malware, Results, PCI_Vuln) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", vuln)
					con.commit()
					counter2 = counter2 + 1
					
			except lite.Error, e:
				if con:
					con.rollback()
					print "Error %s:" % e.args[0]
					sys.exit(1)

			finally:
				if con:
					con.close() 

	outFileC = filename
#	return outFileC, outdir, current_db
	
def load_qid(f, outdir,  d):
	filename = f
	current_db = outdir+'/'+d
	with open(outdir+'/'+filename, 'rb') as mycsv:
		con = lite.connect(outdir+'/'+d)
		cur = con.cursor() 
		cur = con.commit()
		reader = csv.reader(mycsv)
		counter = 0
		counter2 = 0
		for counter,row in enumerate(reader):
#			print(row)
			quidly = (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12])
			
			try:
				con = lite.connect(outdir+'/'+d)
				
				with con:
					cur = con.cursor()    

#					cur.execute("DROP TABLE IF EXISTS qid_def")
					cur.execute("CREATE TABLE IF NOT EXISTS qid_def (Id INTEGER PRIMARY KEY, QID INT, CVE_ID TEXT, Vendor_Reference TEXT, Bug_traq_ID INT, CVSS INT, CVSS_Base INT, CVSS_Temporal INT, Threat TEXT, Impact TEXT, Solution TEXT, Exploitability TEXT, Associated_Malware TEXT, PCI_Vuln TEXT)")
					cur.execute("INSERT INTO qid_def(QID, CVE_ID, Vendor_Reference, Bug_traq_ID, CVSS, CVSS_Base, CVSS_Temporal, Threat, Impact, Solution, Exploitability, Associated_Malware, PCI_Vuln) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", quidly)
					con.commit()
					counter2 = counter2 + 1
					
			except lite.Error, e:
				if con:
					con.rollback()
					print "Error %s:" % e.args[0]
					sys.exit(1)

			finally:
				if con:
					con.close() 

	outFileQ = filename
#	return outFileQ, outdir, current_db

def load_mhost(filename,  outdir, qu, outFileM):
	d=outFileM
	current_db = outdir+'/'+d
	with open(outdir+'/'+filename, 'rb') as mycsv:
		con = lite.connect(outdir+'/'+d)
		cur = con.cursor() 
		cur = con.commit()
		reader = csv.reader(mycsv)
		counter = 0
		counter2 = 0
		for counter,row in enumerate(reader):
			host = (row[0], row[1], row[2])

			try:
				con = lite.connect(outdir+'/'+d)

				with con:
					cur = con.cursor()    

					cur.execute("CREATE TABLE IF NOT EXISTS mhosts(Id INTEGER PRIMARY KEY, IP TEXT, NetBIOS TEXT, OS TEXT)")
					cur.execute("INSERT INTO mhosts(IP, NetBIOS, OS) VALUES(?, ?, ?)", host)
					con.commit()
					counter2 = counter2 + 1
					
			except lite.Error, e:
				if con:
					con.rollback()
					print "Error %s:" % e.args[0]
					sys.exit(1)

			finally:
				if con:
					con.close() 
	outFileM = filename
	return outFileM, outdir, qu, current_db

def load_events(f, outdir, d):
	filename = f
	current_db = outdir+'/'+d
	with open(outdir+'/'+filename, 'rb') as mycsv:
		con = lite.connect(outdir+'/'+d)
		cur = con.cursor() 
		cur = con.commit()
		reader = csv.reader(mycsv)
		counter = 0
		counter2 = 0
		for counter,row in enumerate(reader):
			print("LOAD_EVENTS \nIP, QID, First_Detected, Last_Detected, Times_Detected, Port, Results\n",row)
			events2 = (row[0], row[1], row[2], row[3], row[4], row[5], row[6])
			
			try:
				con = lite.connect(outdir+'/'+d)
				
				with con:
					cur = con.cursor()    

#					cur.execute("DROP TABLE IF EXISTS events")
					cur.execute("CREATE TABLE IF NOT EXISTS events(Id INTEGER PRIMARY KEY, IP TEXT, QID INT, First_Detected DATE, Last_Detected DATE, Times_Detected INT, Port TEXT, Results TEXT)")
					cur.execute("INSERT INTO vulnerabilities(IP, QID, First_Detected, Last_Detected, Times_Detected, Port, Results) VALUES (?, ?, ?, ?, ?, ?, ?)", events2)
					con.commit()
					counter2 = counter2 + 1

			except lite.Error, e:
				if con:
					con.rollback()
					print "Error %s:" % e.args[0]
					sys.exit(1)

			finally:
				if con:
					con.close() 

	outFileE = filename
#	return outFileE, outdir, current_db

def process(filename, outdir, qu, outFileT, outFileL, outFileC, outFileQ, outFileM, outFileE, current_db):
	qu = "all"
	(filename, outdir,  outFileT) = titleblock(filename, outdir,  outFileT)
	(filename, outdir,  outFileL) = labels(filename, outdir,  outFileL)
	(filename, outdir,  qu, outFileC) = content(filename, outdir,  qu, outFileC)
	(filename, outdir, qu, outFileQ) = qidling(filename, outdir,  qu, outFileQ)
	(filename, outdir,  qu, outFileM) = mhost(filename, outdir, qu, outFileM)
	(filename, outdir,  qu, outFileE) = event(filename, outdir,  qu, outFileE)
	load_titles(filename, outdir, 
	 current_db)
	load_content(outFileC, outdir,  current_db)
	load_qid(outFileQ, outdir,  current_db)
	load_mhost(outFileM, outdir, qu, current_db)
	load_events(outFileE, outdir,  current_db)

	return(filename, qu, outFileT, outFileL, outFileC, outFileQ, outFileM, outFileE, current_db)

def help_me():
	print('''                *** Help File ***\n
	Choices 1 through 5 produce csv files broken down into the "Title 
	Block" with the details of the test, requester, date of test, 
	business unit and so on; and the content of the individual 
	vulnerabilities, differentiated by OS - specifically Linux, Windows 
	and Other.  There is also an "ALL OS" choice, which is likely to be 
	the one you want to use to load the database, where you might want 
	counts and specifics by various operating system platforms.\n
	The next three choices, 6 through 8 are related to the database.  
	If you want to run the system by hand, you can type the platform 
	number and then "7" to load the title block to a database table, 
	then your choice of platform and "8" to run all modules.  Choosing 
	"9" runs the modules in #8 inside a callable module called "process"
	as in "import from csv-edit process".  
	\n
	The TODO list is to create a GUI interface...\n''')

if __name__ == '__main__':
	main()
