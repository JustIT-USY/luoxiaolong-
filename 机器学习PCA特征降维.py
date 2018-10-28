from sklearn.decomposition import PCA              #PCA特征降维#
train_reduced = PCA.fit_transform(train)
test_reduced = PCA.transform(test)
