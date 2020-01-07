import numpy as np
import pandas as pd
from collections import defaultdict

from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder

import DT
import ReplaceMissingTransformer

class Model(object):

  def __init__(self, df):
    self.df = df

  def process(self):
    imp = SimpleImputer(missing_values=np.nan, strategy='constant')
    df_repl = imp.fit_transform(self.df)
    df_zeros = np.where(df_repl != 'missing_value', df_repl, 0.0)

    df = pd.DataFrame(data=df_zeros)
    d = defaultdict(LabelEncoder)
    fit = df.apply(lambda x: d[x.name].fit_transform(x))

    #df_enc = LabelEncoder().fit_transform(df)
    #df_enc = enc.fit_transform(df)
    print(fit)