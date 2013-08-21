#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  functional_tests.py
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



try: import unittest2 as unittest #for Python <= 2.6
except: import unittest
import sys, urllib2
sys.path.append('./fts/lib')
from selenium import webdriver
import subprocess
import sys
import os.path

ROOT = 'http://localhost:8001'

class FunctionalTest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.web2py = start_web2py_server()
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(1)

    @classmethod    
    def tearDownClass(self):
        self.browser.close()
        self.web2py.kill()

    def get_response_code(self, url):
        """Returns the response code of the given url

        url     the url to check for 
        return  the response code of the given url
        """
        handler = urllib2.urlopen(url)
        return handler.getcode()


def start_web2py_server():
    #noreload ensures single process
    print os.path.curdir    
    return subprocess.Popen([
            'python', '../../web2py.py', 'runserver', '-a "LucyLoo2"', '-p 8001'
    ])

def run_functional_tests(pattern=None):
    print 'running tests'
    if pattern is None:
        tests = unittest.defaultTestLoader.discover('fts')
    else:
        pattern_with_globs = '*%s*' % (pattern,)
        tests = unittest.defaultTestLoader.discover('fts', pattern=pattern_with_globs)

    runner = unittest.TextTestRunner()
    runner.run(tests)

if __name__ == '__main__':
    if len(sys.argv) == 1:
        run_functional_tests()
    else:
        run_functional_tests(pattern=sys.argv[1])

