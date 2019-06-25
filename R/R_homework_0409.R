setwd("/Users/skye_ye/Desktop/gitTUT/R")
getwd()

data <- read.csv(file = "Berkeley_reference_of_tainan.csv",header = TRUE,sep= ",")
names(data) 
rawData <- data.frame(data["Year."],data["Ten_Anomaly."],data["Ann_Anomaly."],data["Ten_Unc.."])

p1<-data.frame(data["Year."],data["Ann_Anomaly."]+23.29)
p2<-data.frame(data["Year."],data["Ten_Anomaly."]+23.29)

plot(p1,type="l",xaxt="n",yaxt="n",xlab="",ylab="Mean Temperature",bg="white",
     main= "Reference Location:23.31N,119.71E",)
title(main="Country: Taiwan                            Nearby Cities: Kaohsiung, Tainan, Fengshan",
      adj=0.3,line=0.5,cex.main=0.7)
abline(v=seq(1840, 2020, 20), h=seq(21.5, 24.5, 0.5), lty=2, col="gray")
lines(p2,type="l",col="Red")
legend(1840,24.5,lwd=2,col=c("red","black"),cex=0.8,
       legend=c("10-year moving average with 95% uncertainty","12-month moving average"))
axis(side=1,at=seq(1840,2020,20))
par(mar=c(4, 2, 4, 6)+0.1) #设置图形边距c(bottom,left, top, right)
axis(side=4,at=seq(21.5,24.5,0.5))
mtext(4,text="Mean Temperature(°C )",line=3)
text(x=1975,y=21.7, labels = "Berkeley Earth surface temperature",cex=0.8)
par(bg="grey95") #把图形背景设为灰色，後面可以接 0 到 99，顏色越大越白

