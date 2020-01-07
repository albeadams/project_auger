import numpy as np
from sklearn.base import TransformerMixin

#http://zacstewart.com/2014/08/05/pipelines-of-featureunions-of-pipelines.html
class ReplaceMissingTransformer(TransformerMixin):

    def transform(self, X, **transform_params):
        df = np.where(X != 'missing_value', X, 0.0)
        return df

    def fit(self, X, y=None, **fit_params):
        return self
