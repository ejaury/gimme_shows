import subprocess
from client.base import BaseClient
from settings import settings

class UTorrent(BaseClient):
  def __init__(self, save_to=None):
    self.save_to = save_to or getattr(settings, 'SAVE_DIR')

  def start_from_url(self, url, save_to=None):
    print 'Saving torrent from: %s' % url

    if save_to:
      print 'Download file to %s' % save_to
    else:
      print 'Download file to %s' % self.save_to

    print 'Start uTorrent to download'
