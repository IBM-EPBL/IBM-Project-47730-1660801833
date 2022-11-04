install.packages('lubridate')
library('readr')
library("lubridate")
library(readxl)
dat <- read_csv("C:/Users/ankai/Desktop/important saves/disaster analysis/case_study_1_cdd_database_final_0.csv")


df <- dat[(dat$`EVENT TYPE` == 'Wildfire'),]

Location <- c(unique(df$`Province/Territory`))
Location


testVector <-data.frame(EVENT_START_DATE=df$"EVENT START DATE",PROVINCE_TERRITORY=df$"Province/Territory")

prov_map<-function(a){
  n<-length(a)
  x<-c(rep(0,n))
  for (i in 1:n) {
    if(!is.na(a[i])) { 
      if (a[i]=="BC") {x[i]<-1}
      if (a[i]=="BC AB") {x[i]<-2}
      if (a[i]=="AB") {x[i]<-3}
      if (a[i]=="YT") {x[i]<-4}
      if (a[i]=="NT") {x[i]<-5}
      if (a[i]=="SK") {x[i]<-6}
      if (a[i]=="MB") {x[i]<-7}
      if (a[i]=="ON") {x[i]<-8}
      if (a[i]=="ON QC") {x[i]<-9}
      if (a[i]=="QC") {x[i]<-10}
      if (a[i]=="NL") {x[i]<-11}
      if (a[i]=="NB") {x[i]<-12}
      if (a[i]=="NS") {x[i]<-13}
    }
  }
  return(x)
}

#names(testVector) <- c("EVENT_START_DATE", "PROVINCE_TERRITORY")
prov_map('ON')
prov_map(c('ON','BC'))

prov_map(testVector$PROVINCE_TERRITORY)





testVector2 <-data.frame(EVENT_START_DATE=testVector$EVENT_START_DATE,
                        PROVINCE_TERRITORY=testVector$PROVINCE_TERRITORY,
                        PROV_MAP=prov_map(testVector$PROVINCE_TERRITORY))




plot(as.Date(testVector2$EVENT_START_DATE),testVector2$PROV_MAP)

plot(as.Date(testVector$EVENT_START_DATE),testVector$PROVINCE_TERRITORY)


testVector$EVENT_START_DATE
month<- strftime(testVector$EVENT_START_DATE,"%m")
month



testVector2 <-data.frame(EVENT_START_DATE=testVector$EVENT_START_DATE,
                         PROVINCE_TERRITORY=testVector$PROVINCE_TERRITORY,
                         PROV_MAP=prov_map(testVector$PROVINCE_TERRITORY),
                         MONTH=strftime(testVector$EVENT_START_DATE,"%m"))

plot(testVector2$PROV_MAP,testVector2$MONTH)

str(testVector2)


#
#
#
old_date<- "01/01/1979"
new_date<- as.Date(old_date, "%m/%d/%Y")
new_date
#[1] "1979-01-01"
month<- strftime(new_date,"%m")
month
#[1] "01"
year<- strftime(new_date, "%Y")
year
#[1] "1979"
#
#
#
