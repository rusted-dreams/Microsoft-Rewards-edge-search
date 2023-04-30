import webbrowser
import time
import os
import importlib
import subprocess
import sys


def install_wonderwords_module():  # if the wonderwords is not installed then this function installs it.
    try:
        module = importlib.import_module("wonderwords")
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "wonderwords"])
        module = importlib.import_module("wonderwords")
    return module

install_wonderwords_module()

from wonderwords import RandomWord



def open_edge_browser():
    edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    webbrowser.register("edge", None, webbrowser.BackgroundBrowser(edge_path))


def perform_search():

    open_edge_browser()
    
    for i in range(10):
        search_term = RandomWord().word()
        time.sleep(3)
        url = f"https://www.bing.com/search?q={search_term}"
        webbrowser.get("edge").open_new_tab(url)

    os.system("taskkill /f /im msedge.exe")


for i in range(9):
    perform_search()