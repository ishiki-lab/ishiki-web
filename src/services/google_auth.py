import os
import config
import app_secrets

print("app_secrets.__file__", app_secrets.__file__)

CREDS_DIR = os.path.join(os.path.dirname(app_secrets.__file__), "creds")


def creds_path():
    return os.path.join(CREDS_DIR, config.GOOGLE_CREDENTIAL_FILE)


