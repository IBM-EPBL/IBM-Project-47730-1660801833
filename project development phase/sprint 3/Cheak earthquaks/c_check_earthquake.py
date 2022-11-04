def check_earthquakes_location(lat_out=float,lon_out=float):
    
    try:
    
        TARGET_REQ_URL = "https://www.emsc-csem.org/service/rss/rss.php?typ=emsc"
    
        REQ_TARGET = requests.get(TARGET_REQ_URL).text
        SOUP_TARGET = BeautifulSoup(REQ_TARGET,"html.parser")
        
        FIND_ALL_IT = SOUP_TARGET.find_all("item")
        
        checking_value = 0
        
        print("\n")
        time.sleep(1.2)
        print("CONNECTED PORTAL I")
        
        
        for x_loop in FIND_ALL_IT:
            
            TITLE_OUT = x_loop.find("title")
            LAT_OUT = x_loop.find("geo:lat")
            LON_OUT = x_loop.find("geo:long")
            DEP_OUT = x_loop.find("emsc:depth")
            MAG_OUT = x_loop.find("emsc:magnitude")
            TIME_OUT = x_loop.find("emsc:time")
            ST_OUT = x_loop.find("status")
            
            
            LAT_OUT = float(LAT_OUT.text)
            LON_OUT = float(LON_OUT.text)
            
            
            
            if lat_out == LAT_OUT and lon_out == LON_OUT:
                
                time.sleep(0.8)
                print("\n")
                print("TITLE: ",TITLE_OUT.text)
                print("LATITUDE: ",LAT_OUT)
                print("LONGITUDE: ",LON_OUT)
                print("DEPTH: ",DEP_OUT.text)
                print("MAGNITUDE: ",MAG_OUT.text)
                print("DATE: ",TIME_OUT.text)
                print("STATUS: ",ST_OUT.text)
                print("\n")
                checking_value += 1
                                                    
      
            elif "%.2f"%float(lat_out) == "%.2f"%float(LAT_OUT) and "%.2f"%float(lon_out) == "%.2f"%float(LON_OUT):
                
                time.sleep(0.8)
                print("\n")
                print("TITLE: ",TITLE_OUT.text)
                print("LATITUDE: ",LAT_OUT)
                print("LONGITUDE: ",LON_OUT)
                print("DEPTH: ",DEP_OUT.text)
                print("MAGNITUDE: ",MAG_OUT.text)
                print("DATE: ",TIME_OUT.text)
                print("STATUS: ",ST_OUT.text)
                print("\n")
                checking_value += 1
                                        
                                                    
            elif "%.f"%float(lat_out) == "%.f"%float(LAT_OUT) and "%.f"%float(lon_out) == "%.f"%float(LON_OUT):
                
                time.sleep(0.8)
                print("\n")
                print("TITLE: ",TITLE_OUT.text)
                print("LATITUDE: ",LAT_OUT)
                print("LONGITUDE: ",LON_OUT)
                print("DEPTH: ",DEP_OUT.text)
                print("MAGNITUDE: ",MAG_OUT.text)
                print("DATE: ",TIME_OUT.text)
                print("STATUS: ",ST_OUT.text)
                print("\n")
                checking_value += 1
     
                         
            elif int(float(lat_out)) == int(float(LAT_OUT)) and int(float(lon_out)) == int(float(LON_OUT)):
                
                time.sleep(0.8)
                print("\n")
                print("TITLE: ",TITLE_OUT.text)
                print("LATITUDE: ",LAT_OUT)
                print("LONGITUDE: ",LON_OUT)
                print("DEPTH: ",DEP_OUT.text)
                print("MAGNITUDE: ",MAG_OUT.text)
                print("DATE: ",TIME_OUT.text)
                print("STATUS: ",ST_OUT.text)
                print("\n")
                checking_value += 1
                
            else:
                pass
            
        if checking_value < 1:
            
            time.sleep(0.8)
            print("Portal I: There is no earthquake response")
            print("\n")
    
    except:
        
        print("YOU ARE CONNECTING OTHER SOURCE PLEASE WAIT")
        print("\n")
        time.sleep(1.5)
    
    
    try:
        
        TARGET_REQ_URL = "https://www.emsc-csem.org/service/rss/rss.php?typ=emsc&magmin=4"
    
        REQ_TARGET = requests.get(TARGET_REQ_URL).text
        SOUP_TARGET = BeautifulSoup(REQ_TARGET,"html.parser")
        
        FIND_ALL_IT = SOUP_TARGET.find_all("item")
        
        checking_value = 0
        
        print("\n")
        time.sleep(1.2)
        print("CONNECTED PORTAL II")
        
        
        for x_loop in FIND_ALL_IT:
            
            TITLE_OUT = x_loop.find("title")
            LAT_OUT = x_loop.find("geo:lat")
            LON_OUT = x_loop.find("geo:long")
            DEP_OUT = x_loop.find("emsc:depth")
            MAG_OUT = x_loop.find("emsc:magnitude")
            TIME_OUT = x_loop.find("emsc:time")
            ST_OUT = x_loop.find("status")
            
            
            LAT_OUT = float(LAT_OUT.text)
            LON_OUT = float(LON_OUT.text)
            
            
            
            if lat_out == LAT_OUT and lon_out == LON_OUT:
                
                time.sleep(0.8)
                print("\n")
                print("TITLE: ",TITLE_OUT.text)
                print("LATITUDE: ",LAT_OUT)
                print("LONGITUDE: ",LON_OUT)
                print("DEPTH: ",DEP_OUT.text)
                print("MAGNITUDE: ",MAG_OUT.text)
                print("DATE: ",TIME_OUT.text)
                print("STATUS: ",ST_OUT.text)
                print("\n")
                checking_value += 1
                                                    
      
            elif "%.2f"%float(lat_out) == "%.2f"%float(LAT_OUT) and "%.2f"%float(lon_out) == "%.2f"%float(LON_OUT):
                
                time.sleep(0.8)
                print("\n")
                print("TITLE: ",TITLE_OUT.text)
                print("LATITUDE: ",LAT_OUT)
                print("LONGITUDE: ",LON_OUT)
                print("DEPTH: ",DEP_OUT.text)
                print("MAGNITUDE: ",MAG_OUT.text)
                print("DATE: ",TIME_OUT.text)
                print("STATUS: ",ST_OUT.text)
                print("\n")
                checking_value += 1
                                        
                                                    
            elif "%.f"%float(lat_out) == "%.f"%float(LAT_OUT) and "%.f"%float(lon_out) == "%.f"%float(LON_OUT):
                
                time.sleep(0.8)
                print("\n")
                print("TITLE: ",TITLE_OUT.text)
                print("LATITUDE: ",LAT_OUT)
                print("LONGITUDE: ",LON_OUT)
                print("DEPTH: ",DEP_OUT.text)
                print("MAGNITUDE: ",MAG_OUT.text)
                print("DATE: ",TIME_OUT.text)
                print("STATUS: ",ST_OUT.text)
                print("\n")
                checking_value += 1
     
                         
            elif int(float(lat_out)) == int(float(LAT_OUT)) and int(float(lon_out)) == int(float(LON_OUT)):
                
                time.sleep(0.8)
                print("\n")
                print("TITLE: ",TITLE_OUT.text)
                print("LATITUDE: ",LAT_OUT)
                print("LONGITUDE: ",LON_OUT)
                print("DEPTH: ",DEP_OUT.text)
                print("MAGNITUDE: ",MAG_OUT.text)
                print("DATE: ",TIME_OUT.text)
                print("STATUS: ",ST_OUT.text)
                print("\n")
                checking_value += 1
                
            else:
                pass
            
        if checking_value <= 0:
            
            time.sleep(0.8)
            print("PORTAL II: There is no earthquake response")
            print("\n")
                                                
            
    except:
        
        print("THERE IS A CONNECTION PROBLEM, IT MAY BE ABOUT YOUR INTERNET CONNECTION OR DATABASE")
        time.sleep(0.5)
        print("PLEASE CHECK YOUR CONNECTION AND TRY AGAIN")
        print("\n")
        time.sleep(0.7)
