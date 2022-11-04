def get_earthquake(count_search=int):
    
    SOURCE_URL ='https://ds.iris.edu/seismon/eventlist/index.phtml'
    
    try:
        
        MAIN_URL_REQ = requests.get(SOURCE_URL).text
        MAIN_SOUP_URL = BeautifulSoup(MAIN_URL_REQ,"html.parser")
        PARAMS_ALL_GET = MAIN_SOUP_URL.find_all("table",class_="tablesorter")
        
        i_count_stop = 0
                    
        for X_DETAIL in PARAMS_ALL_GET:
                        
            DETAIL_TR_ALL = X_DETAIL.find_all("tr")
                        
            for x_d in DETAIL_TR_ALL:
                            
                LIST_DETAIL_ALL = x_d.text.replace("\n",",").split(",")
                i_count_stop += 1
                            
                if 1 < i_count_stop < count_search:
                    
                    LIST_DETAIL_ALL[4] = float(LIST_DETAIL_ALL[4])
                    
                    if LIST_DETAIL_ALL[4] > 4.8:
                        
                        time.sleep(0.8)
                        print("\n")
                        print("IT MAY BE DANGEROUS")
                        print("MAGNITUDE: ", LIST_DETAIL_ALL[4])
                        print("LATITUDE: " + LIST_DETAIL_ALL[2])
                        print("LONGITUDE: " + LIST_DETAIL_ALL[3])
                        print("DATE: " + LIST_DETAIL_ALL[1])
                        print("DEPTH: " + LIST_DETAIL_ALL[5])
                        print("--"*10)
                        
                    else:
                        
                        time.sleep(0.8)
                        print("\n")
                        print("MAGNITUDE: ", LIST_DETAIL_ALL[4])
                        print("LATITUDE: " + LIST_DETAIL_ALL[2])
                        print("LONGITUDE: " + LIST_DETAIL_ALL[3])
                        print("DATE: " + LIST_DETAIL_ALL[1])
                        print("DEPTH: " + LIST_DETAIL_ALL[5])
                        print("--"*10)
                        
    except:
        
        print("\n")
        print("THERE IS A CONNECTION PROBLEM, IT MAY BE ABOUT YOUR INTERNET CONNECTION OR DATABASE")
        time.sleep(0.5)
        print("PLEASE CHECK YOUR CONNECTION AND TRY AGAIN")
        print("\n")
        time.sleep(0.7)
