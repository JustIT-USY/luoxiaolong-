from sklearn.linear_model import LogisticRegression         # 逻辑回归 #
module = LogisticRegression()
module.fit(x, y)
module.score(x, y)
module.predict(test)
