---
layout: single
title: "Machine Learning: Multiclass Classification Template for any Classification Dataset"
header:
  image: "https://live.staticflickr.com/65535/51237631257_b822eb6470_w.jpg"
  teaser: "https://live.staticflickr.com/65535/51237631257_b822eb6470_w.jpg"
categories:
  - machine-learning
tags:
  - Machine-learning
  - Tutorial
  - Classification
  - Multi-class Classification
  - Template
toc: true
toc_label: "Table of Contents"
toc_icon: "heart"
---


We do often use classification algorithms to predict a particular class based on provided input features. In this tutorial, we will implement a python class file that includes most of the classification methods.

## Utilities
After creating an object of the class, we will be able to do the following:
* Split train-test data
* Generate Classification Report
* Plot Classification Report
* Generate Confusion Matrix
* Save the model for future use

## Included Algorithms
*  Logistic Regression Classifier
* K-Neighbor Classifier
* SVM (Linear) Classifier
* SVM (RBF) Classifier
* Naive Bayes Classifier
* Decision Tree Classifier
* Random Forest Classifier

## Necessary Modules
We will use the following modules in our code
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import classification_report, confusion_matrix
import joblib
import os
```
* `pandas` and `numpy` $\rightarrow$ for data (in dataframe) processing
* `matplotlib` and `seaborn` $\rightarrow$ for plotting
* `sklearn.metrics` $\rightarrow$ to generate the classification reports and confusion matrices
* `joblib` and `os` $\rightarrow$ to store the models

Apart from these modules, we will also use  `sklearn.model_selection` for splitting the whole dataset to train and test-data. Also, corresponding `sklearn` submodules for importing the classifiers. We will include those while creating methods for each classifier.

## Train-test Split Function
The following function will help us to split the dataset into train-test data. We can keep it outside the class or inside the class as a static method (using the `@static` decorator beforehand).
```python
def preprocess(dataset, x_iloc_list, y_iloc, testSize):
    # dataset = pd.read_csv(csv_file)
    X = dataset.iloc[:, x_iloc_list].values 
    y = dataset.iloc[:, y_iloc].values 

    # split into training and testing set
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = testSize, random_state = 0)

    # standardization of values
    from sklearn.preprocessing import StandardScaler
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)
    return X_train, X_test, y_train, y_test
```

## Classification Class
Now let's create our class. here, I name the class as `Classification`.
### Constructor Method
We will need to provide four input arguments while creating an object of the class.
* X_Train, X_test $\rightarrow$ train and test data for target features
* y_train, y_test $\rightarrow$ train and test data for target labels
```python
class Classification:
    
    def __init__(self, X_train, X_test, y_train, y_test):
        self.X_train = X_train
        self.X_test = X_test
        self.y_train = y_train
        self.y_test = y_test
```

### Accuracy
We can use the following method to obtain accuracy from the confusion matrix.
```python
    def accuracy(self, confusion_matrix):
        sum, total = 0,0
        for i in range(len(confusion_matrix)):
            for j in range(len(confusion_matrix[0])):
                if i == j: 
                    sum += confusion_matrix[i,j]
                total += confusion_matrix[i,j]
        return sum/total
```

### Classification Report plot
The following method will be used to generate plots of the data we achieve in our classification report. We will save the plots in our local sub-directory named `clf_plots`.
```python
    def classification_report_plot(self, clf_report, filename):
        folder = "clf_plots"
        if not os.path.isdir(folder):
            os.mkdir(folder)
        
        out_file_name = folder + "/" + filename + ".png"
        
        fig=plt.figure(figsize=(16,10))
        sns.set(font_scale=4)
        sns.heatmap(pd.DataFrame(clf_report).iloc[:-1, :].T, annot=True, cmap="Greens")
        fig.savefig(out_file_name, bbox_inches="tight")
```

## Classifiers
Now, let's add individual method for each classification algorithm. Here in each method, we will
* import the classifier
* create an object of the classifier class
* fit the train data to the model
* store our model in `model` sub-directory
* predict with test data
* generate classification report
* generate confusion matrix
* cenerate classification report plot
### Linear Regression
```python
	def LR(self):
        from sklearn.linear_model import LogisticRegression
        lr_classifier = LogisticRegression()
        lr_classifier.fit(self.X_train, self.y_train)
        joblib.dump(lr_classifier, "model/lr.sav")
        y_pred = lr_classifier.predict(self.X_test)

        print("### Logistic Regression Classifier ###")
        print('Classification Report: ')
        print(classification_report(self.y_test, y_pred),'\n')
        print('Confusion Matrix: ')
        print(confusion_matrix(self.y_test, y_pred),'\n')
        print('Precision: ', self.accuracy(confusion_matrix(self.y_test, y_pred))*100,'%')

        self.classification_report_plot(classification_report(self.y_test, y_pred, \
                                                                    output_dict=True), "LR")
