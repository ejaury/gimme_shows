from exceptions import NotImplementedError

class BaseClient():
  def __init__(self, save_to=None):
    raise NotImplementedError

  def start_from_file(self, torrent_path, save_to=None):
    raise NotImplementedError

  def start_from_url(self, url, save_to=None):
    raise NotImplementedError
