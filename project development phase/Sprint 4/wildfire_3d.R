library('readr')
library("lubridate")
library(readxl)
library('rgl')
dat <- read_csv("C:/Users/ankai/Desktop/important saves/disaster analysis/case_study_1_cdd_database_final_0.csv")


df <- dat[(dat$`EVENT TYPE` == 'Wildfire'),]

Location <- c(unique(df$`Province/Territory`))
Location


testVector <-data.frame(EVENT_START_DATE=df$"EVENT START DATE",PROVINCE_TERRITORY=df$"Province/Territory")

prov_map<-function(a){
  n<-length(a)
  x<-data.frame('Y'=rep(0,n),'X'=rep(0,n))
  for (i in 1:n) {
    if(!is.na(a[i])) { 
      if (a[i]=="BC") {x[i,]<-c(1,2)}
      if (a[i]=="BC AB") {x[i,]<-c(1,3)}
      if (a[i]=="AB") {x[i,]<-c(1,4)}
      if (a[i]=="YT") {x[i,]<-c(2,2)}
      if (a[i]=="NT") {x[i,]<-c(2,5)}
      if (a[i]=="SK") {x[i,]<-c(1,6)}
      if (a[i]=="MB") {x[i,]<-c(1,8)}
      if (a[i]=="ON") {x[i,]<-c(1,10)}
      if (a[i]=="ON QC") {x[i,]<-c(1,11)}
      if (a[i]=="QC") {x[i,]<-c(1,12)}
      if (a[i]=="NL") {x[i,]<-c(1,14)}
      if (a[i]=="NB") {x[i,]<-c(1,16)}
      if (a[i]=="NS") {x[i,]<-c(1,18)}
    }
  }
  return(x)
}

#names(testVector) <- c("EVENT_START_DATE", "PROVINCE_TERRITORY")
prov_map('ON')
prov_map(c('ON','BC'))

prov_map(testVector$PROVINCE_TERRITORY)

testVector$EVENT_START_DATE
month<- strftime(testVector$EVENT_START_DATE,"%m")
month



testVector2 <-data.frame(EVENT_START_DATE=testVector$EVENT_START_DATE,
                         PROVINCE_TERRITORY=testVector$PROVINCE_TERRITORY,
                         PROV_MAP=prov_map(testVector$PROVINCE_TERRITORY),
                         MONTH=strftime(testVector$EVENT_START_DATE,"%m"))

plot3d(testVector2$PROV_MAP.X, testVector2$PROV_MAP.Y, testVector2$MONTH,col = rainbow(1000))
with(iris, plot3d('x'=testVector2$PROV_MAP.X, 'y'=testVector2$PROV_MAP.Y, testVector2$EVENT_START_DATE, 
                   type='s',col=as.numeric(testVector2$MONTH )))

with(iris, plot3d('x'=testVector2$PROV_MAP.X, 'y'=testVector2$PROV_MAP.Y, testVector2$MONTH, 
                  type='s',col=rainbow(1000)))
str(testVector2)


#
#
#