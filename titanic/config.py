import os
import pathlib

class PathConfig:
    def __init__(self):
        self.project_path = pathlib.Path(__file__).parent.parent.resolve()
        self.titanic_path = f"{self.project_path}/data/titanic"

class EnvConfig:
    def get_gender_mapping_code(self):
        """
        Get the mapping dictionary for gender codes.

        Returns:
            dict: A dictionary mapping gender values to their corresponding codes.
                Example: {'male': 0, 'female': 1}
        """
        gender_mapping_info = {
            'male' : 0,
            'female' : 1,
        }

        return gender_mapping_info
    
    def get_column_list(self):
        """
        Get the list of column names.

        Returns:
            list: A list of column names.
                Example: ['Sex', 'Age_band', 'Pclass']
        """
        columns_list = ['Sex', 'Age_band', 'Pclass']
        return columns_list

