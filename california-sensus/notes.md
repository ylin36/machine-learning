# This project provides a detailed flow of ml problem solving steps.
* These are my notes combined with california sensus example from Hands-On Machine Learning with Scikit-Learn, Keras & TensorFlow book 2nd edition.
* The notes and source code are written by me while going through the book's tutorials. 
* The dataset is provided via the book's tutorials.

## 0. Pre-req
* Install visual studio code. Install python extension
* Install anaconda
* Open anaconda cmd to install all the required modules.
  * conda install python=3.6
  * conda install -c conda-forge jupyterlab
  * conda install numpy
  * conda install pandas
  * conda install -c conda-forge matplotlib
  * conda install -c intel scikit-learn
* on vscode, ctrl+shift+p to open command pallet and run create new jupyter...

## 1. Dataset
population, median income, median housing price for each block group in California.

## 2. Model goal
predict housing price in any district

## 3. Framing the problem

### 3.1 Identifying business objective.
* Output of the model will go through another ml system with other values to determine if investiment in a given area is worth it

### 3.2 Identify current situation
* Users are manually estimating, and this is expensive.

### 3.3 Choose ml type
1. Supervised, unsupervised, or reinforcement learning? 
    * supervised since we are labeling training examples
2. Classification task, regresshion task, or something else? 
    * regression since we are predicting a value. univariate regression because we predict a single value. if we were predicting multiple values per district it would be multivariate regression.
3. Batch learning, or online learning? 
    * Batch will be chosen because there won't be a continuous flow of data. No need for rapid adjustment.

### 3.4 Selecting a performance measure
* we choose Root Mean Square Error to give an idea of how much error the system typically makes in its prediction with higher weit on large errors.

![image info](./notes-images/rmse.jpg)

* There are others for regression tasks such as Mean Absolute Error (MAE). Both are ways to measure the distance between two vectors (vector of predictions, and vector of target).
* root of sum of squares (RMS) => Euclidean norm => l2 norm (the two here is the square) => notion of distance we are familiar with
* mean absolute error => Manhattan norm => l1 norm (there are no square) => measures distance between 2 points in a city of you only travel along orthogonal city blocks.

* the norm index k is the square, cube, etc... in the (h(xi)-y(i))^k part of the equation.
* the higher the norm index, the more it focuses on large values and neglects small ones. This is why RMSE is more sensitive to outliers than MAE. 
* When outliers are rare, RMSE works very well.

### 3.5 Check the assumptions
Check with people if the assumptions are correct. For example, is the business objective correct? do we care really care about pricing for this model pipeline or should we care about another output because that's the input to another ml pipeline.

## 4. Getting start
* See Housing.jpynb for code example

## Glossary
### Pipelines
* Sequence of data processing componments.
* Components typically run asynchronously.
* Each components pulls in a large amount of data, process it, and store result in data store.
* Another component will later pull this data, process it, and store result in data store.