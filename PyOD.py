# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.13.1
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% [markdown]
# # PyOD: a Unified Python Library for Anomaly Detection
# ### The scikit-learn for outlier detection machine learning tasks
#
# from [towards data science](https://towardsdatascience.com/pyod-a-unified-python-library-for-anomaly-detection-3608ec1fe321 "Original Article") by [Alexandra Amidon](https://alexandra-amidon.medium.com "Alexandra Amidon on medium.com")

# %%
from pyod.utils.data import generate_data
import numpy as np

import matplotlib.pyplot as plt

# %%
#     behaviour : str, default='old'
#         Behaviour of the returned datasets which can be either 'old' or
#         'new'. Passing ``behaviour='new'`` returns
#         "X_train, y_train, X_test, y_test", while passing ``behaviour='old'``
#         returns "X_train, X_test, y_train, y_test".

# %%
X_train, X_test, y_train, y_test = \
    generate_data(n_train=200,
                 n_test=100,
                 n_features=5,
                 contamination=0.1,
                 random_state=3,
                 behaviour = 'new')
X_train = X_train * np.random.uniform(0, 1, size=X_train.shape)
X_test = X_test * np.random.uniform(0, 1, size=X_test.shape)

# %%
from pyod.models.abod import ABOD
clf_name = 'ABOD'
clf = ABOD()
clf.fit(X_train)
test_scores = clf.decision_function(X_test)

# %%
from pyod.utils.utility import precision_n_scores
from sklearn.metrics import roc_auc_score
roc = round(roc_auc_score(y_test, test_scores), ndigits=4)
prn = round(precision_n_scores(y_test, test_scores), ndigits=4)
print(f'{clf_name} ROC:{roc}, precision @ rank n:{prn}')


# %%
from sklearn.metrics import roc_curve
fpr, tpr, _ = roc_curve(y_test, test_scores)
plt.plot(fpr, tpr)

# %%
X = range(len(y_test))
fig, ax = plt.subplots(figsize=(15,5))
# ax.scatter(X,y_test, color='orange')
# ax2 = ax.twinx()
# ax2.scatter(X,test_scores)

ax.scatter(test_scores, y_test)
plt.show()

# %%
test_scores

# %%
from pyod.models.copod import COPOD
clf_name = 'COPOD'
clf = COPOD()
clf.fit(X_train)
test_scores = clf.decision_function(X_test)

# %%
from pyod.utils.utility import precision_n_scores
from sklearn.metrics import roc_auc_score
roc = round(roc_auc_score(y_test, test_scores), ndigits=4)
prn = round(precision_n_scores(y_test, test_scores), ndigits=4)
print(f'{clf_name} ROC:{roc}, precision @ rank n:{prn}')

# %%
