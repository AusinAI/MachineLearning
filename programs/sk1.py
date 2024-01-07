from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier


X = [[10,20],[20,40]]
Y = [3,2]

reg = linear_model.BayesianRidge()
reg.fit(X,Y)

print(reg.predict([[30,60]]))
print(reg.coef_)

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2, random_state=42)


model = DecisionTreeClassifier()
model.fit(X_train,y_train)

predictions = model.predict(X_test)

print("Predictions: ",prediction)


print(X_train.shape)
print(y_train.shape)

print(X_test.shape)
print(y_test.shape)

        





