#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#   test0904.py
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
import time 
import sqlite3 as lite
import sys
import os

con = None


def main():
	choice = "chew"
	
	filename=raw_input("enter the filename==>  ")
	outFileT = ''
	outFileL = '' 
	outFileC = ''
	current_db = filename[:-4]+'.db' 

	while choice != "swallow":
		os_choice = "100099"
		while os_choice != "99" :

			print('\nEnter   "1"  for Linux')
			print('        "2"  for Windows')
			print('        "3"  for all other platforms')
			print('        "4"  for all platforms')
			print('      ******************************')
			print('        "5"  Check SQLite3 version')
			#print('        "6"  Load Titleblock to DB from csv File')
			print('        "7"  Load Content to DB from csv File')
			print('        "8"  Fully automates function for #7')
			print('      ******************************')
			print('       "88"  Display Help File')
			print('       "99"  to exit the script')
				
			os_choice = raw_input('      \n     =>  ')
			qu = ""
			if os_choice == "1":
				qu = "lin"
				(filename, outFileT) = titleblock(filename, outFileT)
				(filename, outFileL) = labels(filename, outFileL)
				(filename, qu, outFileC) = content(filename, qu, outFileC)
			elif os_choice == "2":
				qu = "win"
				(filename, outFileT) = titleblock(filename, outFileT)
				(filename, outFileL) = labels(filename, outFileL)
				(filename, qu, outFileC) = content(filename, qu, outFileC)
			elif os_choice == "3":
				qu = "other"
				(filename, outFileT) = titleblock(filename, outFileT)
				(filename, outFileL) = labels(filename, outFileL)
				(filename, qu, outFileC) = content(filename, qu, outFileC)
			elif os_choice == "4":
				qu = "all"
				(filename, outFileT) = titleblock(filename, outFileT)
				(filename, outFileL) = labels(filename, outFileL)
				(filename, qu, outFileC) = content(filename, qu, outFileC)
			elif os_choice == "5":
				lite_ver = litever(current_db)
			elif os_choice == "6":
				print(filename, current_db)
				load_titles(filename, current_db)
			elif os_choice == "7":
				qu = "all"
				(filename, outFileT) = titleblock(filename, outFileT)
				(filename, outFileL) = labels(filename, outFileL)
				(filename, qu, outFileC) = content(filename, qu, outFileC)
				load_titles(filename, current_db)
				load_content(outFileC, current_db)
			elif os_choice == "8":
				process(filename, qu, outFileT, outFileL, outFileC, current_db)
			elif os_choice == "88":
				help_me()
			elif os_choice == "99":
				break
			else: continue
			print(" Input File          = %s,\n Current Platform    = %s,\n Output Title File   = %s\n Output Label File   = %s,\n Output Content File = %s" % (filename, qu, outFileT, outFileL, outFileC))
		run_away = raw_input("if you would like to run with a different source-file, type 'y'\nIf you would like to run away, type 'r' :=>  ")
		if run_away == 'y':
			filename=raw_input("enter the filename==>  ")
		elif run_away == 'r':
			print("Thanks for using the csv-edit scripts.")
			time.sleep(7)
			choice = "swallow"
		else:
			print("Either 'y' or 'r' please")
			
	return 0

def titleblock(filename, outFileT):
	with open('titleblock_'+filename, 'wb') as title:
		outFileT = 'titleblock_'+filename
		writer = csv.writer(title) 
		with open(filename, 'rb') as mycsv:
			reader = csv.reader(mycsv)
			counter = 0
			for counter,row in enumerate(reader):
				if counter < 1: continue
				if counter > 6: break
				writer.writerow(row)
	return (filename, outFileT)

def labels(filename, outFileL):
	with open('labels_'+filename, 'wb') as labels:
		outFileL = 'labels_'+filename
		writer = csv.writer(labels)
		with open(filename, 'rb') as mycsv:
			reader = csv.reader(mycsv)
			counter = 0
			for counter,row in enumerate(reader):
				if counter == 7:
					rowEdit = [row[0],row[22],row[2], row[4], row[6], row[15], row[16], row[11], row[18], row[19], row[20], row[25], row[26], row[27], row[28], row[29], row[30], row[31]]
					writer.writerow(rowEdit)
	return (filename, outFileL)
	
