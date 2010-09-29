#!/usr/bin/env python

from core import *
from client.utorrent import UTorrent
from settings import settings

def main():
  crawler = Crawler('./rss_list')
  logger = Logger.get_logger('Main')
  crawler.client = UTorrent(getattr(settings, 'SAVE_DIR'))
  logger.info('Created an instance of %s client with save directory pointed to: %s'
      % (crawler.client.__class__.__name__, crawler.client.save_to))
  crawler.run()

if __name__ == '__main__':
  main()
