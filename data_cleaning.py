#%%
import data_extraction,database_utils
from data_extraction import DataExtractor
from database_utils import DatabaseConnector
import pandas as pd
from dateutil import parser
#%%
def has_numbers(inputString):
    return any(char.isdigit() for char in inputString)
#%%
class DataCleaning():
    def __init__(self,dataframe):
        self.dataframe = dataframe


    def clean_user_data(self):
        clean_1_no_null = self.dataframe[self.dataframe.country_code != 'NULL']
        messy_first_names = []
        for item in clean_1_no_null.first_name:
            if has_numbers(item):
                messy_first_names.append(item)
        clean_2_users = clean_1_no_null[~clean_1_no_null.first_name.isin(messy_first_names)]
        clean_3_country_code = clean_2_users.replace('GGB','GB')
        cleaned_data = clean_3_country_code
        return cleaned_data

    
    def clean_card_data(self):
        remove_null = self.dataframe[self.dataframe.card_number != 'NULL']
        date_errors = []
        for item in remove_null.expiry_date:
            if item.isalpha():
                date_errors.append(item)
        remove_date_error = remove_null.copy()
        for item in date_errors:
            remove_date_error.drop(remove_date_error.loc[remove_date_error['expiry_date']==item].index, inplace=True)

        
        








