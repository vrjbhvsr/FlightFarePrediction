from logger import logging
import os
import sys
from datetime import datetime

class App_logger:
    def __init__(self):
        pass
    def log(self,file_name, message):
        self.now = datetime.now()
        self.date = self.now.date
        self.current_time = self.now.strftime('%H%M%S')
        file_name.write(
            str(self.date+'/'+str(self.current_time) + '\t\t' + message + '\n')
        )

