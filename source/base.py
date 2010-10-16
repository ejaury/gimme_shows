from exceptions import NotImplementedError

class BaseSourceFeed:
  def __init__(self, url=None):
    self.url = url
    self.name = ''
    self.season = ''

  def parse_name(self, raw_info):
    raise NotImplementedError

  def parse_season(self, raw_info):
    raise NotImplementedError
