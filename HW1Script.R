
#Problem 1
#row.names is the parameter used in the read.table function that lets you either give it a vector of the row names or the column which contains the row names.
setwd("C:\\Users\\Richie Howell\\Documents\\R Stuffs and things")
table = read.table(file = "HW1text.txt", header = TRUE)
#-----------------------------------------------------------
#Problem 2
vec1=c(1,0,0,0)
vec2=c(0,1,0,0)
vec3=c(0,0,1,0)
vec4=c(0,0,0,1)
MAT1=cbind(vec1,vec2,vec3,vec4)
lastElement = MAT1[4,4]
MAT1.Transposed = t(MAT1)
Mat1.Inverse=solve(MAT1)
