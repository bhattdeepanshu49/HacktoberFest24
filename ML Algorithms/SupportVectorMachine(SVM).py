from inspect import classify_class_attrs
import numpy as np
import pandas as pd
import warnings
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report

warnings.filterwarnings("ignore")
mobile_data = pd.read_csv("mobiledata.csv")

# the target that the model need to predict
target = ["purchases_mobile"]

# encode data using one-hot encoding
mobile_data_encoded = pd.get_dummies(mobile_data.drop(target, axis=1)).astype(int)

print(f"mobile data encoded is: {mobile_data_encoded}")
mobile_target = mobile_data[target].replace({'yes': 1, 'no': 0})

# features excluding target
features = mobile_data_encoded.columns

# split data into training and testing sets
# test split is 15% of original data
X_train, X_test, y_train, y_test = train_test_split(mobile_data_encoded, mobile_target, test_size=0.15, random_state=100)

# train model
model = SVC()
model.fit(X_train, y_train)

# evaluate model
print(model.score(X_test, y_test))

# show model classification report
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))