def content(filename, qu, outFileC):
	chklist=["OS","Red Hat Enterprise Linux ES 3", "Linux 2.4-2.6 / Embedded Device / F5 Networks Big-IP", "Linux 2.4-2.6 / SonicWALL", "Linux 2.6", "Red Hat Enterprise Linux ES 4", "Red Hat Enterprise Linux Server 5.8", "Linux*"]
	wchklist=["OS", "Windows 2003 Service Pack 2", "Windows 2008 R2 Enterprise Service Pack 1", "Windows Server 2003 Service Pack 2", "Windows Server 2008 R2 Enterprise 64 bit Edition Service Pack 1","Windows"]
	ochklist=chklist+wchklist
	written = 0
	with open(qu+'_content_'+filename, 'wb') as content:
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
						print(written)
				elif qu == "win":
					lisst = wchklist
					if any(item in row[4] for item in lisst):
						writer.writerow(rowEdit)
						written = written + 1
						print(written)
				elif qu == "other": 
					lisst = ochklist
					if row[4] not in lisst:
						writer.writerow(rowEdit)
						written = written +1
						print(written)
				elif qu == "all": 
					if  len(str(row[0])) <= '16':
						writer.writerow(rowEdit)
						written = written +1
#						print(row[0], 'is the value of the IP field')
#				print(len(str(row[0])), ' is the length of the strings in the IP field')
#			print(written, ' is the number of lines written.')
	print(counter, " is the number of rows in the csv.")
	return (filename, qu, outFileC)

def litever(current_db):
	try:
		con = lite.connect('current_db')
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

def load_titles(f, d):
#	print("This is da 'd'-atabase name, y\'all! ", d ) 
#	print("This is da origin 'f'-ilename, y\'all! ", f )
	filename = f
	current_db = d
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
		con = lite.connect(d)
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
	return filename, current_db

def load_content(f, d):
	filename = f
	current_db = d
#	print("This is da 'd,' y\'all! ", d )
#	print("This is da 'f,' y\'all! ", f )
	with open(filename, 'rb') as mycsv:
		con = lite.connect(d)
		cur = con.cursor() 
		cur.execute("PRAGMA foreign_keys = ON")
		cur = con.commit()
		reader = csv.reader(mycsv)
		counter = 0
		counter2 = 0
		for counter,row in enumerate(reader):
#			print(row)
			vuln = (row[0],row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18])
			
			try:
				con = lite.connect(d)
				
				with con:
					cur = con.cursor()    

#					cur.execute("DROP TABLE IF EXISTS vulnerabilities")
					cur.execute("CREATE TABLE IF NOT EXISTS vulnerabilities(Id INTEGER PRIMARY KEY, IP TEXT, CVSS_Base TEXT, NetBIOS TEXT, OS TEXT,  QID TEXT, First_Detected TEXT, Last_Detected TEXT, Times_Detected INT, Port TEXT, CVE_ID TEXT, Vendor_Reference TEXT, Bug_traq_ID TEXT, Threat TEXT, Impacts TEXT, Solution TEXT, Exploitability TEXT, Associated_Malware TEXT, Results TEXT, PCI_Vuln TEXT)")
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
	return outFileC, current_db

def process(filename, qu, outFileT, outFileL, outFileC, current_db):
	qu = "all"
	(filename, outFileT) = titleblock(filename, outFileT)
	(filename, outFileL) = labels(filename, outFileL)
	(filename, qu, outFileC) = content(filename, qu, outFileC)
	load_titles(filename, current_db)
	load_content(outFileC, current_db)
	return(filename, qu, outFileT, outFileL, outFileC, current_db)

def help_me():
	print('''                *** Help File ***\n
	Choices 1 through 4 produce csv files broken down into the "Title 
	Block" with the details of the test, requester, date of test, 
	business unit and so on; and the content of the individual 
	vulnerabilities, differentiated by OS - specifically Linux, Windows 
	and Other.  There is also an "ALL OS" choice, which is likely to be 
	the one you want to use to load the database, where you might want 
	counts and specifics by various operating system platforms.
	\n
	The next three choices, 5 through 7 are related to the database.  
	If you want to run the system by hand, you can type the platform 
	number and then "6" to load the title block to a database table, 
	then your choice of platform and "7" to run all modules.  Choosing 
	"8" runs the modules in #7 inside a callable module called "process"
	as in "import from csv-edit process".  
	\n
	The TODO list has a GUI interface for setting the filename and 
	outFile stub(s).\n''')

if __name__ == '__main__':
	main()
