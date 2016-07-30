# -*- coding: utf-8 -*-
from __future__ import unicode_literals

OUTPUT_PATH = 'output/'
PAGE_PATHS = ['pages']
PAGE_SAVE_AS = '{slug}.html'


SITENAME = "Predict23"
SITEURL = 'https://predict23.ru'


AUTHOR = u"Проект &laquo;Прогноз-23&raquo;"

DESCRIPTION = u'Расчет и заполнение рекомендуемых товаров на основе статистики просмотров и заказов'
GITHUB_URL = 'https://github.com/Predict23'
DISQUS_SITENAME = "blog-notmyidea"


FEED_ALL_ATOM=None

TIMEZONE = "Europe/Moscow"

# can be useful in development, but set to False when you're ready to publish
RELATIVE_URLS = True

REVERSE_CATEGORY_ORDER = True
LOCALE = "ru_RU.UTF-8"
DEFAULT_PAGINATION = 4
DEFAULT_DATE = (2012, 3, 2, 14, 1, 1)


# path-specific metadata
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
}

# static paths will be copied without parsing their contents
STATIC_PATHS = [
    'pictures',
    'extra/robots.txt',
]



