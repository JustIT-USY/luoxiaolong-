from sklearn.naive_bayes import GaussianNB            #朴素贝叶斯分类器#
module = GaussianNB()
module.fit(x, y)
predicted = module.predict(test)
