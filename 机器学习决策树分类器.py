from sklearn import tree                              #决策树分类器#
module = tree.DecisionTreeClassifier(criterion='gini')
module.fit(x, y)
module.score(x, y)
module.predict(test)
