library(ggplot2)
setwd("/Users/skye_ye/Desktop/gitTUT/R")
getwd()

data <- read.csv(file = "Berkeley_reference_of_tainan.csv",header = TRUE,sep= ",")
#ggplot有點像圖層的概念可以一直加自己需要的元素
#不用轉換成data.frame的格式，直接輸入每列的變數就能用了
ggplot(data,aes(x = Year.)) +
  geom_line(aes(y=23.29 + Ann_Anomaly.,colour ="12-month moving average")) +
  geom_line(aes(y=23.29 + Ten_Anomaly.,colour ="10-year moving average with 95% uncertainty")) +
  geom_text(aes(x=1980,y=21.6,label = "Berkeley Earth surface temperature"))+
  geom_ribbon(aes(ymin=Ten_Anomaly.+23.29-Ten_Unc.., 
                  ymax=Ten_Anomaly.+23.29+Ten_Unc..), fill="grey1", alpha=0.2) + #預測的區間
  scale_colour_manual("",values = c("10-year moving average with 95% uncertainty" = "red",
                                    "12-month moving average" = "black")) + #修改設定顏色
  theme(panel.background=element_rect(fill='transparent', color='gray'))+#修改背景
  #theme(panel.background = element_blank())+這個是全部變成空白的，包括外面的框框
  
  #xlim(1840,2020) +
  #ylim(21.5,24.5) + 
  #显示刻度从1840到2020,间隔为20,這樣不需要上面對於xlim和ylim的限制了,這樣會變成重複設置
  #一個範圍的話就用seq()
  #scale_y_continuous(breaks=c(4, 4.25, 4.5, 5, 6,8)只顯示設置的刻度，用c（）
  scale_x_continuous(breaks=seq(1840,2020,20)) +
  scale_y_continuous(breaks=seq(21.5,24.5,0.5)) +
  
  xlab('Year') +
  ylab('Mean Temperature(°C )') +
  ggtitle('Reference Location:23.31N,119.71E')+
  theme(legend.position=c(0.28,0.9))+#設置legend的位置，右上角为c(1,1),左下角为c(0,0)
  theme(legend.title=element_blank())+
  #theme(legend.background=element_rect(fill='transparent', color='gray'))+
  theme(legend.key.size=unit(0.8,'cm'))+
  theme(plot.title = element_text(hjust = 0.5))+
  theme(plot.background=element_rect(colour = 'gray90'))

