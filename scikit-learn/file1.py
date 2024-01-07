#from sklearn import KFold
#from sklearn import Pipeline
#from sklearn.preprocessing import StandardScaler

from sklearn import datasets
from sklearn.model_selection 

iris = datasets.load_iris()
X = iris.data[:,2:]
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X,y,stratify=y, random_state=7)





