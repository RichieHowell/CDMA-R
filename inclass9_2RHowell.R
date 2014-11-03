setwd("C:\\Users\\Richie Howell\\Documents\\R Stuffs and things\\CDMA-R")

load("fdata.rData")
head(final)
#create training and test sets
final$gp = runif(dim(final)[1])
testSet = subset(final, final$gp <= .1)
trainset = subset(final, final$gp > .1)
#fit the linear regression model
attach(trainset)
finalFit = lm(ssc ~ coder + location + age + gender + ethnicity + 
                som1 + som2 + som3 + som4 + som4 + som6 + som7 + som8 + 
                som9 + som10 + som11 + som12 + som13 + som14)
install.packages("MASS")
library(MASS)
finalStep = stepAIC(finalFit, direction = "both")
finalStep
#fit the data using the new formula
finalFit2 = lm(ssc ~ coder + location + som1 + som2 + som3 + som4 + 
                 som10 + som11 + som12 + som13 + som14)
summary(finalFit2)
#predict the values
testSet$sscpred = predict(finalFit2, newdata = testSet)
library(ggplot2)
ggplot(data = testSet, aes(x = sscpred, y = ssc)) +
  geom_point(color = "red")+
  geom_line(aes(x = ssc, y = ssc), color = "blue")
#does not seem to predict them very well, we wanted to see dots around the line but instead we see
#dots scattered everywhere with a large amount missing towards the middle of data