csvEdit
========

For editing csv files down to size, removing excess bloatage and unneeded columns

csvEdit License
	Copyright 2013 Wolf Halton <wolf@sourcefreedom.com>
  
	This program is free software; you can redistribute it and/or modify
	it under the terms of the GNU General Public License as published by
	the Free Software Foundation; either version 2 of the License, or
	(at your option) any later version.

caller.py is the front-end that calls the reader.
    How to use: either put the csv-edit folder in your dist-packages folder 
    or invoke caller on the command line from inside the csv-edit folder.  
    Current choices to use are "1" - to process your raw Qualys csv output file.

reader.py is the set of modules that processes the raw Qualys csv file.  
    If you have not added the csv-edit folder to the dist-packages folder, 
    you need to put the file you are processing in the csv-edit folder.

csvEdit uses web2py as a web front-end.  
	Web2py License
	Web2py is Licensed under the LGPL license version 3 
	(http://www.gnu.org/licenses/lgpl.html)

	Copyrighted (c) by Massimo Di Pierro (2007-2013)
    
How to use: 
    '''                *** Help File ***\n
	Choices 1 through 5 produce csv files broken down into the "Title 
	Block" with the details of the test, requester, date of test, 
	business unit and so on; and the content of the individual 
	vulnerabilities, differentiated by OS - specifically Linux, Windows 
	and Other.  There is also an "ALL OS" choice, which is likely to be 
	the one you want to use to load the database, where you might want 
	counts and specifics by various operating system platforms.\n
	The next three choices, 6 through 8 are related to the database.  
	If you want to run the system by hand, you can type the platform 
	number and then "7" to load the title block to a database table, 
	then your choice of platform and "8" to run all modules.  Choosing 
	"9" runs the modules in #8 inside a callable module called "process"
	as in "import from csv-edit process".
	All the files are put into an eponymously-titled directory.  This 
	should be easier to zip and move
	\n
	The TODO list is:
		to develop a GUI (web) interface with web2py
		to create list of sql commands for analyst's report
