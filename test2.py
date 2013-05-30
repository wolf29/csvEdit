#!/usr/bin/python 
#test2.py
import csv
filename="test4.csv"
print(filename)
def main():
	filename="test31.csv"
	www=titleblock(filename)
	ttt=tailey(filename)
	print(www)
	print(ttt)
	print(filename)
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
				print('something',row)
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
