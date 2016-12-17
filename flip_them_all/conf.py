

from distutils.spawn import find_executable

class Settings(object):

    def __init__(self):
        self.ffmpeg = find_executable("ffmpeg")


settings = Settings()
