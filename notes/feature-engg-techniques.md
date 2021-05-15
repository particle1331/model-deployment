# Research environment: Feature engineering techniques

<br>

- [Research environment: Feature engineering techniques](#research-environment-feature-engineering-techniques)
  - [Problems with features](#problems-with-features)
  - [Feature engineering techniques](#feature-engineering-techniques)

<br>

## Problems with features

---
[Back to top](#research-environment-feature-engineering-techniques)


* **Common problems with features**

  * Missing data
  * Skewed distribution
  * Labels
  * Outliers

<br>

* **Missing data.** Affects all machine learning models. At least for scikit-learn models. Need to fill in those missing values.

<br>

* **Categorical variables.** Problems can include high cardinality (models may overfit) or rare labels (some labels exist only on the test or the train set). Or representations e.g. strings or date time variables.

<br>

* **Distributions.** Better spread of values may improve performance.

<br>

* **Outliers.** Linear models are severely degraded by outliers. Another type of model is Adaboost where tremendous weight is assigned to outliers which may result in overfitting. 

<br>

* **Scale.** This can be a numerical or optimization issue. ML models which are sensitive to scale:
  * Linear and logistic regression
  * Neural nets
  * SVM
  * KNN
  * K-means
  * LDA
  * PCA

  Meanwhile **tree-base models are insensitive to scale**, e.g. Decision Trees, RF, Gradient Boosted Trees such as XGBoost and LightGBM.

<br>

## Feature engineering techniques

---

[Back to top](#research-environment-feature-engineering-techniques)

* **Missing data imputation.** For numerical variables: mean/median imputation, arbitrary value imputation, and end of tail imputation. For categorical variables, we can have "missing" category, or we can replace with frequent categories. Other techniques include complete-case analysis, adding a "missing" indicator, and random sample imputation. 

<br>

* **Categorical encoding.** Traditional techniques: one-hot encoding, frequency encoding, label encoding. We can also encode based on monotonic relationship with target: ordered label encoding, mean encoding, weight of evidence. Alternative techniques include binary encloding and feature hashing. 

<br>

* **Rare labels.** To remedy overfitting due to high cardinality feature, we can create a "rare" label which replaces all labels which occur infrequently. 

<br>

* **Transforming distributions.** Simple transformations include logarithmic, exponential, reciprocal, Box-Cox, Yeo-Johnson transformations. Or alternatively, we can discretize our numerical variables to get a variable with better spread using unsupervised techniques like equal-width, equal-frequency, and K-means. Or we can use supervised techniques, e.g. Decision Trees trained on the variable with bins as targets to replace the values with the index of the bins.

<br>

* **Outliers**. To remove outliers we can perform discretisation, capping / censoring, or truncation. 

<br>

* **Scale.** Most common technique is standardization using mean and standard deviation to values are spread in $[-1, 1]$, or min-max scaling which scales values to be between $[0, 1]$. 

<br>

* **Datetime variables.** If we have datetime variables we can extract useful features such as day, month, year, hour, min, sec, etc. We can also compute elapsed time. Or age of the user. 

<br>

* **Text.** For text data we can consider characters, words, unique words to get an idea of the lexical diversity of the corpus. We can create Bag of Words, and TF-IDF features. 

<br>

* **Time series.** For time series we can create features such as aggregating over certain time periods, e.g. total spending in last month. We can also calculate time since last transaction.

<br>

* **Feature combination.** We can also take the sum, ration, products, etc. of features. This can improve performance of models.


