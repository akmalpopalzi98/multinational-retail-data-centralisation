#%%
import pandas as pd
import tabula as tb
import json
import requests




class DataExtractor():
    def __init__(self, database_connector_instance = None, table_name = None):
        self.database_connector_instance = database_connector_instance
        self.table_name = table_name

    def read_df_tables(self):
        table_list = self.database_connector_instance.list_db_tables()
        if self.table_name in table_list:
            table = pd.read_sql_table(self.table_name, self.database_connector_instance.init_db_engine())
            return table
        else:
            return 'Table not in Database'


    def retrieve_pdf_data(self,link):
        pdf_data = tb.read_pdf(link,pages = 'all')
        df_pdf = pd.concat(pdf_data)
        return df_pdf
    

    def list_number_of_stores(self,endpoint,dictionary):
        r = requests.get(endpoint,headers = dictionary)
        output = r.json()
        return output['number_stores']
    

    def retrieve_stores_data(self,endpoint2):
        #incompelete
        pass



        






    


# %%
