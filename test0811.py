#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#   test0811.py  
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
import sqlite3 as lite
import sys

con = None


def main():
	choice = "chew"
	filename=raw_input("enter the filename==>  ")
	outFileT = ''
	outFileL = '' 
	outFileC = ''
	while choice != "swallow":
		os_choice = "100099"
		while os_choice != "99" :
			print('\nEnter   "1"  for Linux')
			print('        "2"  for Windows')
			print('        "3"  for all other platforms')
			print('      ******************************')
			print('        "4"  Check SQLite3 version')
			print('        "5"  Test Table Creation')
			print('        "6"  Load Titleblock to DB from csv File')
			print('        "7"  Load Content to DB from csv File')
			print('       "99"  to exit the script')
				
			os_choice = raw_input('      \n     =>  ')
			qu = ""
			if os_choice == "1":
				qu = "lin"
			elif os_choice == "2":
				qu = "win"
			elif os_choice == "3":
				qu = "other"
			elif os_choice == "4":
				lite_ver = litever()
			elif os_choice == "5":
				lite_ver = test_table(filename)
			elif os_choice == "6":
				lite_push = load_titles(filename)
			elif os_choice == "7":
				lite_push_2 = load_content(outFileC)
			elif os_choice == "99":
				break
			else: continue
			(filename, outFileT) = titleblock(filename, outFileT)
			(filename, outFileL) = labels(filename, outFileL)
			(filename, qu, outFileC) = content(filename, qu, outFileC)
			print(" Input File          = %s,\n Current Platform    = %s,\n Output Title File   = %s\n Output Label File   = %s,\n Output Content File = %s" % (filename, qu, outFileT, outFileL, outFileC))
		run_away = raw_input("if you would like to run with a different source-file, type 'y'\nIf you would like to run away, type 'r'")
		if run_away == 'y':
			filename=raw_input("enter the filename==>  ")
		elif run_away == 'r':
			print("Thanks for using the csv-edit scripts.")
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
	with open(qu+'_content_'+filename, 'wb') as content:
		outFileC = qu+'_content_'+filename
		writer = csv.writer(content)
		with open(filename, 'rb') as mycsv:
			reader = csv.reader(mycsv)
			counter = 0
			for counter,row in enumerate(reader):
				if counter < 7: continue
#				if counter > ([-2:]) : break # This string-slicing technique doesn't work on lists made by csv module for some reason
				rowEdit = [row[0],row[22],row[2], row[4], row[6], row[15], row[16], row[11], row[18], row[19], row[20], row[25], row[26], row[27], row[28], row[29], row[30], row[31]]
				if qu == "lin":
					lisst = chklist
					if any(item in row[4] for item in lisst):
						writer.writerow(rowEdit)
				elif qu == "win":
					lisst = wchklist
					if any(item in row[4] for item in lisst):
						writer.writerow(rowEdit)
				elif qu == "other": 
					lisst = ochklist
					if row[4] not in lisst:
						writer.writerow(rowEdit)
	return (filename, qu, outFileC)


def litever():
	try:
		con = lite.connect('test.db')
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

def test_table(f):
	cars = (
	(1, 'Audi', 52642),
	(2, 'Mercedes', 57127),
	(3, 'Skoda', 9000),
	(4, 'Volvo', 29000),
	(5, 'Bentley', 350000),
	(6, 'Hummer', 41400),
	(7, 'Volkswagen', 21600)
	)

	try:
		con = lite.connect('test.db')
		with con:
			cur = con.cursor()    
			cur.execute("DROP TABLE IF EXISTS Cars")
			cur.execute("CREATE TABLE Cars(Id INT, Name TEXT, Price INT)")
			cur.executemany("INSERT INTO Cars VALUES(?, ?, ?)", cars)
	
	except lite.Error, e:
		if con:
			con.rollback()
		print "Error %s:" % e.args[0]
		sys.exit(1)

	finally:
		if con:
			con.close() 

def load_titles(f):
	filename = f
	titles=[]
	with open(filename, 'rb') as mycsv:
			reader = csv.reader(mycsv)
			counter = 0
			for counter,row in enumerate(reader):
				if counter < 1: continue
				if counter > 6: break
				titles.append(row)
				 
#			print titles
		
			tests = (1, titles[0][0], titles[0][1], titles[0][2], titles[0][3], titles[0][4], titles[0][5], titles[0][6], titles[1][0], titles[1][1], titles[1][2], titles[4][0], titles[4][1], titles[4][2], titles[4][3], titles[4][4], titles[4][5], titles[4][6]),
			
#			print(tests)
	try:
		con = lite.connect('test.db')
		with con:
			cur = con.cursor()    
			cur.execute("DROP TABLE IF EXISTS tests")
			cur.execute("CREATE TABLE tests(Id INTEGER PRIMARY KEY, Corp TEXT, Address_1 TEXT, Address_2 TEXT, City TEXT, State TEXT, Country TEXT, Postal_Code TEXT, Requester TEXT, Code_1 TEXT, Role TEXT, Asset_Groups TEXT, IPs TEXT, Active_Hosts INT, Hosts_Matching_Filters INT, Trend_Analysis TEXT, Date_Range TEXT, Asset_Tags TEXT)")
			cur.executemany("INSERT INTO tests VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", tests)
	
	except lite.Error, e:
		if con:
			con.rollback()
		print "Error %s:" % e.args[0]
		sys.exit(1)

	finally:
		if con:
			con.close() 

def load_content(f):
	filename = f
	with open(filename, 'rb') as mycsv:
		print(filename)
		id = 1
		reader = csv.reader(mycsv)
		counter = 0
		for counter,row in enumerate(reader):
			if counter > 8: 
				continue
			print(row)
#			chine = (test.tests.id, row[0],row[2], row[4])
			vuln = (id, str(row[0]),str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8]), str(row[9]), str(row[10]), str(row[11]), str(row[12]), str(row[13]), str(row[14]), str(row[15]), str(row[16]), str(row[17]))
			print "Look, this is vuln =>  ", vuln
			try:
				con = lite.connect('test.db')
				with con:
					cur = con.cursor()    
#					cur.execute("DROP TABLE IF EXISTS machines")
#					cur.execute("CREATE TABLE machines(Id INTEGER PRIMARY KEY, Test_ID INT, IP TEXT, NetBIOS TEXT, OS TEXT)")
#					cur.executemany("INSERT INTO machines VALUES(?, ?, ?, ?, ?)", chines)

					cur.execute("DROP TABLE IF EXISTS vulnerabilities")
					cur.execute("CREATE TABLE vulnerabilities(Id INTEGER PRIMARY KEY, IP TEXT, CVSS_Base TEXT, NetBIOS TEXT, OS TEXT,  QID TEXT, First_Detected TEXT, Last_Detected TEXT, Port TEXT, CVE_ID TEXT, Vendor_Reference TEXT, Bug_traq_ID TEXT, Threat TEXT, Impacts TEXT, Solution TEXT, Exploitability TEXT, Associated_Malware TEXT, Results TEXT, PCI_Vuln TEXT)")
					cur.executemany("INSERT INTO vulnerabilities VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", vuln)

			except lite.Error, e:
				if con:
					con.rollback()
					print "Error %s:" % e.args[0]
					sys.exit(1)

			finally:
				if con:
					con.close() 

if __name__ == '__main__':
	main()