```

### KNN
```python
	def KNN(self):
        from sklearn.neighbors import KNeighborsClassifier
        knn_classifier = KNeighborsClassifier()
        knn_classifier.fit(self.X_train, self.y_train)
        joblib.dump(knn_classifier, "model/knn.sav")
        y_pred = knn_classifier.predict(self.X_test)
        
        print("### K-Neighbors Classifier ###")
        print('Classification Report: ')
        print(classification_report(self.y_test, y_pred),'\n')
        print('Confusion Matrix: ')
        print(confusion_matrix(self.y_test, y_pred),'\n')
        print('Precision: ', self.accuracy(confusion_matrix(self.y_test, y_pred))*100,'%')

        self.classification_report_plot(classification_report(self.y_test, y_pred, \
                                                                    output_dict=True), "KNN")
```

### SVM (Linear and RBF)
```python
    # kernel type could be 'linear' or 'rbf' (Gaussian)
    def SVM(self, kernel_type):
        from sklearn.svm import SVC
        svm_classifier = SVC(kernel = kernel_type)
        svm_classifier.fit(self.X_train, self.y_train)
        joblib.dump(svm_classifier, "model/svm.sav")
        y_pred = svm_classifier.predict(self.X_test)
        
        print("### Support Vector Classifier (" + kernel_type + ") ###")
        print('Classification Report: ')
        print(classification_report(self.y_test, y_pred),'\n')
        print('Confusion Matrix: ')
        print(confusion_matrix(self.y_test, y_pred),'\n')
        print('Precision: ', self.accuracy(confusion_matrix(self.y_test, y_pred))*100,'%')

        self.classification_report_plot(classification_report(self.y_test, y_pred, \
                                                                    output_dict=True), "SVC"+kernel_type)
```

### Naive-Bayes
```python
    def NB(self):
        from sklearn.naive_bayes import GaussianNB
        nb_classifier = GaussianNB()
        nb_classifier.fit(self.X_train, self.y_train)
        joblib.dump(nb_classifier, "model/nb.sav")
        y_pred = nb_classifier.predict(self.X_test)
        
        print("### Naive Bayes Classifier ###")
        print('Classification Report: ')
        print(classification_report(self.y_test, y_pred),'\n')
        print('Confusion Matrix: ')
        print(confusion_matrix(self.y_test, y_pred),'\n')
        print('Precision: ', self.accuracy(confusion_matrix(self.y_test, y_pred))*100,'%')

        self.classification_report_plot(classification_report(self.y_test, y_pred, \
                                                                    output_dict=True), "NB")
```

### Decision Tree
```python
    def DT(self):
        from sklearn.tree import DecisionTreeClassifier
        tree_classifier = DecisionTreeClassifier()
        tree_classifier.fit(self.X_train, self.y_train)
        joblib.dump(tree_classifier, "model/tree.sav")
        y_pred = tree_classifier.predict(self.X_test)
        
        print("### Decision Tree Classifier ###")
        print('Classification Report: ')
        print(classification_report(self.y_test, y_pred),'\n')
        print('Confusion Matrix: ')
        print(confusion_matrix(self.y_test, y_pred),'\n')
        print('Precision: ', self.accuracy(confusion_matrix(self.y_test, y_pred))*100,'%')

        self.classification_report_plot(classification_report(self.y_test, y_pred, \
                                                                    output_dict=True), "DT")
```

### Random Forest
```python
    def RF(self):
        from sklearn.ensemble import RandomForestClassifier
        rf_classifier = RandomForestClassifier(n_estimators = 10, criterion = 'entropy')
        rf_classifier.fit(self.X_train, self.y_train)
        joblib.dump(rf_classifier, "model/rf.sav")
        y_pred = rf_classifier.predict(self.X_test)
        
        print("### Random Forest Classifier ###")
        print('Classification Report: ')
        print(classification_report(self.y_test, y_pred),'\n')
        print('Confusion Matrix: ')
        print(confusion_matrix(self.y_test, y_pred),'\n')
        print('Precision: ', self.accuracy(confusion_matrix(self.y_test, y_pred))*100,'%')

        self.classification_report_plot(classification_report(self.y_test, y_pred, \
                                                                    output_dict=True), "RF")
```

The entire code is available in [Github](https://gist.github.com/shantoroy/2172937f5157998069d667b362e3fe81).

Thanks everyone! Have a nice day!!!


<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE1ODQ0ODg5MDUsMTI5MjY0NzEzMSwtMT
cwNzk0MDQyMV19
-->