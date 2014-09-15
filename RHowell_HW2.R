getwd()
setwd("C:\\Users\\Richie Howell\\Documents\\R Stuffs and things\\CDMA-R")
load('phsample.RData')
summary(dhus)
names(dhus)
#it appears to be a data set of people or entities and their information
#2.12, creates a subset of the dpus dataset with only values of 
#PINCP and PERNP between 1000 and 250000, ESR = 1, ages between 20 and 50, WKHP above or equal to 40, PWGTP1 as natural numbers, 
#cow between 1 and 7, and SCHL between 1 and 24
psub = subset(dpus,with(dpus,(PINCP>1000)&(ESR==1)&
                          (PINCP<=250000)&(PERNP>1000)&(PERNP<=250000)&
                          (WKHP>=40)&(AGEP>=20)&(AGEP<=50)&
                          (PWGTP1>0)&(COW %in% (1:7))&(SCHL %in% (1:24))))
#2.13 makes the data more readable by making it more human readable.
psub$SEX = as.factor(ifelse(psub$SEX==1,'M','F'))
psub$SEX = relevel(psub$SEX,'M')
cowmap <- c("Employee of a private for-profit",
            "Private not-for-profit employee",
            "Local government employee",
            "State government employee",
            "Federal government employee",
            "Self-employed not incorporated",
            "Self-employed incorporated")
psub$COW = as.factor(cowmap[psub$COW])
psub$COW = relevel(psub$COW,cowmap[1])
schlmap = c(
  rep("no high school diploma",15),
  "Regular high school diploma",
  "GED or alternative credential",
  "some college credit, no degree",
  "some college credit, no degree",
  "Associate's degree",
  "Bachelor's degree",
  "Master's degree",
  "Professional degree",
  "Doctorate degree")
psub$SCHL = as.factor(schlmap[psub$SCHL])
psub$SCHL = relevel(psub$SCHL,schlmap[1])
dtrain = subset(psub,ORIGRANDGROUP >= 500)
dtest = subset(psub,ORIGRANDGROUP < 500)
#2.14, gives us a summary of the cow variable in the dtrain dataset
summary(dtrain$COW)
data = read.csv("Produc.csv")
