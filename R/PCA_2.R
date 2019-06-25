library(ggplot2)

library(Rmisc)

setwd("/Users/skye_ye/Desktop/gitTUT/R")

getwd()

data <- read.csv(file = "GOMECC2_station_data.csv",header = TRUE,sep= ",")
names(data)
d <- data
d[d<10]<-NA #把-999變為NAN
#data2 <- data.frame(d[,"CTDSAL"], d[,"CTDTMP"], d[,"ALKALI"])
#data4 <- na.omit (data) #把data2裡的nan都刪掉

p1 <-ggplot(d)+geom_point(aes(x=ALKALI,y=CTDSAL)) 
p2 <-ggplot(d,aes(x=CTDSAL,y=CTDTMP))+geom_point()#+geom_smooth(method="loess",se=FALSE)
p3 <-ggplot(d,aes(x=ALKALI,y=CTDTMP))+geom_point()#+geom_smooth(method="loess",se=FALSE)
p4 <-ggplot(d)+geom_point(aes(x=NITRAT,y=TCARBN))

multiplot(p1,p2,p3,p4,cols=2)


  
