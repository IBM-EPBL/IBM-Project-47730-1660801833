library('readr')
library("lubridate")
library('rgl')
library('ggplot2')
dator <- read_csv("C:/Users/ankai/Desktop/important saves/disaster analysis/Nature_Disaster_Analysis_ggplot/data_pop_ud.csv")
dator$`EVENT START DATE`[131] <- "2018-01-01"


dat_a <- dator[dator$`Province/Territory`=="NL" & as.numeric(strftime(dator$`EVENT START DATE`,"%Y"))<=1982,]
dat_b <- dator[dator$`Province/Territory`=="NL" & as.numeric(strftime(dator$`EVENT START DATE`,"%Y"))>1982,]
datplot_a_e <- data.frame(x=dat_a$EVACUATED)
datplot_b_e <- data.frame(x=dat_b$EVACUATED)
datplot_a_f <- data.frame(x=dat_a$FATALITIES)
datplot_b_f <- data.frame(x=dat_b$FATALITIES)

pt_a_e <- hist(datplot_a_e$x,breaks=seq(0,2000,125))  
ppt_a_e <- data.frame(x=pt_a_e$breaks[-length(pt_a_e$breaks)],count=pt_a_e$counts)
pt_b_e <- hist(datplot_b_e$x,breaks=seq(0,2000,125))  
ppt_b_e <- data.frame(x=pt_b_e$breaks[-length(pt_b_e$breaks)],count=pt_b_e$counts)
pt_a_f <- hist(datplot_a_f$x,breaks=seq(0,2000,125))  
ppt_a_f <- data.frame(x=pt_a_f$breaks[-length(pt_a_f$breaks)],count=pt_a_f$counts)
pt_b_f <- hist(datplot_b_f$x,breaks=seq(0,2000,125))  
ppt_b_f <- data.frame(x=pt_b_f$breaks[-length(pt_b_f$breaks)],count=pt_b_f$counts)

ppt <- data.frame(x=c(ppt_a_e$x,ppt_b_e$x,ppt_a_f$x,ppt_b_f$x),
                  count=c(ppt_a_e$count,ppt_b_e$count,ppt_a_f$count,ppt_b_f$count),
                  color=c(rep("ae",nrow(ppt_a_e)),rep("be",nrow(ppt_b_e)),rep("af",nrow(ppt_a_f)),rep("bf",nrow(ppt_b_f))))

ggplot(ppt) +
  geom_bar(data=ppt_a_e,aes(x,count+ppt_a_f$count,fill="Evacuated"), stat = "identity") +
  geom_bar(data=ppt_b_e,aes(x,-count-ppt_b_f$count,fill="Evacuated"), stat = "identity") +
  geom_bar(data=ppt_a_f,aes(x,count,fill="Fatalities"), stat = "identity") +
  geom_bar(data=ppt_b_f,aes(x,-count,fill="Fatalities"), stat = "identity") +
  scale_y_continuous(breaks=seq(-100,40,10),labels=abs(seq(-100,40,10)))+
  labs(title="Evacuation and Fatalities in NL", 
       subtitle="up: <1982,    down: >1982",
       x="No. of Invloved Indivadual", 
       y="Fatalities or Evacuation", 
       fill="Human Action")+
  scale_colour_manual(name="Line Color",
                      values=c(Evacuated="#CC6666", Fatalities="#9999CC"))+
  geom_line(data=data.frame(x=c(-60:2000)),aes(x,0))


#
# test
# 
2000/2/2/2/2


k <- data.frame(x=1:100, y=rnorm(100), z=rnorm(100))
ggplot()+
  geom_bar(data=k,aes(x,k$z, fill="z"), stat = "identity")+
  geom_bar(data=k,aes(x,k$y, fill="y"), stat = "identity")+
  scale_colour_manual(name="color",
                      values=c(y="red",z="blue"))
ggplot()+
  geom_bar(data=k,aes(x,k$y, fill="y"), stat = "identity")+
  geom_bar(data=k,aes(x,k$z, fill="z"), stat = "identity")+
  scale_colour_manual(name="color",
                      values=c(y="red",z="blue"))
