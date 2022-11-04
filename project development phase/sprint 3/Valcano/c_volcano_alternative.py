def get_alternative_volcano():
    
    TARGET_REQ_URL = "https://volcano.si.edu/news/WeeklyVolcanoRSS.xml"
    
    try:
        
        REQ_TARGET = requests.get(TARGET_REQ_URL).text
        SOUP_TARGET = BeautifulSoup(REQ_TARGET,"html.parser")
        
        FIND_ALL_ITE = SOUP_TARGET.find_all("item")
        
        
        for x_loop in FIND_ALL_ITE:
            
            TITLE_OUT = x_loop.find("title")
            DES_OUT = x_loop.find("description")
            COOR_OUT = x_loop.find("georss:point")
            
            time.sleep(0.8)
            print("\n")
            print("TITLE: ",TITLE_OUT.text)
            print("DESCRIPTION: ",DES_OUT.text.replace("<p>","").replace("</p>",""))
            print("COORDINATE: ",COOR_OUT.text.replace("<p>","").replace("</p>",""))
            print("--"*10)
            
    except:
        
        print("\n")
        print("THERE IS A CONNECTION PROBLEM, IT MAY BE ABOUT YOUR INTERNET CONNECTION OR DATABASE")
        time.sleep(0.5)
        print("PLEASE CHECK YOUR CONNECTION AND TRY AGAIN")
        print("\n")
        time.sleep(0.7)
