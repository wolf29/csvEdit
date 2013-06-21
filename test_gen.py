#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  untitled.py
#  
#  Copyright 2013 Wolf Halton  <wolf@sourcefreedom.com>
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
import random


def main():
	i = 0
	chklist=["OS","Red Hat Enterprise Linux ES 3", "Linux 2.4-2.6 / Embedded Device / F5 Networks Big-IP", "Linux 2.4-2.6 / SonicWALL", "Linux 2.6", "Red Hat Enterprise Linux ES 4", "Red Hat Enterprise Linux Server 5.8", "Linux*"]
	wchklist=["OS", "Windows 2003 Service Pack 2", "Windows 2008 R2 Enterprise Service Pack 1", "Windows Server 2003 Service Pack 2", "Windows Server 2008 R2 Enterprise 64 bit Edition Service Pack 1","Windows"]
	ochklist=chklist+wchklist
	print(len(ochklist))
	

	while i < 102:
		i = i + 1
		print(ochklist[random.randint(0,13)])

	return 0

if __name__ == '__main__':
	main()

