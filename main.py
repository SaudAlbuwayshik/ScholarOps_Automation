# main.py

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load dataset
data = pd.read_csv('data/scholarship_specialization_data.csv')

# Preview data
print("\nSample data:")
print(data.head())

# Encode categorical variables
data_encoded = pd.get_dummies(data.drop('Recommended_Scholarship_Specialization', axis=1))
y = data['Recommended_Scholarship_Specialization']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(data_encoded, y, test_size=0.3, random_state=42)

# Model
model = DecisionTreeClassifier(max_depth=5, random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# Evaluation
print("\nClassification Report:")
print(classification_report(y_test, y_pred))
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# Visualization
os.makedirs('outputs', exist_ok=True)
plt.figure(figsize=(20,10))
plot_tree(model, feature_names=X_train.columns, class_names=np.unique(y).astype(str), filled=True)
plt.title('Scholarship Specialization Decision Tree')
plt.savefig('outputs/decision_tree.png')
plt.show()
