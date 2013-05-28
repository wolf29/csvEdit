#!/bin/bash -x
#  spliff.sh
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
#sed -n '8,13p' datafile.txt > newfile.txt
echo "enter input file"; read infile

ct=`cat $infile |wc -l`
ct0=`expr $ct - 0`
ct1=`expr $ct - 1`
ct2=`expr $ct - 2`
echo $ct, $ct1, $ct2
# Clean up the output files

slim="`echo $infile | cut -d '.' -f 1 `"
echo "$slim is the stub"

sed -n '1,7p' "$infile" > "$slim"_title.csv

sed -n "8p" "$infile" > "$slim"_labels.csv

sed -n "9,$ct2"p "$infile" > "$slim"_content.csv

sed -n "$ct1,$ct"p "$infile" > "$slim"_endblock.csv

