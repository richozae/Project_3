# -*- coding: utf-8 -*-
"""ECommerce_Delivery.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Ape6lZt9jREGz0Rkk7wxliWapBWuGfJ5

Richo
Fresh Graduated from Shipbuilding Institute of Polytechnic Surabaya
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from google.colab import drive

drive.mount('/content/drive')
df = pd.read_csv('/content/drive/My Drive/Colab Notebooks/progresproject/posting/ECommerce_Delivery.csv')

#print df value for the next information
print(df)

#cheking dataset for raw and columns
df.shape

df.head()

df.tail()

df.info()

df.isna().sum()

df.isna()

df.drop(['ID'], axis=1, inplace=True)

df.duplicated().sum()

df.describe()

"""# EDA (Exploratory Data Analysis)
to understand the correspondence between variables as a further step in the variable analysis process
"""

plt.pie(df['Gender'].value_counts(),labels = ['F','M'], autopct='%1.1f%%', startangle=90)
plt.title('Gender Distribution')

"""# Product Properties"""

fig, ax = plt.subplots(1,3,figsize=(15,5))
sns.histplot(df['Weight_in_gms'], ax=ax[0], kde=True).set_title('Weight Distribution')
sns.countplot(x = 'Product_importance', data = df, ax=ax[1]).set_title('Product Importance')
sns.histplot(df['Cost_of_the_Product'], ax=ax[2], kde=True).set_title('Cost of the Product')

"""In the first graph, it can be observed that products with weights between 1000-2000 grams and 4000-6000 grams have a higher quantity compared to the range of 3000-4000 grams. In the second graph, the importance of low-type products shows the highest figure. In the third graph, there is a significant increase in the distribution at the $225-275 range.

-

# Logistic
"""

fig, ax = plt.subplots(1,3,figsize=(15,5))
sns.countplot(x = 'Warehouse_block', data = df, ax=ax[0]).set_title('Warehouse Block')
sns.countplot(x = 'Mode_of_Shipment', data = df, ax=ax[1]).set_title('Mode of Shipment')
sns.countplot(x = 'Reached.on.Time_Y.N', data = df, ax=ax[2]).set_title('Reached on Time')

"""In graph 1, the quantity of products in warehouse F is the highest, while in other warehouses, the quantity of products is nearly the same. In graph 2, it shows that product shipments via water or ship transportation are the largest, with a figure exceeding 7000 products. In graph 3, it indicates that untimely deliveries are higher compared to on-time deliveries.

-

# Customer Eksperience
"""

fig, ax = plt.subplots(2,2,figsize=(15,10))
sns.countplot(x = 'Customer_care_calls', data = df, ax=ax[0,0]).set_title('Customer Care Calls')
sns.countplot(x = 'Customer_rating', data = df, ax=ax[0,1]).set_title('Customer Rating')
sns.countplot(x = 'Prior_purchases', data = df, ax=ax[1,0]).set_title('Prior Purchases')
sns.histplot(x = 'Discount_offered', data = df, ax=ax[1,1], kde = True).set_title('Discount Offered')

"""In the customer_care_calls graph, the majority of customers have made 3-4 calls, which could be a potential indicator that customers might be facing delivery issues.

In the second graph, we can see that the number of customer ratings at all levels is the same, but there are more ratings of 1 and 3, indicating that customers are not satisfied with the service.

In the third graph, the highest value indicates that customers have made 2-3 previous purchases, which means that customers who have made previous purchases are satisfied with the service.

In the fourth graph, most products have a dominant discount range of 0-10%.

# Customer Gender and Product Delivery
"""

sns.countplot(x = 'Gender', data = df, hue = 'Reached.on.Time_Y.N').set_title('Gender vs Reached on Time')

"""The number of products delivered on time for both genders is the same, indicating that there is no relationship between customer gender and product delivery.

# Product Properties and Product Delivery
"""

fig, ax = plt.subplots(1,3,figsize=(15,5))
sns.violinplot(y = df['Weight_in_gms'], ax=ax[0], kde=True, x = df['Reached.on.Time_Y.N']).set_title('Weight Distribution')
sns.countplot(x = 'Product_importance', data = df, ax=ax[1], hue = 'Reached.on.Time_Y.N').set_title('Product Importance')
sns.violinplot(y = df['Cost_of_the_Product'], ax=ax[2], kde=True, x = df['Reached.on.Time_Y.N']).set_title

"""In Figure 1, products weighing more than 4500 grams are not delivered on time, and furthermore, there are more products with weights between 2500 - 3500 grams that are delivered on time.

In Figure 2, there is no significant difference in product delivery based on product priority.

In Figure 3, it is observed that products priced higher than 250 have a higher number of instances of not being delivered on time.

# Logistic and Product Delivery
"""

