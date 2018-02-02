#!/usr/bin/env python
import shelve
from datetime import datetime, timedelta
import time
import sys



class Stopwatch(object):

    def __init__(self):
        self.start_time = time.time()
        input("Press Enter to stop...")
        time_elapsed = time.time() - self.start_time 
        time_elapsed += self.get_time_previous()
        self.save_time(time_elapsed)
        time_str = timedelta(seconds=time_elapsed)
        print(f'Total time today: {time_str}')

    def get_key(self):
        return datetime.today().strftime(f'%Y%m%d')

    def get_time_previous(self):
        k = self.get_key()
        with shelve.open('times') as shelf:
            return shelf.get(k, 0)

    def save_time(self, time_elapsed):
        k = self.get_key()
        with shelve.open('times') as shelf:
            shelf[k] = time_elapsed


def main():
    sw = Stopwatch()



if __name__ == '__main__':
    main()