import os
import sys

APP_MODE_PRODUCTION = "production"
APP_MODE_DEVELOPMENT = "development"
APP_MODE_TEST = "test"

class AppConfig(object):

    APP_MODE_PRODUCTION = "production"
    APP_MODE_DEVELOPMENT = "development"
    APP_MODE_TEST = "test"

    def __init__(self):
        mode = os.environ.get('APP_MODE', 'development')
        self.set_mode(mode)

    def set_mode(self, mode):
        self.APP_MODE = mode
        print("mode: %s" % self.APP_MODE)

        if self.APP_MODE == "production":
            from app_secrets import config_prod as conf
        elif self.APP_MODE == "development":
            from app_secrets import config_dev as conf
        else:
            from app_secrets import config_test as conf

        self.conf = conf


    def __getattr__(self, name):

        try:
            return getattr(self.conf, name)
        except AttributeError as e:
            return None

sys.modules[__name__] = AppConfig()


