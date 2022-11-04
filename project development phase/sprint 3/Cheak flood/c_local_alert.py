def get_local_based(search_parameters=str,count_search=int):
    
    TARGET_URL = f"https://severeweather.wmo.int/{search_parameters}/"
    
    try:
            
        TAR_REQ = requests.get(TARGET_URL).text
        BS_REQ = BeautifulSoup(TAR_REQ,"html.parser")
                        
        Area_ALL = BS_REQ.find_all("area")
        
        i_count_stop = 0
                     
        for x_loop_area in Area_ALL:
                            
            HREF_ALL_AREA_PATH = x_loop_area.get("href")
            REP_DOT_RAIN = HREF_ALL_AREA_PATH.replace("./","")
            ALL_PATH_RAIN = TARGET_URL + REP_DOT_RAIN
                                
            NEW_TAR_REQ = requests.get(ALL_PATH_RAIN).text
            BS_NEW_TAR = BeautifulSoup(NEW_TAR_REQ,"html.parser")
            AREA_NEW_ALL = BS_NEW_TAR.find_all("area")
                
            if i_count_stop < count_search:
                
                for new_all_loop in AREA_NEW_ALL:
                                                            
                    NEW_HREF_TARGET = new_all_loop.get("href")
                                            
                    if NEW_HREF_TARGET.startswith("javascript"):      
                                                
                        JAVA_TAR_URL_PATH = NEW_HREF_TARGET
                        SPLIT_TAR_JAVA = JAVA_TAR_URL_PATH.split("javascript:clickPopUp('./")
                        SPLIT_COMMA_JAVA = SPLIT_TAR_JAVA[1].split(",")
                        FIN_JAVA_TAR = SPLIT_COMMA_JAVA[0].replace("'","")
                        LAST_FIN_URL_ALL = TARGET_URL + REP_DOT_RAIN
                        PATH_WITH_CLEAR = LAST_FIN_URL_ALL.replace("index.html","")
                        TOGETGER_ALL_PATH = PATH_WITH_CLEAR + FIN_JAVA_TAR
                                                
                        LAST_NEW_TAR_REQ = requests.get(TOGETGER_ALL_PATH).text
                        LAST_BS_NEW_TAR = BeautifulSoup(LAST_NEW_TAR_REQ,"html.parser")
                                                
                        DIV_COOR = LAST_BS_NEW_TAR.find("td")
                                                
                        if DIV_COOR != None:
                            i_count_stop += 1
                            CLEAR_OUTPUT_LAST_RESULT = DIV_COOR.text.replace("As reported from","")
                            
                            time.sleep(0.8)
                            print("\n")
                            print(CLEAR_OUTPUT_LAST_RESULT)
                            print("--"*10)
                        

    except:
        
        print("\n")
        print("THERE IS A CONNECTION PROBLEM, IT MAY BE ABOUT YOUR INTERNET CONNECTION OR DATABASE")
        time.sleep(0.5)
        print("PLEASE CHECK YOUR CONNECTION AND TRY AGAIN")
        print("\n")
        time.sleep(0.7)
