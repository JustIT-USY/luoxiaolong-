from sklearn import svm                                #支持向量机#
module = svm.SVC()
module.fit(x, y)
module.score(x, y)
module.predict(test)
module.predict_proba(test)
