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


def open_edge_browser(): #The function opens the edge browser.
    edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    webbrowser.register("edge", None, webbrowser.BackgroundBrowser(edge_path))


def perform_search(): #This opens a new tab and does a random word search.

    open_edge_browser()
    
    for i in range(10):
        search_term = RandomWord().word() #generates a random word to search for.
        time.sleep(2)  #waits 2 sec before opening a new tab to allow the search to happen first.
        url = f"https://www.bing.com/search?q={search_term}"
        webbrowser.get("edge").open_new_tab(url)

    os.system("taskkill /f /im msedge.exe") #Closes the browser for after 10 searches/tabs.


for i in range(9):
    perform_search()
