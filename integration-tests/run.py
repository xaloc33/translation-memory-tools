#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
# Copyright (c) 2013 Jordi Mas i Hernandez <jmas@softcatala.org>
# Copyright (c) 2014 Leandro Regueiro Iglesias <leandro.regueiro@gmail.com>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place - Suite 330,
# Boston, MA 02111-1307, USA.

import sys
sys.path.append('../src/')

from HTMLParser import HTMLParser
from Queue import Queue
from optparse import OptionParser
from checkdownloads import CheckDownloads
from checksearch import CheckSearch
from crawler import Crawler
import urllib2
import urlparse

site_url = None

def read_parameters():
    global site_url

    parser = OptionParser()

    enviroments = {
        'localhost': 'http://localhost:8080/',
        'dev': 'http://www.softcatala.org/recursos/dev/',
        'preprod': 'http://www.softcatala.org/recursos/preprod/',
        'prod': 'http://www.softcatala.org/recursos/',
    }

    opt_enviroments = "localhost, dev, prepod, prod"
    parser.add_option("-e", "--enviroment", dest="enviroment", default="prod",
                      type="choice", choices=enviroments.keys(),
                      help="set default enviroment to: " + opt_enviroments)

    (options, args) = parser.parse_args()
    site_url = enviroments.get(options.enviroment, None)


if __name__ == '__main__':
    read_parameters()
    print("Integration tests for: " + site_url)
    print("Use --help for assistance")

    search = CheckSearch(site_url)
    if not search.check():
        sys.exit(1)

    crawler = Crawler(site_url + "memories.html")
    crawler.run()
    
    downloads = CheckDownloads(crawler.get_all_links())
    downloads.check()

    if downloads.errors > 0:
        print('Total download errors {0}'.format(downloads.errors))
        sys.exit(1)

    sys.exit(0)
