from sklearn.ensemble import GradientBoostingClassifier      #Gradient Boosting 和 AdaBoost算法#
from sklearn.ensemble import GradientBoostingRegressor
module = GradientBoostingClassifier(n_estimators=100, learning_rate=0.1, max_depth=1, random_state=0)
module.fit(x, y)
module.predict(test)
