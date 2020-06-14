import pandas as pd

from ml.preprocessing.normalization import Normalizer
from util import wrap_text


class Preprocessing:
    """
    Class to perform data preprocessing before training
    """

    def clean_data(self, df: pd.DataFrame):
        """
        Perform data cleansing.
        
        Parameters
        ----------            
        df  :   pd.Dataframe
                Dataframe to be processed

        Returns
    	-------
        pd.Dataframe
            Cleaned Data Frame
        """
        print("Cleaning data")
        df['Pclass'] = "0"
        df['Pclass'] = df.Pclass.astype('object')

        return df

    def categ_encoding(self, df: pd.DataFrame):
        """
        Perform encoding of the categorical variables

        Parameters
        ----------            
        df  :   pd.Dataframe
                Dataframe to be processed

        Returns
    	-------
        pd.Dataframe
            Cleaned Data Frame
        """
        print("Category encoding")
        df_copy = df.copy()
        df_copy = pd.get_dummies(df_copy)
        return df_copy
