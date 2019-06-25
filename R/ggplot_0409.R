library(ggplot2)
setwd("/Users/skye_ye/Desktop/gitTUT/R")
getwd()

data <- read.csv(file = "Berkeley_reference_of_tainan.csv",header = TRUE,sep= ",")
names(data) 


data["Year."]
p1<-data.frame(data["Year."],data["Ann_Anomaly."]+23.29)
p2<-data.frame(data["Year."],data["Ten_Anomaly."]+23.29)
##################
plot(p1,type="l",xaxt="n",ylim=c(21.5,24.5),
     main="Reference Location:23.31N,119.71E",xlab="",ylab="Mean Temperature")
par(new=TRUE)
plot(p2,type="l",col="red",ylim=c(21.5,24.5),axes=FALSE,xlab="",ylab="")
legend(1840,24.5,lwd=2,col=c("red","black"),cex=0.6,
       legend=c("10-year moving average with 95% uncertainty","12-month moving average"))
axis(side=1,at=seq(1840,2020,20))
axis(side=4,at=seq(21.5,24.5,0.5))

p1<-data.frame(data["Year."],data["Ann_Anomaly."]+23.29)
p2<-data.frame(data["Year."],data["Ten_Anomaly."]+23.29)
################
plot(p1,type="l",xaxt="n",ylim=c(21.5,24.5),main="Reference Location:23.31N,119.71E")
lines(p2,type="l",col="Red")

plot(p1,type="l",xaxt="n",main="Reference Location:23.31N,119.71E",
     xlab="",ylab="Mean Temperature")
lines(p2,type="l",col="Red")
legend(1840,24.5,lwd=2,col=c("red","black"),cex=0.6,
       legend=c("10-year moving average with 95% uncertainty","12-month moving average"))
axis(side=1,at=seq(1840,2020,20))
axis(side=4,at=seq(21.5,24.5,0.5))