fig, ax = plt.subplots(1,2,figsize=(15,5))
sns.countplot(x = 'Warehouse_block', data = df, ax=ax[0], hue = 'Reached.on.Time_Y.N').set_title('Warehouse Block')
sns.countplot(x = 'Mode_of_Shipment', data = df, ax=ax[1], hue = 'Reached.on.Time_Y.N').set_title('Mode of Ship')

"""This graph illustrates the relationship between logistics and on-time product delivery. Since the majority of products are shipped from Warehouse F, I assume that Warehouse F is located near the port, and most products are transported by ship. In both graphs, the difference between the number of products delivered on time and those not delivered on time remains constant across warehouse blocks and shipping methods. This means that logistics and shipping methods do not impact product delivery.

# Customer Experience and Product Delivery
"""

fig, ax = plt.subplots(2,2,figsize=(15,10))
sns.countplot(x = 'Customer_care_calls', data = df, ax=ax[0,0],hue = 'Reached.on.Time_Y.N').set_title('Customer Care Calls')
sns.countplot(x = 'Customer_rating', data = df, ax=ax[0,1],hue = 'Reached.on.Time_Y.N').set_title('Customer Rating')
sns.countplot(x = 'Prior_purchases', data = df, ax=ax[1,0],hue = 'Reached.on.Time_Y.N').set_title('Prior Purchases')
sns.violinplot(x = 'Reached.on.Time_Y.N', y = 'Discount_offered' ,data = df, ax=ax[1,1]).set_title('Discount O')

"""The first graph is about customer service calls and product delivery. In this graph, we can observe that the difference between on-time and delayed product deliveries decreases as the number of customer calls increases. This suggests that with delayed product deliveries, customers become concerned about their orders and contact customer service.

The second graph is about customer ratings and product delivery. Here, we can see that customers who provide ratings tend to have a higher number of on-time product deliveries.

The third graph is related to previous customer purchases, indicating that customers who have made more prior purchases tend to receive more on-time product deliveries. This is likely why they continue to buy from the company.

The fourth graph concerns discounts offered on products and product delivery. In this graph, we can observe that products with a discount of 0-10% have a higher number of delayed deliveries, whereas products with discounts exceeding 10% tend to have more on-time deliveries.

# DATA PREPROCESSING 2
Label Encoding the Categorical Variables
"""

from sklearn.preprocessing import LabelEncoder

#Label encoding object
le = LabelEncoder()

#columns for label encoding
cols = ['Warehouse_block','Mode_of_Shipment','Product_importance', 'Gender']

#label encoding
for i in cols:
    le.fit(df[i])
    df[i] = le.transform(df[i])
    print(i, df[i].unique())

plt.figure(figsize=(10,10))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')

"""can see that there is positive correlation between cost of product and number of customer care calls."""

sns.violinplot(x = 'Customer_care_calls', y = 'Cost_of_the_Product', data = df)

"""# TRAIN AND TEST SPLIT"""

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(df.drop('Reached.on.Time_Y.N', axis=1), df['Reached.on.Time_Y.N'], test_size=0.2, random_state=0)

"""# Random Forest Classifier"""

from sklearn.ensemble import RandomForestClassifier

#Random Forest Classifier Object
rfc = RandomForestClassifier()

#Using GridSearchCV for hyperparameter tuning
from sklearn.model_selection import GridSearchCV

#Parameter grid
param_grid = {
    'max_depth': [4,8,12,16],
    'min_samples_leaf': [2,4,6,8],
    'min_samples_split': [2,4,6,8],
    'criterion': ['gini', 'entropy'],
    'random_state': [0,42]
}

#GridSearchCV object
grid = GridSearchCV(estimator=rfc, param_grid=param_grid, cv=5, n_jobs=-1, verbose=2, scoring='accuracy')

#Fitting the model
grid.fit(X_train, y_train)

#Best parameters
print('Best parameters: ', grid.best_params_)

#Random Forest Classifier Object
rfc = RandomForestClassifier(criterion='gini', max_depth=8, min_samples_leaf=8, min_samples_split=2, random_state=42)

#Fitting the model
rfc.fit(X_train, y_train)

#Training accuracy
print('Training accuracy: ', rfc.score(X_train, y_train))

#predicting the test set results
rfc_pred = rfc.predict(X_test)

"""# Decision Tree Classifier"""

from sklearn.tree import DecisionTreeClassifier

#Decision Tree Classifier Object
dtc = DecisionTreeClassifier()

#Using GridSearchCV for hyperparameter tuning
from sklearn.model_selection import GridSearchCV
#Parameter grid
param_grid = {
    'max_depth': [2,4,6,8],
    'min_samples_leaf': [2,4,6,8],
    'min_samples_split': [2,4,6,8],
    'criterion': ['gini', 'entropy'],
    'random_state': [0,42]}

