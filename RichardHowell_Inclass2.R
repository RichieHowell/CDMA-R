
getwd()
setwd("C:\\Users\\Richie Howell\\Documents\\R Stuffs and things\\CDMA-R")

load('exampleData.rData')
summary(custdata)
summary(custdata$state.of.res)
#for state of residence it seems like a well behaved data set with no NA vaues
summary(custdata$custid)
#for this one the information about the median, and spacing of hte variables matters
#little since customer ids don't give relevant information about the customer and are just an identifier
summary(custdata$sex)
#data seems well behaved, under half female is odd but i guess that is the data
summary(custdata$is.employed)
#NA's might be missing data or could stand for false
summary(custdata$income)
#there is a negative value for the min, need to see if this stands for debt
#or if there is a problem inputting the data, max is also abnormally high for the data it seems
summary(custdata$marital.stat)
#seems well behaved 
summary(custdata$health.ins)
#no NA data so this seems well behaved, a lot more ture than false which makes sense
summary(custdata$housing.type)
#do NA's mean no home, or their housing situation does not fit into the 4 kinds
summary(custdata$recent.move)
#more NA's so need to see if missing data, or error inputting data, or is NA is false
summary(custdata$num.vehicles)
#NA should prob be 0 in this case,unless error inputting data
summary(custdata$age)
summary(custdata$is.employed.fix1)
summary(custdata$age.normalized)
summary(custdata$Median.Income)
summary(custdata$income.norm)
summary(custdata$gp)
summary(custdata$income.lt.30k)
summary(custdata$age.range)
summary(custdata$Income)