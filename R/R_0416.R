#主成份分析（PCA），還有EOF分析 SVD分析 DEOF 分析
#怎麼從眾多參數中找出自己要分析的參數？找出最重要的控制參數？
#如果很快找到線型關係，就不用PCA了。
#如果拿到數據沒辦法解釋的時候就可以試試看PCA，或者資料量太龐大，亦或需要定量解釋的時候，
#所以PCA分析的數據都是比較離散的數據。PCA就是轉變座標軸，轉到一個程度，找到所有點離他最接近的。
#你要喂多少數據，要有邏輯背景支撐,你要解釋為什麼PCA跑出來是這樣的。
#R有內建prcomp

setwd("/Users/skye_ye/Desktop/gitTUT/R")

getwd()

data <- read.csv(file = "GOMECC2_station_data.csv",header = TRUE,sep= ",")
names(data)
d <- data
d[d<10]<-NA #把-999變為NAN
data2 <- data.frame(d[,"CTDSAL"], d[,"CTDTMP"], d[,"CTDPRS"], d[,"CTDOXY"],
                    d[,"OXYGEN"], d[,"NITRAT"], d[,"TCARBN"], d[,"ALKALI"])

data4 <- na.omit (data2) #把data2裡的nan都刪掉

d.pca<-prcomp(data4, center = TRUE ,scale. = TRUE )

summary(d.pca)#summary就是要顯示
biplot(d.pca)

#x1<-d[,"CTDSAL"]
#x2<-d[,"CTDTMP"]
#x3<-d[,"CTDOXY"]
