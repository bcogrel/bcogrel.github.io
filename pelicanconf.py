#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Benjamin Cogrel'
SITENAME = u"Benjamin Cogrel"
SITEURL = 'https://research.bcgl.fr'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'
LOCALE = 'en_UK' 

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# EMAIL_ADDRESS = "lastname AT inf.unibz.it"
GITHUB_ADDRESS = "https://github.com/bcogrel"
TWITTER_ADDRESS = "https://twitter.com/bcogrel"
PROFILE_IMAGE_URL = "/images/bcogrel.jpg"
SHOW_ARTICLE_AUTHOR = False
LICENSE_NAME = ""
EXT_BLOG_ADDRESS = "https://blog.bcgl.fr"
DEFAULT_DATE_FORMAT = '%B %Y'


# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('Ontop', 'http://ontop.inf.unibz.it'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

THEME = "/home/benji/envs/pelican-2.7/deps/crowsfoot/"
