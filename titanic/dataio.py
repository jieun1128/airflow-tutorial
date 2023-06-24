
import pandas as pd

class DataIOStream:

    def get_data(self, path, f_name, flag=False):
        """
        Load data from a CSV file.

        Parameters:
            path (str): The path to the directory containing the CSV file.
            f_name (str): The name of the CSV file (without the file extension).
            flag (bool, optional): A flag indicating whether to include the path in the file name. 
                                   Defaults to False.

        Returns:
            pandas.DataFrame: The loaded data as a pandas DataFrame.
        """
        if flag:
            return pd.read_csv(f'{f_name}.csv')
        return pd.read_csv(f'{path}/{f_name}.csv')

    def get_X_y(self, data):
        """
        Split data into features (X) and labels (y).

        Parameters:
            data (pandas.DataFrame): The input data containing both features and labels.

        Returns:
            tuple: A tuple (X, y) containing the features (X) and labels (y).
        """
        X = data[data.columns[1:]]
        X = X[['Sex', 'Age_band', 'Pclass']]
        y = data['Survived']

        return X, y
    
