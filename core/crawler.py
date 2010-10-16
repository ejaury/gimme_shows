import os
import utils
from lib import feedparser
from logger import Logger
from source.sources import EzrssFeed
from settings import settings
from utils import Indexer

class Crawler:
  def __init__(self, list_file):
    self.logger = Logger.get_logger(utils.get_fullname(self))
    self.list_file = list_file
    self.indexer = Indexer()
    self._client = None

  # return raw list in list format
  def parse_list(self, list_file):
    try:
      self.logger.info('Opening RSS file: %s' % list_file)
      f = open(list_file, 'r')
    except IOError:
      self.logger.error('Cannot read file: %s' % list_file)
      return -1

    self.feeds_list = []
    
    line = f.readline()
    while line: 
      self.logger.debug('Reading: %s' % line)
      feeds = feedparser.parse(line)
      try:
        # default only get the latest entry
        raw_f = feeds['entries'][0]
        feed_item = EzrssFeed(raw_f.link)
        feed_item.parse_name(raw_f.summary or raw_f.value)
        feed_item.parse_season(raw_f.summary or raw_f.value)
        self.feeds_list.append(feed_item)
      except IndexError:
        pass
      line = f.readline()

  @property
  def client(self):
    return self._client

  @client.setter
  def client(self, c):
    self._client = c

  def run(self):
    self.parse_list(self.list_file) 
    self.logger.info('Start checking latest RSS feeds')
    for feed in self.feeds_list:
      if feed.name:
        if not self.indexer.episode_exists(feed.name, feed.url):
          save_path = os.path.join(getattr(settings, 'SAVE_DIR'),
                                   feed.name,
                                   feed.season)
          self.client.start_from_url(feed.url, save_path)
          self.indexer.save(feed.name, feed.url)
      else:
        continue

    self.logger.info('Exiting application')
