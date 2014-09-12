
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
#min age is 0, either newborn customer or that should be NA
summary(custdata$is.employed.fix1)
#this summary only tells us that characters are used to fill this variable
summary(custdata$age.normalized)
#i have no idea what a normalized age means, but data seems standard. Since it is normalized, it is good that the mean is 0
summary(custdata$Median.Income)
#mean is higher than the median so higher numbers in the higher 50%
summary(custdata$income.norm)
#max is really large
summary(custdata$gp)
#i have no idea what GP stands for, but data seems evenly distributed
summary(custdata$income.lt.30K)
#more people under 30k then over 30k, no data missing
summary(custdata$age.range)
#most people in the range from 25 to 65
summary(custdata$Income)
#the min is 0 which means 0 was a valid number to input for income, but there are also NA's so the NA's should probably be 0 unless income information was not able to be gained
library("hexbin")
library(ggplot2)
custdata2 <- subset(custdata,
                    (custdata$age > 0 & custdata$age < 100
                     & custdata$income > 0 & custdata$income < 200000))
hexbinplot(income ~ age, custdata2)
ggplot(custdata2, aes(x=age,y=income)) +
  geom_point() +
  ylim(0,200000) +
  theme_bw() +
  ggtitle("Scatterplot of Income vs Age")
#the hex bin plot is a bit easier to see where concentrations of correlations are located
#i will use a hex bin plot for the relationship between number of vehiclesand income
hexbinplot(num.vehicles ~ income, custdata)
#the plot tells me most people have 1 or 2 cars, and those that have more have lower income
#I will use a filled bar graph for income less than 30k vs recently moved
ggplot(custdata) + geom_bar(aes(x=recent.move,
                                fill=income.lt.30K),
                            position="fill") +
  theme_bw()+
  ggtitle("comparing recently moved to income less than 30k")
#we learn that there is a higher percentage of people with income less than 30k who did not recently move
