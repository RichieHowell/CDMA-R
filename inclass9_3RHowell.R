setwd("C:\\Users\\Richie Howell\\Documents\\R Stuffs and things\\CDMA-R")

load("NatalRiskData.rData")
attach(sdata)
complications = c("ULD_MECO","ULD_PRECIP", "ULD_BREECH")
riskfactors = c("URF_DIAB", "URF_CHYPER", "URF_PHYPER", "URF_ECLAM")
y = "atRisk"
x = c("PWGT", "UPREVIS", "CIG_REC", "GESTREC3", 
      "DPLURAL", complications, riskfactors)
fmla = paste(y, paste(x, collapse="+"), sep="~")
model = glm(fmla, family = binomial)
sdata$gp <- runif(dim(sdata)[1])
train <- subset(sdata, sdata$gp > 0.5)
test <- subset(sdata, sdata$gp <= 0.5)
train$pred <- predict(model, newdata = train, type = "response")
library(ggplot2)
#density plot
ggplot(train, aes(x=pred, color=factor(atRisk), linetype=factor(atRisk))) +  geom_density()

confusion.test <- table(pred=test$pred>0.5, target = test$atRisk)
confusion.test
accuracy <- (confusion.test[2,2] + confusion.test[1,1])/sum(confusion.test[,])
accuracy 
precision <- confusion.test[2,2] / sum(confusion.test[2,])
precision
recall <- confusion.test[2,2] / sum(confusion.test[,2])
recall


