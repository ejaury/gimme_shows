import re
from source.base import BaseSourceFeed
from core import utils
from core.logger import Logger

class EzrssFeed(BaseSourceFeed):
  src = 'http://www.ezrss.it/'

  def __init__(self, url=None):
    BaseSourceFeed.__init__(self, url)
    self.logger = Logger.get_logger(utils.get_fullname(self))
    self.logger.debug('Created an instance')

  def parse_name(self, raw_info):
    try:
      self.name = re.sub(r';[:\d\w\s//]*', '', re.sub(r'Show Name: *', '', raw_info))
    except:
      self.logger.error('Cannot parse Name from: %s' % raw_info)
    finally:
      if raw_info == self.name or not self.name:
        self.name = 'my show'

  def parse_season(self, raw_info):
    try:
      self.season = re.sub(r';[:\d\w\s//]*', '', re.sub(r'.*Season: *', '', raw_info))
    except:
      self.logger.error('Cannot parse season number from: %s' % raw_info)
    finally:
      if raw_info == self.season or not self.season:
        self.season = ''
      else:
        self.season = 'Season %s' % self.season

