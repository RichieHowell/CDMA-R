setwd("C:\\Users\\Andrew\\Downloads")
#get the data from the pandas data frame export

projectData = read.csv('ProjectDF.csv')

#needed libraries
library(rpart)
library(ROCR)
library(gplots)

#turn out mpg high way varaible into whether or not it si below the mean(bad MPG) or above the mean(good mpg)
projectData$MPG.highway = findInterval(projectData$MPG.highway, c(29))

#set the variables to test upon
vars = c("Cylinders", "Horsepower", "RPM", "Rev.per.mile", "Price", "Weight", "EngineSize")
temp <- paste('MPG.highway ~ ',paste(vars,collapse=' + '),sep='')

#train the model
tmodel <- rpart(temp,data=projectData)

#get the predictions
projectData$pred <- predict(tmodel, newdata = projectData)

#see how our predictions did
eval <- prediction(projectData$pred, projectData$MPG.highway)
auc_calc <- performance(eval,'auc')

auc_calc@y.values
#AUC value is .96, which is close to 1 so the prediction model is good

