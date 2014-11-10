setwd("C:\\Users\\Richie Howell\\Documents\\R Stuffs and things\\CDMA-R")

data(iris)

#see the names of the variables
names(iris)
#see the first 6 observations
head(iris)
#see a summary of the variables
summary(iris)
#get the features and scale them
irisFeatures = iris[,1:4]
scaledIF = scale(irisFeatures)
#get the distance and use it to make a hierarchical cluster
distanceI = dist(scaledIF, method = "euclidean")
hier_clI = hclust(distanceI, method="ward.D")
#plots the dendogram

plot(hier_clI, labels=iris$Species)
#seperates into 3 clusters
rect.hclust(hier_clI, k=3)
groupsI = cutree(hier_clI, k = 3)
print(groupsI)
#in the first cluster we see mostly Setosa
#in the second cluster we see mostly virginica
#in the third cluster we see mostly versicolor


#inclass 10_2
#implements teh kmeans algorithm
kmeans_clustersI <- kmeans(distanceI, 3 , nstart=100, iter.max=100)
#extra the cluster assignment from hierarchical and kmeans
compareI <- cbind(groupsI,kmeans_clustersI$cluster)
compareI <- as.data.frame(compareI)
compareI <- cbind(iris$Species,compareI)
names(compareI) <- c("Species", "Hierarchical", "kmeans")
compareI
#there is no variation with the setosa species but we see variation with the versicolor
#and virginica species. cluster 1 is sepereated from 2 and 3, but 2 and 3 are not seperated from each other
