def get_alternative_earthquake():
    
    TARGET_REQ_URL = "https://www.emsc-csem.org/service/rss/rss.php?typ=emsc"

    REQ_TARGET = requests.get(TARGET_REQ_URL).text
    SOUP_TARGET = BeautifulSoup(REQ_TARGET,"html.parser")
    
    FIND_ALL_IT = SOUP_TARGET.find_all("item")
    
    try:
        
        for x_loop in FIND_ALL_IT:
            
            TITLE_OUT = x_loop.find("title")
            LAT_OUT = x_loop.find("geo:lat")
            LON_OUT = x_loop.find("geo:long")
            DEP_OUT = x_loop.find("emsc:depth")
            MAG_OUT = x_loop.find("emsc:magnitude")
            TIME_OUT = x_loop.find("emsc:time")
            ST_OUT = x_loop.find("status")
            
            time.sleep(0.8)
            print("\n")
            print("TITLE: ",TITLE_OUT.text)
            print("LATITUDE: ",LAT_OUT.text)
            print("LONGITUDE: ",LON_OUT.text)
            print("DEPTH: ",DEP_OUT.text)
            print("MAGNITUDE: ",MAG_OUT.text)
            print("DATE: ",TIME_OUT.text)
            print("STATUS: ",ST_OUT.text)
            print("--"*10)
            
    except:
            
        print("\n")
        print("THERE IS A CONNECTION PROBLEM, IT MAY BE ABOUT YOUR INTERNET CONNECTION OR DATABASE")
        time.sleep(0.5)
        print("PLEASE CHECK YOUR CONNECTION AND TRY AGAIN")
        print("\n")
        time.sleep(0.7)
