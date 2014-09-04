
#Problem 1
#row.names is the parameter used in the read.table function that lets you either give it a vector of the row names or the column which contains the row names.
setwd("C:\\Users\\Richie Howell\\Documents\\R Stuffs and things\\CDMA-R")
table = read.table(file = "HW1text.txt", header = TRUE)
#-----------------------------------------------------------
#Problem 2
#create the vectors for number 1
vec1=c(1,0,0,0)
vec2=c(0,1,0,0)
vec3=c(0,0,1,0)
vec4=c(0,0,0,1)
#binds the vectors into a matrix, identity matrix in this example
MAT1=cbind(vec1,vec2,vec3,vec4)
#outputs the last element in the matrix
print(MAT1[4,4])
#finds the transpose of the matrix and puts it into MAT1.transposed
MAT1.Transposed = t(MAT1)
#finds the inverse of the matrix and puts it into MAT1.Inverse
Mat1.Inverse=solve(MAT1)
#------------------------------------------------
#problem 3
#creates the data set
fpe <- read.table("http://data.princeton.edu/wws509/datasets/effort.dat")
#prints out the data where effort = 0
print(fpe[fpe$effort == 0,])
#prints out the names of the variables in the data set
print(colnames(fpe))
#prints out the names of the rows in the data set
print(rownames(fpe))
#finds out what head does
?head
#returns out the first few elements of a data set
print(head(fpe))
#writes the data to a csv file
write.csv(fpe,file="fpecsv.csv")
#writes the data to a txt file
write.table(fpe,file="fpetxt.txt",sep="\t")
