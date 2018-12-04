"""
Sort a list by putting the system to sleep for the duration of the list element itself.
Algorithm as described on 4chan.
Author: Pairode Jaroensri
Last visited: May 15, 2017
"""

from time import sleep
from multiprocessing import Process

def sl_print(i):
    sleep(i)
    print(i * 100)

def sleep_sort(lst):
    for i in lst:
        Process(target=sl_print, args=(i / 100,)).start()
