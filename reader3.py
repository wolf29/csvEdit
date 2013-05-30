#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#   reader2.sh  
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
row = ['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',]
rowEdit = [row[0],row[22],row[2], row[4], row[6], row[15], row[16], row[11], row[18], row[19], row[20], row[25], row[26], row[27], row[28], row[29], row[30], row[31]]
#[0,22,2,4,6,15,16,11,18,19,20,25,26,27,28,29,30,31]
filename=''

def main():
	filename=raw_input("enter the filename==>  ")
	t=titleblock(filename)
	L=labels(filename)
	c=content(filename)
	r=tailey(filename)
	print(t,'\n',c,'\n',r,'\n')
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
				print(row)
				writer.writerow(row)

def labels(filename):
	row = ['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',]
	rowEdit = [row[0],row[22],row[2], row[4], row[6], row[15], row[16], row[11], row[18], row[19], row[20], row[25], row[26], row[27], row[28], row[29], row[30], row[31]]
	with open('labels_'+filename, 'wb') as labels:
		writer = csv.writer(labels)
		with open(filename, 'rb') as mycsv:
			reader = csv.reader(mycsv)
			counter = 0
			for counter,row in enumerate(reader):
				if counter == 7:
					rowEdit = [row[0],row[22],row[2], row[4], row[6], row[15], row[16], row[11], row[18], row[19], row[20], row[25], row[26], row[27], row[28], row[29], row[30], row[31]]
					print(rowEdit)
					writer.writerow(rowEdit)

def content(filename):
	row = ['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',]
	rowEdit = [row[0],row[22],row[2], row[4], row[6], row[15], row[16], row[11], row[18], row[19], row[20], row[25], row[26], row[27], row[28], row[29], row[30], row[31]]
	with open('content_'+filename, 'wb') as labels:
		writer = csv.writer(labels)
		with open(filename, 'rb') as mycsv:
			reader = csv.reader(mycsv)
			counter = 0
			for counter,row in enumerate(reader):
				if counter < 8: continue
#				if counter > ([-2:]) : break 
				rowEdit = [row[0],row[22],row[2], row[4], row[6], row[15], row[16], row[11], row[18], row[19], row[20], row[25], row[26], row[27], row[28], row[29], row[30], row[31]]
				print('boop-beep',rowEdit)
				writer.writerow(row)

def tailey(filename):
	with open('endblock_'+filename, 'wb') as endblock:
		writer = csv.writer(endblock)
		with open(filename, 'rb') as mouse:
			reader=csv.reader(mouse)
			what=mouse.readlines()[-2:]
			for i in what:
				print(i)
				writer.writerows(i)

if __name__ == '__main__':
	main()

