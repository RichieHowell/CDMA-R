setwd("C:\\Users\\Richie Howell\\Documents\\R Stuffs and things\\CDMA-R")
#Inclass 11_1
#-----------------------
data(mtcars)
head(mtcars)
names(mtcars)
library(rpart)
?mtcars
#mpg = miles per gallon
#cyl = number of cylinders
#disp = displacement in cubic inches
#hp = gross horsepower
#drat = rear axle ratio
#wt = weight
#qsec = quarter mile time
#vs = V/s
#am = transmission with 0 being auto and 1 being manual
#gear = number of forward gears
#carb = number of carburetors
vars = c("mpg", "cyl", "disp", "hp", "drat", "wt", "qsec", "vs", "gear", "carb")
temp <- paste('am ~ ',paste(vars,collapse=' + '),sep='')
temp
tmodel <- rpart(temp,data=mtcars)
install.packages("rpart.plot")
library(rpart.plot)
prp(tmodel)
#it seems that the main factor in the transmission is the weight of the vehicle.

library(ROCR)

mtcars$pred <- predict(tmodel, newdata = mtcars)
eval <- prediction(mtcars$pred, mtcars$am)
auc_calc <- performance(eval,'auc')

auc_calc@y.values
#AUC is .90891 so we have a good AUC


#Inclass 11 part 2
#----------------------------------
#trains a knn and gets the system time and AUC
install.packages('class')
library(class)
knnTrain = mtcars[,vars]
am = mtcars$am > 0
system.time(knnDecision <- knn(knnTrain,knnTrain,am,k=200,prob=T))
#time elapsed is 0
knnPred <- ifelse(knnDecision==TRUE,
                  attributes(knnDecision)$prob,
                  1-(attributes(knnDecision)$prob))
head(knnPred)
library(ROCR)
evalKnn <- prediction(knnPred, am) #from ROCR package
auc_calcKnn <- performance(evalKnn,'auc')
auc_calc@y.values
#.9089069 AUC value

#logistic model 
f <- paste('am ~ ',paste(vars,collapse=' + '),sep='')
system.time(gmodel <- glm(as.formula(f),
                          data=knnTrain,
                          family=binomial(link='logit')))
#time elapsed is .09
log_predict <- predict(gmodel, 
                       newdata=knnTrain, 
                       type = "response")

evalLog <- prediction(log_predict, am)
auc_calcLog <- performance(evalLog,'auc')
auc_calcLog@y.values
#got an AUC of 1 for this one
#desicion tree

library(rpart)
f <- paste('am ~ ',paste(vars,collapse=' + '),sep='')
system.time(tmodel <- rpart(f,data=mtcars))
#time elapsed is 0
mtcars$pred <- predict(tmodel, newdata = mtcars)
mtcars$am <- mtcars$am > 0

#calculate AUC for CART decision tree
evalTree <- prediction(mtcars$pred, mtcars$am) 
auc_calcTree <- performance(evalTree,'auc')
auc_calcTree@y.values
#AUC is .9089 for this one

# it appears that KNN and decision tree had the same system time and AUC but 
# logistic model had a longer time and a better AUC


#Inclass 11 part 3
#-----------------------------

install.packages("e1071")
library(e1071)


system.time(fit <- naiveBayes(as.formula(f), data=mtcars))
#elapsed time is .14, longer than other models
system.time(naivB_pred <- predict(fit, mtcars, type = 'raw'))
#elapsed time is .02
evalB <- prediction(naivB_pred[,2], mtcars$am) 
auc_calcB <- performance(evalB,'auc')
auc_calcB@y.values
#AUC is .984
#Bayes alogorithm took longer than the other models, had a worse AUC then the
#logistical model but a better AUC then the other 2 models.