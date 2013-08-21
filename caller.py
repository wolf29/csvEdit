#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  caller.py
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
import time
from reader import process

def main():
	''' How to use: either put the csv-edit folder in your dist-packages
	folder or invoke caller on the command line from inside the 
	csv-edit folder.  Current choices to use are "1" - to process your 
	raw Qualys csv output file, 88 for this help string and 99 to run 
	away.
	'''
	
	#--start constants--
	__version__ = "0.0.0.1"
	#--end constants--

	choice = "chew"
	
	filename=raw_input("enter the filename==>  ")
	qu = "all"
	outFileT = ''
	outFileL = '' 
	outFileC = ''
	outFileQ = ''
	outFileM = ''
	outFileE = ''
	current_db = filename[:-4]+'.db' 
	outdir = ''
	qu = ''
	outFileQ, outFileM, outFileE,

	while choice != "swallow":
		os_choice = "100099"
		while os_choice != "99" :

			print('\nEnter  "1"  Fully automates reader.process() module')
			print('      ******************************')
			print('      "88"  Display Help File')
			print('      "99"  to exit the script')
				
			os_choice = raw_input('      \n     =>  ')
			
			if os_choice == "1":
				(filename, outdir, qu, outFileT, outFileL, outFileC, outFileQ, outFileM, outFileE, current_db) = process(filename, outdir, qu, outFileT, outFileL, outFileC, outFileQ, outFileM, outFileE, current_db)
			#	(filename, qu, outFileT, outFileL, outFileC, current_db) = process(filename, qu, outFileT, outFileL, outFileC, current_db)
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

def help_me():
	print('''
	How to use: either put the csv-edit folder in your dist-packages
	folder or invoke caller on the command line from inside the 
	csv-edit folder.  Current choices to use are "1" - to process your 
	raw Qualys csv output file, 88 for this help string and 99 to run 
	away.''')
	
if __name__ == '__main__':
	main()

