
import sys

import numpy as np
from sklearn.ensemble import RandomForestClassifier

class TitanicModeling:
    def __init__(self):
        pass

    def run_sklearn_modeling(self, X, y, n_estimator):
        """
        Run the modeling process using the sklearn RandomForestClassifier.

        Parameters:
            X (array-like or sparse matrix): The feature matrix.
            y (array-like): The target labels.
            n_estimator (int): The number of estimators (decision trees) in the random forest.

        Returns:
            dict: A dictionary containing the model information, including the model score and parameters.
        """
        model = self._get_rf_model(n_estimator)

        model.fit(X, y)

        model_info = {
            'score' : {
                'model_score' : model.score(X,y)
            },
            'params' : model.get_params()
        }

        return model_info

    def _get_rf_model(self, n_estimator):
        """
        Create a random forest classifier model.

        Parameters:
            n_estimator (int): The number of estimators (decision trees) in the random forest.

        Returns:
            RandomForestClassifier: A random forest classifier model.
        """
        return RandomForestClassifier(n_estimators=n_estimator, max_depth=3)
