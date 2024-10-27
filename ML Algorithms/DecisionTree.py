from re import X
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
import warnings
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import plot_tree

warnings.filterwarnings("ignore")
mobile_data = pd.read_csv("mobiledata.csv")

# the target that the model need to predict
target = ["purchases_mobile"]

# encode data using one-hot encoding
mobile_data_encoded = pd.get_dummies(mobile_data.drop(target, axis=1)).astype(int)

print(f"mobile data encoded is: {mobile_data_encoded}")
mobile_target = mobile_data[target]

# features excluding target
features = mobile_data_encoded.columns

# split data into training and testing sets
# test split is 15% of original data
X_train, X_test, y_train, y_test = train_test_split(mobile_data_encoded, mobile_target, test_size=0.15, random_state=100)

# train model
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# evaluate model
print(model.score(X_test, y_test))

# visualize tree
plt.figure(figsize=(20,10))
plot_tree(model,
          feature_names=features,
          class_names = [str(c) for c in model.classes_],
          filled=True,
          rounded=True,
          fontsize=10)
plt.show()
