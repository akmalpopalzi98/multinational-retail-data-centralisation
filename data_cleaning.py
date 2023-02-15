#%%

import pandas as pd
from dateutil import parser
#%%
def has_numbers(inputString):
    return any(char.isdigit() for char in inputString)



import datetime
def validate(date_text):
        try:
            if datetime.date.fromisoformat(date_text):
                  return True
        except ValueError:
              return date_text
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
        date_format_errors = []
        for item in self.dataframe.date_payment_confirmed:
             if validate(item):
                  pass
             else:
                  date_format_errors.append(item)

        clean_date_format = remove_date_error.copy()
        for item in date_format_errors:
             clean_date_format.drop(clean_date_format.loc[clean_date_format['date_payment_confirmed']==item].index, inplace=True)

        return clean_date_format
    
    
             

        

        
        