#GridSearchCV object
grid = GridSearchCV(estimator=dtc, param_grid=param_grid, cv=5, n_jobs=-1, verbose=2, scoring='accuracy')

#Fitting the model
grid.fit(X_train, y_train)

#Best parameters
print('Best parameters: ', grid.best_params_)

#Decision Tree Classifier Object
dtc = DecisionTreeClassifier(criterion='gini', max_depth=6, min_samples_leaf=6, min_samples_split=2, random_state=0, class_weight='balanced')

#Fitting the model
dtc.fit(X_train, y_train)

#Training accuracy
print('Training accuracy: ', dtc.score(X_train, y_train))

#predicting the test set results
dtc_pred = dtc.predict(X_test)

"""# Logistic Regressor"""

from sklearn.linear_model import LogisticRegression

#Logistic Regression Object
lr = LogisticRegression()

#fitting the model
lr.fit(X_train, y_train)

#Training accuracy
lr.score(X_train, y_train)

#predicting the test set results
lr_pred = lr.predict(X_test)

"""# K Nearest Neighbors"""

from sklearn.neighbors import KNeighborsClassifier

#KNN Classifier Object
knn = KNeighborsClassifier()

#fitting the model
knn.fit(X_train, y_train)

#training accuracy
knn.score(X_train, y_train)

#predicting the test set results
knn_pred = knn.predict(X_test)

"""# Model Evaluation"""

from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, mean_absolute_error, r2_score, mean_squared_error

fig, ax = plt.subplots(2,2,figsize=(15,10))
sns.heatmap(confusion_matrix(y_test, rfc_pred), annot=True, cmap='coolwarm', ax=ax[0,0]).set_title('Random Forest Classifier')
sns.heatmap(confusion_matrix(y_test, dtc_pred), annot=True, cmap='coolwarm', ax=ax[0,1]).set_title('Decision Tree Classifier')
sns.heatmap(confusion_matrix(y_test, lr_pred), annot=True, cmap='coolwarm', ax=ax[1,0]).set_title('Logistic Regression')
sns.heatmap(confusion_matrix(y_test, knn_pred), annot=True, cmap='coolwarm', ax=ax[1,1]).set_title('KNN Classifier')

#classification report
print('Random Forest Classifier: \n', classification_report(y_test, rfc_pred))
print('Decision Tree Classifier: \n', classification_report(y_test, dtc_pred))
print('Logistic Regression: \n', classification_report(y_test, lr_pred))
print('KNN Classifier: \n', classification_report(y_test, knn_pred))

"""# Model Comparison"""

models = ['Random Forest Classifier', 'Decision Tree Classifier', 'Logistic Regression', 'KNN Classifier']
accuracy = [accuracy_score(y_test, rfc_pred), accuracy_score(y_test, dtc_pred), accuracy_score(y_test, lr_pred), accuracy_score(y_test, knn_pred)]
sns.barplot(x=models, y=accuracy, palette='magma').set_title('Model Comparison')
plt.xticks(rotation=90)
plt.ylabel('Accuracy')

plt.figure(figsize=(8, 6))
plt.pie(accuracy, labels=models, autopct='%1.1f%%', startangle=140)
plt.title('Accuracy Comparison')
plt.axis('equal')

plt.show()

"""# Evaluation and Conclusion
The aim of this project is to predict whether products from the e-commerce company will arrive on time or not, while also analyzing the factors influencing product delivery and understanding customer behavior. Through data exploration, it was discovered that both product weight and price significantly impact the success of product deliveries. Products weighing between 2500 - 3500 grams and priced under $250 tend to have a higher likelihood of on-time deliveries. Furthermore, the majority of products are shipped from Warehouse F via ships, suggesting that Warehouse F is likely located near the port.

Customer behavior also plays a role in predicting on-time deliveries. The more frequently customers contact customer service, the higher the likelihood of delivery delays. Interestingly, customers who have made more previous purchases tend to receive more on-time deliveries, which may be a reason why they continue to shop with the company. Products with discounts of 0-10% tend to have a higher number of delayed deliveries, whereas products with discounts exceeding 10% tend to have more on-time deliveries.

In terms of machine learning models, the decision tree classifier has the highest accuracy among the models, reaching 69%. Random forest classifier and K Nearest Neighbors classifiers have accuracies of 68% and 65% respectively. Logistic regression is the model with the lowest accuracy, which is 63%.

Based on the model's learning accuracy, the highest accuracy was achieved by the Decision Tree model, with a pie chart percentage reaching 25.8%.
"""