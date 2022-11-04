library('readr')
library("lubridate")
library('rgl')
library('ggplot2')
dat <- read_csv("C:/Users/ankai/Desktop/important saves/disaster analysis/data_pop_ud.csv")



c(unique(dat$`EVENT TYPE`))

wf <- dat[(dat$`EVENT TYPE` == 'Wildfire') & (dat$Population > 0),] 
wfyear<-data.frame(x=wf$`EVENT START DATE`,y=(wf$`INJURED/INFECTED`+wf$FATALITIES+wf$EVACUATED)/(wf$Population))
ggplot(wfyear,aes(x=as.Date(wfyear$x),y=wfyear$y))+ geom_point(shape=1)
wfmonth<-data.frame(x=strftime(wf$`EVENT START DATE`,"%m"),y=(wf$`INJURED/INFECTED`+wf$FATALITIES+wf$EVACUATED)/(wf$Population))
qplot( x=wfmonth$x , y=wfmonth$y , data=wfmonth , geom=c("boxplot","jitter") , fill=wfmonth$x)
#
#
wf <- dat[(dat$`EVENT TYPE` == 'Wildfire') & (dat$Population > 0) & (dat$`Province/Territory` == 'ON'),] 
wfyear<-data.frame(x=wf$`EVENT START DATE`,y=(wf$`INJURED/INFECTED`+wf$FATALITIES+wf$EVACUATED)/(wf$Population))
ggplot(wfyear,aes(x=as.Date(wfyear$x),y=wfyear$y))+ geom_point(shape=1)
wfmonth<-data.frame(x=strftime(wf$`EVENT START DATE`,"%m"),y=(wf$`INJURED/INFECTED`+wf$FATALITIES+wf$EVACUATED)/(wf$Population))
qplot( x=wfmonth$x , y=wfmonth$y , data=wfmonth , geom=c("boxplot","jitter") , fill=wfmonth$x)
#
#
wf <- dat[(dat$`EVENT TYPE` == 'Wildfire') & (dat$Population > 0) & (dat$`Province/Territory` == 'MB'),] 
wfyear<-data.frame(x=wf$`EVENT START DATE`,y=(wf$`INJURED/INFECTED`+wf$FATALITIES+wf$EVACUATED)/(wf$Population))
ggplot(wfyear,aes(x=as.Date(wfyear$x),y=wfyear$y))+ geom_point(shape=1)
wfmonth<-data.frame(x=strftime(wf$`EVENT START DATE`,"%m"),y=(wf$`INJURED/INFECTED`+wf$FATALITIES+wf$EVACUATED)/(wf$Population))
qplot( x=wfmonth$x , y=wfmonth$y , data=wfmonth , geom=c("boxplot","jitter") , fill=wfmonth$x)
#
#

#
#
fd <- dat[(dat$`EVENT TYPE` == 'Flood')& (dat$Population > 0),]             
fdyear<-data.frame(x=fd$`EVENT START DATE`,y=(fd$`INJURED/INFECTED`+fd$FATALITIES+fd$EVACUATED)/(fd$Population))
ggplot(fdyear,aes(x=as.Date(fdyear$x),y=fdyear$y))+ geom_point(shape=1)  
fdmonth<-data.frame(x=strftime(fd$`EVENT START DATE`,"%m"),y=(fd$`INJURED/INFECTED`+fd$FATALITIES+fd$EVACUATED)/(fd$Population))
qplot( x=fdmonth$x , y=fdmonth$y , data=fdmonth , geom=c("boxplot","jitter") , fill=fdmonth$x)
#
#
fd <- dat[(dat$`EVENT TYPE` == 'Flood')& (dat$Population > 0)& (dat$`Province/Territory` == 'ON'),]             
fdyear<-data.frame(x=fd$`EVENT START DATE`,y=(fd$`INJURED/INFECTED`+fd$FATALITIES+fd$EVACUATED)/(fd$Population))
ggplot(fdyear,aes(x=as.Date(fdyear$x),y=fdyear$y))+ geom_point(shape=1)  
fdmonth<-data.frame(x=strftime(fd$`EVENT START DATE`,"%m"),y=(fd$`INJURED/INFECTED`+fd$FATALITIES+fd$EVACUATED)/(fd$Population))
qplot( x=fdmonth$x , y=fdmonth$y , data=fdmonth , geom=c("boxplot","jitter") , fill=fdmonth$x)
#
#
fd <- dat[(dat$`EVENT TYPE` == 'Flood')& (dat$Population > 0)& (dat$`Province/Territory` == 'MB'),]             
fdyear<-data.frame(x=fd$`EVENT START DATE`,y=(fd$`INJURED/INFECTED`+fd$FATALITIES+fd$EVACUATED)/(fd$Population))
ggplot(fdyear,aes(x=as.Date(fdyear$x),y=fdyear$y))+ geom_point(shape=1)  
fdmonth<-data.frame(x=strftime(fd$`EVENT START DATE`,"%m"),y=(fd$`INJURED/INFECTED`+fd$FATALITIES+fd$EVACUATED)/(fd$Population))
qplot( x=fdmonth$x , y=fdmonth$y , data=fdmonth , geom=c("boxplot","jitter") , fill=fdmonth$x)
