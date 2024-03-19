import os
import sys
from datetime import datetime

class App_logger:
    def __init__(self):
        pass
    def log(self,folder_name,file_name, message):
        self.now = datetime.now()
        self.date = self.now.date()
        self.current_time = self.now.strftime('%H%M%S')

        
        os.makedirs(folder_name,exist_ok=True)
        with open(os.path.join(folder_name,file_name),'a+') as f:
            f.write(str(self.date)+'/'+str(self.current_time) + '\t\t' + message + '\n')
        

