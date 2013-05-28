#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  untitled.py
#  
#  Copyright 2013 mhalton <mhalton@mint-141>
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


def main():
    lc = sum(1 for l in open('test4.csv'))
    print(lc)
    print open("test4.csv").read().replace("\0", ">>>NUL<<<")
    with open('test4.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)
            print(row[2])
    with open('test4.csv', 'rb') as f,open('out.csv', 'wb') as f_out:
        reader = csv.reader(f)
        writer = csv.writer(f_out)
        for row in reader:
            rroww=('moo', row[3], row[5])
            writer.writerow((rroww))
            
	return 0

if __name__ == '__main__':
	main()

