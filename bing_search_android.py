import androidhelper
import time
import subprocess
import importlib


def install_wonderwords_module():  # if the wonderwords is not installed then this function installs it.
    try:
        module = importlib.import_module("wonderwords")
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "wonderwords"])
        module = importlib.import_module("wonderwords")
    return module

install_wonderwords_module()

from wonderwords import RandomWord

search_term = RandomWord().word()
droid.startActivity('android.intent.action.VIEW', f'bing://search?q={search_term}')