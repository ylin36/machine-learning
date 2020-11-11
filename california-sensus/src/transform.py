from sklearn.base import BaseEstimator, TransformerMixin
import numpy as np

rooms_ix, bedrooms_ix, population_ix, household_ix = 3, 4, 5, 6

# Example of writing customized transformer to do tasks such as custom cleanup operations or combining specific attributes
# Scikit-Learn replies on duck typing not inheritance. All we need to do is create a class and implement 
# fit()(returning self), 
# transform(), 
# fit_transform() => get this one free by adding TransformerMixin as a base class
# if you add BaseEstimator as a base class (avoid *args and **kargs in constructor), you will also get two extra methods => get_params() set_params()
# that will be useful for automatic hyperparameter tuning

class CombinedAttributesAdder(BaseEstimator, TransformerMixin):
    def __init__(self, add_bedrooms_per_room=True): # no args or **kargs
        self.add_bedrooms_per_room = add_bedrooms_per_room
    def fit(self, X, y=None):
        return self # nothing else to do
    def transform(self, X):
        rooms_per_household = X[:, rooms_ix] / X[:, household_ix] # all rows of room_ix column / all rows of household_ix column 0 indexed.
        population_per_household = X[:, population_ix] / X[:, household_ix]
        if self.add_bedrooms_per_room:
            bedrooms_per_room = X[:, bedrooms_ix] / X[:, rooms_ix]
            return np.c_[X, rooms_per_household, population_per_household, bedrooms_per_room]
        else:
            return np.c_[X, rooms_per_household, population_per_household]