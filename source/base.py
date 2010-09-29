class BaseSourceFeed:
  def __init__(self, url=None):
    self.url = url
    self.name = ''
    self.season = ''

  def parse_name(self, raw_info):
    pass

  def parse_season(self, raw_info):
    pass
