from sklearn.cluster import KMeans                    #kmeans聚类#
module = KMeans(n_clusters=3, random_state=0)
module.fit(x, y)
module.predict(test)
