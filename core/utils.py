import ConfigParser
from logger import Logger
from settings import settings

class Indexer:
  torrent_key = 'torrent_url'

  def __init__(self, log=None):
    self.logger = Logger.get_logger(self.__class__.__name__)
    self.log_file = log or getattr(settings, 'LATEST_DOWNLOADED_LOG_PATH')
    self.config = ConfigParser.ConfigParser()
    self.config.read(self.log_file)

  def episode_exists(self, show_name, torrent_name):
    # Not a smart indexer, only tries to match whatever torrent filename is in
    # the config file. It doesn't know whether a torrent has been downloaded
    # before or not. In the future, this should be able to know if an episode
    # has been downloaded or not.
    try:
      self.logger.debug("Trying to check if '%s' exists in show '%s'" %
        (show_name, torrent_name))
      return self.config.get(show_name, self.torrent_key) == torrent_name
    except ConfigParser.NoSectionError:
      return False
    except ConfigParser.NoOptionError:
      return False

  def save(self, show_name, torrent_name):
    if not self.config.has_section(show_name):
      self.logger.debug('Adding section for show: %s' % show_name)
      self.config.add_section(show_name)

    self.logger.debug("Saving show '%s' torrent as '%s'" %
      (show_name, torrent_name))
    self.config.set(show_name, self.torrent_key, torrent_name)
    self.logger.debug('Write changes to show log')
    self.config.write(open(self.log_file, 'w'))

#
# Get fully qualified name for an object (including module and class names)
#
def get_fullname(o):
  return '%s.%s' % (o.__module__, o.__class__.__name__)
