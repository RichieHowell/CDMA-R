setwd("C:\\Users\\Richie Howell\\Documents\\R Stuffs and things\\CDMA-R")

load("exampleData1.rData")

?merge
merged_data = merge(custdata, medianincome, by.x= "state.of.res", by.y = "State")
merged_data$norm.income = merged_data$income/merged_data$Median.Income.y
norm.income = merged_data$norm.income
summary(norm.income)
#when you want to see who is actually wealthy, and who is just wealthy because they are
#in a state that is more wealthy is when this comes in handy

trainingset = subset(merged_data, merged_data$norm.income <= .35)
testingset = subset(merged_data,merged_data$norm.income > .35 )


