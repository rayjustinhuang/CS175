library(dplyr)

cali <- read.csv("geochem-fuS06.csv")
glimpse(cali)
selectedcolumns <- c("latitude", "longitude","qd250name","as_aa","cr_icp40", "zn_icp40")
final <- subset(cali, select = selectedcolumns)
final <- rename(final, c("latitude"="Latitude","longitude"="Longitude","qd250name"="Place","as_aa"="As","cr_icp40"="Cr","zn_icp40"="Zn"))

trainsize <- 0.4*nrow(final)
trainrows <- sample(seq_len(nrow(final)), size = trainsize)
training <- final[trainrows, ]
testwithactuals <- final[-trainrows, ]

test <- testwithactuals
test[ , c("As","Cr","Zn")] <- "?"

write.csv(training, "Kriging Train Data.csv")
write.csv(test, "Kriging Test Data.csv")
write.csv(testwithactuals, "Kriging Test Data with Actual Values.csv")

krigedata <- read.csv("Kriging Train Data.csv")
test <- read.csv("Kriging Test Data with Actual Values.csv")


summary(training)
summary(testwithactuals)

plot(training$Zn)
plot(testwithactuals$Zn)

rm(list = ls())
