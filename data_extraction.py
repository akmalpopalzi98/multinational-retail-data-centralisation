#%%
import database_utils
from database_utils import DatabaseConnector
import pandas as pd



class DataExtractor():
    def _init__(self, database_connector_instance, table_name):
        self.database_connector_instance = database_connector_instance
        self.table_name = table_name

    def read_df_tables(self):
        table_list = self.database_connector_instance.list_db_tables()
        if self.table_name in table_list:
            table = pd.read_sql_table(self.table_name, self.database_connector_instance.init_db_engine())
            return table
        else:
            return 'Table not in Database'

    


# %%
