def get_seismic_data(count_search=int):
    
    TARGET_REQ_URL = f"https://www.seismicportal.eu/mtws/api/search?&format=json&downloadAsFile=false&orderby=time-desc&offset=0&limit={count_search}"

    try:
        
        READ_URL = requests.get(TARGET_REQ_URL)
        READ_JSON = READ_URL.json()
    
        for x_num in range(len(READ_JSON)):
    
            NEW_JSON = READ_JSON[x_num]
    
            time.sleep(0.8)
            print("\n")
            print("REGION: ",NEW_JSON["ev_region"])
            print("LATITUDE: ",NEW_JSON["ev_latitude"])
            print("LONGITUDE: ",NEW_JSON["ev_longitude"])
            print("DEPTH: ",NEW_JSON["ev_depth"])
            print("MAGNITUDE VALUE: ",NEW_JSON["ev_mag_value"])
            print("MAGNITUDE TYPE: ",NEW_JSON["ev_mag_type"])
            print("EVENT TIME: ",NEW_JSON["ev_event_time"])
            print("FULL COUNT: ",NEW_JSON["full_count"])
            print("--"*10)
            
    except:
        
        print("\n")
        print("THERE IS A CONNECTION PROBLEM, IT MAY BE ABOUT YOUR INTERNET CONNECTION OR DATABASE")
        time.sleep(0.5)
        print("PLEASE CHECK YOUR CONNECTION AND TRY AGAIN")
        print("\n")
        time.sleep(0.7)
