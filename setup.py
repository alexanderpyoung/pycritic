try:
  from setuptools import setup
except ImportError:
  from distutils.core import setup

config = {
    'description': 'A Metacritic scraper for Python 3',
    'author': 'Alexander Young',
    'url': '',
    'download_url': '',
    'author_email': 'alexander@lxndryng.com',
    'version': '0.1',
    'install_requires': ['nose', 'requests', 'beautifulsoup4'],
    'packages': ['pycritic'],
    'scripts': [],
    'name': 'pycritic'
    }

setup(**config)
