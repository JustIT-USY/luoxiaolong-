from sklearn.neighbors import KNeighborsClassifier     #K近邻#
from sklearn.neighbors import KNeighborsRegressor
module = KNeighborsClassifier(n_neighbors=6)
module.fit(x, y)
predicted = module.predict(test)
predicted = module.predict_proba(test)
