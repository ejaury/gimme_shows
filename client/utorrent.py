import subprocess
from client.base import BaseClient
from core import utils
from core.logger import Logger
from settings import settings

class UTorrent(BaseClient):
  def __init__(self, save_to=None):
    self.logger = Logger.get_logger(utils.get_fullname(self))
    self.save_to = save_to or getattr(settings, 'SAVE_DIR')

  def start_from_url(self, url, save_to=None):
    save_dir = save_to or self.save_to
    torrent_dir = getattr(settings, 'TORRENT_DIR')
    cmd = 'wget %s -P %s 2&>1 /dev/null' % (url, torrent_dir)
    self.logger.info('Launching torrent client to download %s' % url)
    self.logger.debug('Executing subprocess command: %s' % cmd)
    subprocess.Popen(cmd, shell=True)
