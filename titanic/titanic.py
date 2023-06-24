
import pandas as pd

from titanic.preprocess import TitanicPreprocess
from titanic.config import PathConfig
from titanic.dataio import DataIOStream
from titanic.model import TitanicModeling

class TitanicMain(TitanicPreprocess, PathConfig, TitanicModeling, DataIOStream):
    def __init__(self):
        TitanicPreprocess.__init__(self)
        PathConfig.__init__(self)
        TitanicModeling.__init__(self)
        DataIOStream.__init__(self)

    def prepro_data(self, f_name, **kwargs):
        """
        Perform data preprocessing and save the preprocessed data.

        Parameters:
            f_name (str): The name of the input data file.
            **kwargs: Additional keyword arguments.

        Returns:
            str: A message indicating the end of the preprocessing.
        """
        data = self.get_data(self.titanic_path, f_name)
        data = self.run_preprocessing(data)
        data.to_csv(f"{self.titanic_path}/prepro_titanic.csv", index=False)
        kwargs['task_instance'].xcom_push(key='prepro_csv', value=f"{self.titanic_path}/prepro_titanic")
        return "end prepro"
    
    def run_modeling(self, n_estimator, flag, **kwargs):
        """
        Run the modeling process using the preprocessed data.

        Parameters:
            n_estimator (int): The number of estimators for the random forest model.
            flag (bool): A flag indicating whether to load preprocessed data from a file.
            **kwargs: Additional keyword arguments.

        Returns:
            str: A message indicating the end of the modeling process.
        """
        f_name = kwargs["task_instance"].xcom_pull(key='prepro_csv')
        data = self.get_data(self.titanic_path, f_name, flag)
        X, y = self.get_X_y(data)
        model_info = self.run_sklearn_modeling(X, y, n_estimator)
        kwargs['task_instance'].xcom_push(key='result_msg', value=model_info)
        return "end modeling"
    
    

