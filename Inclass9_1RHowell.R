setwd("C:\\Users\\Richie Howell\\Documents\\R Stuffs and things\\CDMA-R")

load("fdata.rData")
head(final)
#using SOM1-5
attach(final)
firstFive = glm(disorder ~ som1+som2+som3+som4+som5, data = final,
                family = "binomial")
summary(firstFive)
#it seems that only som2 has a high p value for this set
exp(firstFive$coef)
#it looks like the odds are 68% better that you have the disorder if you have som1
#repeat for som6-9
secFour = glm(disorder ~ som6+som7+som8+som9, data = final,
                family = "binomial")
summary(secFour)
#it seems in this set som8 is the odd one out with a high p value, but it is lower than som2 was
lastFive = glm(disorder ~ som10+som11+som12+som13+som14, data = final,
                family = "binomial")
summary(lastFive)
#it seems that all of these have low p values and so cannot really bt trusted, except som13
#also their std are pretty low so the data is pretty clustered compared

#the best one to predict the behavior is the second model based on the low p values
