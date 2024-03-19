from src.logger import App_logger
from src.exception import CustomException
import os
import sys
import json
import shutil
import datetime
import pandas as pd

class RawDataValidation:
    def __init__(self,raw_data_directory):
        self.raw_data_directory = raw_data_directory
        self.logger = App_logger()
        self.schema = 'schema.json'

    def ValueFromSchema(self):
        '''This function valiadtes that Wheter the new upcoming data files has expected Number of columns from the schema prepared.
        '''
        try:
        
            self.logger.log('Training_Logs', 'RawDataValidation.txt', "Raw Data Validation iunitiated.")
            with open(self.schema,'r') as f:
                j_file = json.load(f)
                f.close()
            no_of_columns = j_file['NumberofColumns']
            col_names =  j_file['ColName']
            self.logger.log('Training_Logs','RawDataValidation.txt', f"The total number of columns are {no_of_columns}")

            return no_of_columns, col_names
        
        except Exception as e:
            raise CustomException(e,sys)
        

    def CreateGoodBadDataDirectory(self):
        '''This function will create a Good/Bad data directory'''
        try:
            self.logger.log('Training_Logs','RawDataValidation.txt', 'creating Good data and Bad data directory')

            good_path = os.path.join("Validated_training_data/", "GoodRawData/")

            if not os.path.exists(good_path):
                os.makedirs(good_path)
                self.logger.log('Training_Logs','RawDataValidation.txt','Good data directory created')

            Bad_path = os.path.join("Validated_training_data/", "BadRawData/")

            if not os.path.exists(Bad_path):
                os.makedirs(Bad_path)
                self.logger.log('Training_Logs','RawDataValidation.txt','Bad data directory created')

        except Exception as e:
            raise CustomException(e,sys)
        

    def DeleteExistingGoodDataDirectory(self):
        '''This function will delete the Existing Good Data directory
        '''


        try:
            path = "Validated_training_data/"
            if os.path.isdir(path + 'GoodRawData/'):
                shutil.rmtree(path + 'GoodRawData/')
                self.logger.log('Training_Logs','RawDataValidation.txt','Deletion of Good Directory succesfull')
        except Exception as e:
            raise CustomException(e,sys)
        
    
    def DeleteExistingBadDataDirectory(self):
        '''This function will delete the Existing Bad Data directory
        '''
        
        try:
            path = "Validated_training_data/"
            if os.path.isdir(path + 'BadRawData/'):
                shutil.rmtree(path + 'BadRawData/')
                self.logger.log('Training_Logs','RawDataValidation.txt','Deletion of Bad Directory succesfull')
        except Exception as e:
            raise CustomException(e,sys)
        

    def MoveBadDataToArchiveFolder(self):
        ''' This function will move the bad data to Archive folder
        '''
        now = datetime.datetime.now()
        date = now.date()
        time = now.strftime('%H%M%S')
        try:
            source = "Validated_training_data/BadRawData/"
            if os.path.isdir(source):
                path = 'Archivedfolder'
                if not os.path.isdir(path):
                    os.makedirs(path)
                dest = 'Archivedfolder/BadData_' + str(date)+"_"+str(time)
                if not os.path.isdir(dest):
                    os.makedirs(dest)
                files = os.listdir(source)
                for f in files:
                    shutil.move(source + f,dest)
                    self.logger.log('Training_Logs','RawDataValidation.txt','Bad data succesfully moved to Archived folder')


                path1 = "Validated_training_data/"
                if os.path.isdir(path1 + 'BadRawData/'):
                    shutil.rmtree(path1 + 'BadRawData/')
                    self.logger.log('Training_Logs','RawDataValidation.txt','Deletion of Bad Directory succesfull')
        except Exception as e:
            raise CustomException(e,sys)
        

    def validation_of_column_Numbers(self,col_nos):
        '''This function Will chech the number of column present in the new data'''

        self.DeleteExistingGoodDataDirectory()
        self.DeleteExistingBadDataDirectory()
        self.CreateGoodBadDataDirectory()
        try:
            files = [file for file in self.raw_data_directory]
            for f in files:
                pd.read_excel()
        except Exception as e:
            raise CustomException(e,sys)
        

        


        
