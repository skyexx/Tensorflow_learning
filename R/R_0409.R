#獲得文件的路徑
setwd("/Users/skye_ye/Desktop/gitTUT/R")

getwd()

#讀取檔案
data <- read.csv(file = "GOMECC2_station_data.csv",header = TRUE,sep= ",")

#獲得標頭名稱
names(data)

#取出三行數據重組
data2 <- data.frame(data[,"CTDSAL"], data[,"CTDTMP"], data[,"CTDPRS"])

View(data2)

data[,"DEPTH"]

#行列[row，column]
plot(data[,"CTDSAL"], data[,"CTDTMP"],"p")

d <- data
d[d<10]<-NA  #to replace "-999" as "NA"
plot(d[,"TCARBN"],-d[,"DEPTH"],"p") # 繪出x-y圖
hist(d[,"TCARBN"]) # 使用R繪出hist圖  組距圖

#有問題打function name
y<-d[,"TCARBN"]
x1<-d[,"CTDSAL"]
x2<-d[,"CTDTMP"]
x3<-d[,"CTDOXY"]

fit<-lm(y~x1+x2+x3,data=d) #這就是 Multiple Linear Regression

#Coefficients就是係數
# Estimate就是b（y=a1x1+a2x2...+b）
#(Intercept)後面是都為零的時候的值
###Coefficients:
  #Estimate Std. Error t value Pr(>|t|)    
#(Intercept) 1562.21796   29.54833   52.87   <2e-16 ***
  #x1            23.11366    0.76276   30.30   <2e-16 ***
  #x2            -8.00065    0.13554  -59.03   <2e-16 ***
  #x3            -0.73714    0.02749  -26.81   <2e-16 ***
#Multiple R-squared:  0.9249,	Adjusted R-squared:  0.9246 （R-squared越高越好）
### ---

summary(fit)#show the result

fit<-lm(y~x1+x3,data=d)
summary(fit)#show the result

x4<-d[,"CTDOXY"]^2  #(你可以根據你的想法進行變形，添加平方，開放，log...)
fit<-lm(y~x1+x2+x3+x4,data=d)
summary(fit)#show the result

#小工具cheat sheet（function的懶人包）



