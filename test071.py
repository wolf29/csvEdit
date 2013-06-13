#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#   test071.py  
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
	outFileL = 'outl' 
	outFileC = 'outc'
	while choice != "swallow":
		print('\nEnter   "1"  for Linux')
		print('        "2"  for Windows')
		print('        "3"  for all otherplatforms')
		print('      ******************************')
		print('        "4"  Check SQLite3 version')
		print('        "5"  Test Table Creation')
		print('       "99"  to exit the script')
		
		os_choice = raw_input('      \n     =>  ')

		qu = ""
		if os_choice == "1":
			qu = "nix"
		elif os_choice == "2":
			qu = "win"
		elif os_choice == "3":
			qu = "other"
		elif os_choice == "4":
			lite_ver = litever()
		elif os_choice == "5":
			lite_ver = test_table(filename)
		elif os_choice == "99":
			choice = "swallow"
			break
		else: continue
		filename2 = titleblock(filename)
		(filename, outFileL) = labels(filename, outFileL)
		(filename, qu, outFileC) = content(filename, qu, outFileC)

		print(" Input File = %s,\n cycle = %s,\n Output Label File = %s,\n Output Content File = %s" % (filename, qu, outFileL, outFileC))
	return 0

def titleblock(filename):
	with open('titleblock_'+filename, 'wb') as title:
		writer = csv.writer(title)
		with open(filename, 'rb') as mycsv:
			reader = csv.reader(mycsv)
			counter = 0
			for counter,row in enumerate(reader):
				if counter < 1: continue
				if counter > 6: break
				#print(row)
				writer.writerow(row)

def labels(filename, outFileL):
	print(type(filename))
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
		print outFileC
		writer = csv.writer(content)
		with open(filename, 'rb') as mycsv:
			reader = csv.reader(mycsv)
			counter = 0
			for counter,row in enumerate(reader):
				if counter < 7: continue
#				if counter > ([-2:]) : break # This string-slicing technique doesn't work on lists made by csv module for some reason
				rowEdit = [row[0],row[22],row[2], row[4], row[6], row[15], row[16], row[11], row[18], row[19], row[20], row[25], row[26], row[27], row[28], row[29], row[30], row[31]]
				if qu == "nix":
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

if __name__ == '__main__':
	main()
