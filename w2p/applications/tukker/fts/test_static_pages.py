#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  test_static_pages.py
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


from functional_tests import FunctionalTest, ROOT

class TestHomePage (FunctionalTest):

    def setUp(self):
        # John opens his browser and goes to the home-page of the tukker app
        self.url = ROOT + '/tukker/'
        get_browser=self.browser.get(self.url)

    def test_can_view_home_page(self):
        # Let's check if the website was loaded ok => response code == 200
        response_code = self.get_response_code(self.url)
        self.assertEqual(response_code, 200)

    def test_has_right_title(self):        
        # First he looks at the topbar and sees 'MicroPosts On Steroids'
        
        title = self.browser.find_element_by_tag_name('title')
        self.assertEqual('MicroPosts On Steroids', title.text)

    def test_has_right_heading(self):        
        # He's looking for the Heading "Messages With 300 Chars"
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Messages With 300 Chars', body.text)
