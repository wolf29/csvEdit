#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  untitled.py
#  Purpose of this application is to search a given csv and present 
#     a summary of QID, IP operating system and so on. 
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

import os, sys, csv


def main():
	print('''This application will summarize and count content of any \
field within the CSV file you have supplied.  \n     The chosen outputs \
will be output into a fime of arbitrary length.  \n     The fields are \
numbered from zero (0) to whatever the last field is (n-1). \n     \
You will get a chance to preview the content before sending it to \
the email account of your choice.''')
	eml = ''
	filename = raw_input("Enter Filename including full path unless \n the file is in current directory =>  ")
	email=mail(eml)
#	L=labels(filename)
#	c=content(filename)
#	r=tailey(filename)
	print("The filename you chose is         \t %s \nThe Email Address you entered was \t %s " % (filename, email))
	return 0

def mail(eml):
	approval = False
	while approval == False:
		eml=raw_input("enter email address to which you wish results to be sent =>  ")
		print(eml)
		response=raw_input('Is this the correct email address? \n "Y" of "y" for "Yes." "N" or "n" for "No." =>  ')
		if response=="N" or response=="n":
			 print("Please Re-enter Your Email Address")
		else: 
			approval = True
	return eml



if __name__ == '__main__':
	main()

