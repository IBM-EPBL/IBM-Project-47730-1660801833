def get_nasa_eonet(count_search=int):
    
    TEST_SPEC_TARGET_URL = "https://eonet.sci.gsfc.nasa.gov/api/v3/events"
     
    try:
              
        READ_URL = requests.get(TEST_SPEC_TARGET_URL)
        READ_JSON = READ_URL.json()
                        
        EVENTS_JSON = READ_JSON["events"]
                 
                 
        for x_range in range(count_search):
            
                            
            EVENT_TITLE = EVENTS_JSON[x_range]["title"]
            EVENT_DATE = EVENTS_JSON[x_range]["geometry"][0]["date"]
            EVENTS_LAT = EVENTS_JSON[x_range]["geometry"][0]["coordinates"][1]
            EVENTS_LON = EVENTS_JSON[x_range]["geometry"][0]["coordinates"][0]
            
            time.sleep(0.8)
            print("\n")
            print("TITLE: ",EVENT_TITLE)
            print("DATE: ",EVENT_DATE)
            print("LATITUDE: ",EVENTS_LAT)
            print("LONGITUDE: ",EVENTS_LON)
            print("--"*10)
            
    except:
        
        print("\n")
        print("THERE IS A CONNECTION PROBLEM, IT MAY BE ABOUT YOUR INTERNET CONNECTION OR DATABASE")
        time.sleep(0.5)
        print("PLEASE CHECK YOUR CONNECTION AND TRY AGAIN")
        print("\n")
        time.sleep(0.7)
