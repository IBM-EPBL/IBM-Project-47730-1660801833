"""
(cc) Creative Commons / 2020-2021 ISCI - LAB DEVELOPERS
We are an initiative that conducts studies in the field of Space Science, publishes projects and reports, offers analytical perspectives and data analysis to stop the global climate catastrophe.
We believe that science changes the future.
initiative.isc@protonmail.com
initiative.isc@tutanota.com
"""

from __future__ import print_function

try:
    from optparse import OptionParser
    import requests
    from bs4 import BeautifulSoup
    import sys
    import time
    import numpy as np
    import warnings
        
    warnings.filterwarnings(action="ignore",message="CHECK PYTHON VERSION")
    warnings.filterwarnings(action="ignore",message="ALREADY IMPORTED",category=UserWarning)
    warnings.filterwarnings(action="ignore",category=DeprecationWarning)
    
except KeyboardInterrupt:
    
    Message_Error = "ACCESS NOT POSSIBLE"
    sys.exit(f"{Message_Error} - MISSING MODULES! PLEASE CHECK YOUR LIBRARIES AND TRY AGAIN!")
        
        


class color_select:
    # for developers
    # use for define colors within print function,
    # it could not be running with Windows,
    # use it for LINUX or other OS instead of Microsoft
    HEADER_BIG = '\033[95m'
    BLUE_COLOR = '\033[94m'
    CYAN_COLOR = '\033[96m'
    GREEN_COLOR = '\033[92m'
    WARNING_COLOR = '\033[93m'
    FAIL_OUT = '\033[91m'
    ENDC_OUT = '\033[0m'
    BOLD_OUT = '\033[1m'
    UNDERLINE_OUT = '\033[4m'

def how_to_use():

    print("\n")
    print("""
          Welcome to ISC Initiative Natural Disaster Tracking Panel
          This program has been produced by ISCI-Lab and monitors natural disasters
          
          The resources used are up to date. Data flows from various sources.
          Although the results you will see are highly verified, but it is useful to confirm.
          
          HOW TO USE
          Basic command option I: python <script_name>.py -<short_parameters_you_want_to_use> <number_of_call>
          Basic command option II: python <script_name>.py --<long_parameters_you_want_to_use> <number_of_call>
          Basic command option III: python <script_name>.py -<short_parameters_you_want_to_use> <type_of_call>
          Basic command option IV: python <script_name>.py --<long_parameters_you_want_to_use> <type_of_call>
          Basic command option V: python <script_name>.py -<short_parameters_you_want_to_use>
          Basic command option VI: python <script_name>.py --<long_parameters_you_want_to_use>
          
          EXAMPLE
          Please write the parameters completely and accurately. It is case sensitive.
          
          python CEI_NDT.py -h (for help)
          python CEI_NDT.py -R (for latest cyclone report)
          python CEI_NDT.py -E (for alternative earthquake portal)
          python CEI_NDT.py --earthquakealternative (for alternative earthquake portal)
          python CEI_NDT.py --reportcyclone (for latest cyclone report)
          python CEI_NDT.py -e 10 (for earthquake)
          python CEI_NDT.py --earthquake 10 (for earthquake)
          python CEI_NDT.py -l thunder 25 (for thunder local)
          python CEI_NDT.py --localalert thunder 25 (for thunder local)
          python CEI_NDT.py -C 31.425 44.123 (for earthquake checking)
          python CEI_NDT.py --checkearthquake 31.425 44.123 (for tearthquake checking)
          python CEI_NDT.py -U SPAIN (for latest alert from countries)
          python CEI_NDT.py --lastalert SPAIN (for latest alert from countries)
          
          LOCAL ALERT TYPES
          thunder
          rain
          fog
          gale
          
          PARAMETERS
          -e / --earthquake : Check earthquake
          -f / --flood : Check flood
          -c / --cyclone : Check cyclone
          -v / --volcano : Check volcano
          -d / --drought : Check drought
          -w / --wildfire : Check wildfire
          -n / --nasaeonet : Check NASA EONET
          -l / --localalert : Check latest local alert
          -h / --help : Help
          
          -E / --earthquakealternative : Check alternative earthquake portal
          -V / --volcanoalternative : Check alternative volcano portal
          -R / --reportcyclone: Check latest cyclone report
          -S / --seismicactivities: Check seismic activities and center data
          
          -C / --checkearthquake: Check earthquake based on coordinate
          -U / --lastalert: Check latest alert from countries
          
          FOR LAST ALERT
          This section shows the last warning issued by the weather observation departments of the countries.
          Although most countries are on the list, some countries do not provide data flow.
          For regions with names longer than one word, add '_' without any spaces between the words.
          
          NOTE
          Don't forget to check the file location if you get an additional error.
          If you cannot run it with 'python' or 'py', please try 'python3'.""")

    print("\n")
    
    
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
                    

def get_volcano(count_search=int):
    
    try:
        
        GDACS_TARGET = requests.get("https://www.gdacs.org/default.aspx").text
        SOUP_GDACS = BeautifulSoup(GDACS_TARGET,"html.parser")
        ALL_V_DISASTER = SOUP_GDACS.find_all("div",id="mainListVo")  
        CONTROL_VALUE_LIST = []
        i_count_stop = 0
    
                        
        for x_att in ALL_V_DISASTER:
                    
            ALERT_DETAIL_LINK = x_att.find_all("a")
                    
            for x_detail_link in ALERT_DETAIL_LINK:
                        
                LINK_AFTER_SITE = str(x_detail_link.get("href"))
              
                SUB_TARGET = requests.get(LINK_AFTER_SITE).text
                SOUP_TARGET = BeautifulSoup(SUB_TARGET,"html.parser")
                SUB_TARGET_DIV = SOUP_TARGET.find_all("div",id="alert_summary_left")
                                    
                                    
                if i_count_stop <= count_search:
                   
                    i_count_stop += 1
                                        
                    for x_sub_target in SUB_TARGET_DIV:
                                             
                        FIND_TR_ALL = x_sub_target.find_all("td")
                                            
                        for x_sub_td in FIND_TR_ALL:
                            ALL_INFO_TEXT = x_sub_td.text
                            CONTROL_VALUE_LIST.append(ALL_INFO_TEXT.replace("\n","").replace("\n",""))
                                    
                        NA_TAR = CONTROL_VALUE_LIST[3]
                        C_C_TAR = CONTROL_VALUE_LIST[5]
                        C_C_TAR_2 = CONTROL_VALUE_LIST[7]
                        DATE_TAR_V = CONTROL_VALUE_LIST[9]
                        E_V = CONTROL_VALUE_LIST[11]
                        E_V_2 = CONTROL_VALUE_LIST[13]
                        
                        time.sleep(0.8)
                        print("\n")
                        print("NAME: " + NA_TAR)
                        print("DETAIL: " + C_C_TAR)
                        print("DETAIL: " + C_C_TAR_2)
                        print("DETAIL: " + DATE_TAR_V)
                        print("DETAIL: " + E_V)
                        print("DETAIL: " + E_V_2)
                        print("--"*10)
                        
                        CONTROL_VALUE_LIST = []
                        
    except:
        
        print("\n")
        print("THERE IS A CONNECTION PROBLEM, IT MAY BE ABOUT YOUR INTERNET CONNECTION OR DATABASE")
        time.sleep(0.5)
        print("PLEASE CHECK YOUR CONNECTION AND TRY AGAIN")
        print("\n")
        time.sleep(0.7)
                        
                    
                        
def get_cyclone(count_search=int):
    
    try:
    
        GDACS_TARGET = requests.get("https://www.gdacs.org/default.aspx").text
        SOUP_GDACS = BeautifulSoup(GDACS_TARGET,"html.parser")
        ALL_C_DISASTER = SOUP_GDACS.find_all("div",id="mainListTc")
        CONTROL_VALUE_LIST = []
        i_count_stop = 0
        
        
        for x_att in ALL_C_DISASTER:
            
            ALERT_DETAIL_LINK = x_att.find_all("a")
                
            for x_detail_link in ALERT_DETAIL_LINK:
                
                LINK_AFTER_SITE = str(x_detail_link.get("href"))
                SUB_TARGET = requests.get(LINK_AFTER_SITE).text
                SOUP_GDACS_FUNCTION = BeautifulSoup(SUB_TARGET,"html.parser")
                SUB_TARGET_SOUP = SOUP_GDACS_FUNCTION.find_all("div",id="alert_summary_left")
                
                if i_count_stop <= count_search:
                        
                    i_count_stop += 1
                        
                    for x_sub_target in SUB_TARGET_SOUP:
                            
                        FIND_TR_ALL = x_sub_target.find_all("td")
                            
                        for x_sub_td in FIND_TR_ALL:
                            ALL_INFO_TEXT = x_sub_td.text
                            CONTROL_VALUE_LIST.append(ALL_INFO_TEXT.replace("\n","").replace("\n",""))
                   
                        time.sleep(0.8)   
                        print("\n")
                        print("NAME: ",CONTROL_VALUE_LIST[3])
                        print("DETAIL: ",CONTROL_VALUE_LIST[5])
                        print("DETAIL: ",CONTROL_VALUE_LIST[7])
                        print("DETAIL: ",CONTROL_VALUE_LIST[11])
                        print("--"*10)
                            
                        CONTROL_VALUE_LIST = []
                        
    except:
        
        print("\n")
        print("THERE IS A CONNECTION PROBLEM, IT MAY BE ABOUT YOUR INTERNET CONNECTION OR DATABASE")
        time.sleep(0.5)
        print("PLEASE CHECK YOUR CONNECTION AND TRY AGAIN")
        print("\n")
        time.sleep(0.7)
                        

def get_flood(count_search=int):
    
    try:
    
        GDACS_TARGET = requests.get("https://www.gdacs.org/default.aspx").text
        SOUP_GDACS = BeautifulSoup(GDACS_TARGET,"html.parser")
        ALL_F_DISASTER = SOUP_GDACS.find_all("div",id="mainListFl")
                
        CONTROL_VALUE_LIST = []
          
        i_count_stop = 0
    
                        
        for x_att in ALL_F_DISASTER:
                    
            ALERT_DETAIL_LINK = x_att.find_all("a")
                    
            for x_detail_link in ALERT_DETAIL_LINK:
                        
                LINK_AFTER_SITE = str(x_detail_link.get("href"))
              
                SUB_TARGET = requests.get(LINK_AFTER_SITE).text
                SOUP_GDACS_FUNCTION = BeautifulSoup(SUB_TARGET,"html.parser")
                SUB_TARGET_SOUP = SOUP_GDACS_FUNCTION.find_all("div",id="alert_summary_left")
                                    
                                    
                if i_count_stop <= count_search:
                                             
                    i_count_stop += 1
                                        
                    for x_sub_target in SUB_TARGET_SOUP:
                                             
                        FIND_TR_ALL = x_sub_target.find_all("td")
                                            
                        for x_sub_td in FIND_TR_ALL:
                            ALL_INFO_TEXT = x_sub_td.text
                            CONTROL_VALUE_LIST.append(ALL_INFO_TEXT.replace("\n","").replace("\n",""))
                                    
                        DE_TAR = CONTROL_VALUE_LIST[3]
                        DI_TAR = CONTROL_VALUE_LIST[5]
                        LOC_TAR = CONTROL_VALUE_LIST[7]
                        DATE_TAR_F = CONTROL_VALUE_LIST[9]
                        
                        time.sleep(0.8)
                        print("\n")
                        print("DEATH: ",DE_TAR)
                        print("DISPLACED: ",DI_TAR)
                        print("LOCATION: ",LOC_TAR)
                        print("DATE: ",DATE_TAR_F)
                        print("--"*10)
                        
                        CONTROL_VALUE_LIST = []
                        
    except:
        
        print("\n")
        print("THERE IS A CONNECTION PROBLEM, IT MAY BE ABOUT YOUR INTERNET CONNECTION OR DATABASE")
        time.sleep(0.5)
        print("PLEASE CHECK YOUR CONNECTION AND TRY AGAIN")
        print("\n")
        time.sleep(0.7)

def get_drought(count_search=int):
    
    try:
        
        GDACS_TARGET = requests.get("https://www.gdacs.org/default.aspx").text
        SOUP_GDACS = BeautifulSoup(GDACS_TARGET,"html.parser")
        ALL_D_DISASTER = SOUP_GDACS.find_all("div",id="mainListDr")
                
        CONTROL_VALUE_LIST = []
          
        i_count_stop = 0
                
    
        for x_att in ALL_D_DISASTER:
                    
            ALERT_DETAIL_LINK = x_att.find_all("a")
                    
            for x_detail_link in ALERT_DETAIL_LINK:
                        
                LINK_AFTER_SITE = str(x_detail_link.get("href"))
              
                SUB_TARGET = requests.get(LINK_AFTER_SITE).text
                SOUP_GDACS_FUNCTION = BeautifulSoup(SUB_TARGET,"html.parser")
                SUB_TARGET_SOUP = SOUP_GDACS_FUNCTION.find_all("div",id="alert_summary_left")
                                    
                                    
                if i_count_stop <= count_search:
                    
                    i_count_stop += 1
                                        
                    for x_sub_target in SUB_TARGET_SOUP:
                                             
                        FIND_TR_ALL = x_sub_target.find_all("td")
                                            
                        for x_sub_td in FIND_TR_ALL:
                            ALL_INFO_TEXT = x_sub_td.text
                            CONTROL_VALUE_LIST.append(ALL_INFO_TEXT.replace("\n","").replace("\n",""))
                                    
                        NA_TAR = CONTROL_VALUE_LIST[3]
                        C_C_TAR_2 = CONTROL_VALUE_LIST[7]
                        DATE_TAR_V = CONTROL_VALUE_LIST[9]
                        E_V = CONTROL_VALUE_LIST[11]
                        E_V_2 = CONTROL_VALUE_LIST[13]
                        
                        time.sleep(0.8)
                        print("\n")
                        print("NAME: ",NA_TAR)
                        print("DETAIL: ",C_C_TAR_2)
                        print("DETAIL: ",DATE_TAR_V)
                        print("DETAIL: ",E_V)
                        print("DETAIL: ",E_V_2)
                        print("--"*10)
                        
                        CONTROL_VALUE_LIST = []
                        
    except:
        
        print("\n")
        print("THERE IS A CONNECTION PROBLEM, IT MAY BE ABOUT YOUR INTERNET CONNECTION OR DATABASE")
        time.sleep(0.5)
        print("PLEASE CHECK YOUR CONNECTION AND TRY AGAIN")
        print("\n")
        time.sleep(0.7)
                    
def get_wildfire(count_search=int):
    
    try:
        
        GDACS_TARGET = requests.get("https://www.gdacs.org/default.aspx").text
        SOUP_GDACS = BeautifulSoup(GDACS_TARGET,"html.parser")
        ALL_W_DISASTER = SOUP_GDACS.find_all("div",id="mainListWF")
                
        CONTROL_VALUE_LIST = []
          
        i_count_stop = 0
    
                        
        for x_att in ALL_W_DISASTER:
                    
            ALERT_DETAIL_LINK = x_att.find_all("a")
                    
            for x_detail_link in ALERT_DETAIL_LINK:
                        
                LINK_AFTER_SITE = str(x_detail_link.get("href"))
              
                SUB_TARGET = requests.get(LINK_AFTER_SITE).text
                SOUP_GDACS_FUNCTION = BeautifulSoup(SUB_TARGET,"html.parser")
                SUB_TARGET_SOUP = SOUP_GDACS_FUNCTION.find_all("div",id="alert_summary_left")
                                    
                                    
                if i_count_stop <= count_search:
                    
                            
                    i_count_stop += 1
                                        
                    for x_sub_target in SUB_TARGET_SOUP:
                                             
                        FIND_TR_ALL = x_sub_target.find_all("td")
                                            
                        for x_sub_td in FIND_TR_ALL:
                            ALL_INFO_TEXT = x_sub_td.text
                            CONTROL_VALUE_LIST.append(ALL_INFO_TEXT.replace("\n","").replace("\n",""))
                                    
                        NA_TAR = CONTROL_VALUE_LIST[3]
                        C_C_TAR = CONTROL_VALUE_LIST[5]
                        C_C_TAR_2 = CONTROL_VALUE_LIST[7]
                        DATE_TAR_V = CONTROL_VALUE_LIST[9]
                        E_V = CONTROL_VALUE_LIST[11]
                        
                        time.sleep(0.8)
                        print("\n")
                        print("NAME: ",NA_TAR)
                        print("DATE: ",C_C_TAR)
                        print("DURATION DAYS: ",C_C_TAR_2)
                        print("PEOPLE AFFECTED: ",DATE_TAR_V)
                        print("BURNED AREA: ",E_V)
                        print("--"*10)
                        
                        CONTROL_VALUE_LIST = []
                        
    except:
        
        print("\n")
        print("THERE IS A CONNECTION PROBLEM, IT MAY BE ABOUT YOUR INTERNET CONNECTION OR DATABASE")
        time.sleep(0.5)
        print("PLEASE CHECK YOUR CONNECTION AND TRY AGAIN")
        print("\n")
        time.sleep(0.7)


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
        

def get_latest_cyclone_report():
    
    TARGET_REQ_URL = "https://www.cyclocane.com/tropical-storm-risk/"
    
    try:
        
        REQ_TARGET = requests.get(TARGET_REQ_URL).text
        SOUP_TARGET = BeautifulSoup(REQ_TARGET,"html.parser")
        
        FIND_ALL_PRE = SOUP_TARGET.find_all("pre")
        
        LIST_ALL_RES = []
        for x_loop in FIND_ALL_PRE:
            
            CLEAR_OUT = x_loop.text.replace("$$","")
            LIST_ALL_RES.append(CLEAR_OUT)
            
        for x_num_in,x_list_in in enumerate(LIST_ALL_RES):
            
            time.sleep(0.8)
            print("\n")
            print(LIST_ALL_RES[x_num_in])
            print("--"*10)
            
    except:
        
        print("\n")
        print("THERE IS A CONNECTION PROBLEM, IT MAY BE ABOUT YOUR INTERNET CONNECTION OR DATABASE")
        time.sleep(0.5)
        print("PLEASE CHECK YOUR CONNECTION AND TRY AGAIN")
        print("\n")
        time.sleep(0.7)
        

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



def EUROPE_REGION_ALERT(country_type=str):
    
    URL_TARGET = f"https://feeds.meteoalarm.org/feeds/meteoalarm-legacy-atom-{country_type}"
    REQ_TARGET = requests.get(URL_TARGET).text
    SOUP_TARGET = BeautifulSoup(REQ_TARGET,"html.parser")
    

    AREA_TARGET = "cap:areadesc"
    AREA_EVENT = "cap:event"
    AREA_ONSET = "cap:expires"
    AREA_URGENCY = "cap:urgency"
    
    FIND_TARGET = SOUP_TARGET.find_all(AREA_TARGET)[-1]
    FIND_EVENT = SOUP_TARGET.find_all(AREA_EVENT)[-1]
    FIND_ONSET = SOUP_TARGET.find_all(AREA_ONSET)[-1]
    FIND_URGENCY = SOUP_TARGET.find_all(AREA_URGENCY)[-1]
    
    time.sleep(0.8)
    print("\n")
    print("TARGET: ", FIND_TARGET.text)
    print("EVENT: ", FIND_EVENT.text)
    print("ONSET: ", FIND_ONSET.text)
    print("URGENCY: ", FIND_URGENCY.text)
    print("\n")
    
    
    
  
def BRAZIL_REGION_ALERT():
    URL_TARGET = "https://apiprevmet3.inmet.gov.br/avisos/rss"
    REQ_TARGET = requests.get(URL_TARGET).text
    SOUP_TARGET = BeautifulSoup(REQ_TARGET,"html.parser")
    
    ITEM_ALL_CLASS = SOUP_TARGET.find_all("item")
    
    i_index_c = 0
    EVENT_LIST = []
    
    for X_LOOP_DIV in ITEM_ALL_CLASS:
    
        TD_ALL = X_LOOP_DIV.find_all("td")
        
        for X_SINGLE in TD_ALL:
            i_index_c += 1
            
            if 1 < i_index_c <= 6:
                
                EVENT_LIST.append(X_SINGLE.text)
                
                
    TYPE_TARGET = EVENT_LIST[0]
    STATUS_TARGET = EVENT_LIST[1]
    FIRST_DATE_TARGET = EVENT_LIST[2]
    SECOND_DATE_TARGET = EVENT_LIST[3]
    INFO_DATE = EVENT_LIST[4]
    
    time.sleep(0.8)
    print("\n")
    print("TARGET: ", TYPE_TARGET)
    print("STATUS: ", STATUS_TARGET)
    print("FIRST DATE: ", FIRST_DATE_TARGET)
    print("SECOND DATE: ", SECOND_DATE_TARGET)
    print("INFO: ", INFO_DATE)
    print("\n")



def CHINA_REGION_ALERT():
    URL_TARGET = "http://alert-feed.worldweather.org/cn-cma-xx/rss.xml"
    REQ_TARGET = requests.get(URL_TARGET).text
    SOUP_TARGET = BeautifulSoup(REQ_TARGET,"html.parser")
    
    EVENT_LIST = []
    ITEM_ALL_CLASS = SOUP_TARGET.find("item")
    
    for X_LOOP in ITEM_ALL_CLASS:
        
        for X_ATT in X_LOOP:
            
            if X_ATT != " " and 1 < len(X_ATT) and X_ATT != "\n":
                
                EVENT_LIST.append(X_ATT)
            
    
    DATE_EVENT = EVENT_LIST[-1]
    DESCRIPTION_EVENT = EVENT_LIST[-6]
    TYPE_EVENT = EVENT_LIST[0]
    
    time.sleep(0.8)
    print("\n")
    print("DATE: ", DATE_EVENT)
    print("DESCRIPTION: ", DESCRIPTION_EVENT)
    print("TYPE: ", TYPE_EVENT)
    print("\n")



def ECUADOR_REGION_ALERT():
    
    URL_TARGET = "https://cap-sources.s3.amazonaws.com/ec-inamhi-es/rss.xml"
    REQ_TARGET = requests.get(URL_TARGET).text
    SOUP_TARGET = BeautifulSoup(REQ_TARGET,"html.parser")
    
    EVENT_LIST = []
    ITEM_ALL_CLASS = SOUP_TARGET.find("item")
    
    for X_LOOP in ITEM_ALL_CLASS:
        
        for X_ATT in X_LOOP:
            
            if X_ATT != " " and 1 < len(X_ATT) and X_ATT != "\n":
                
                EVENT_LIST.append(X_ATT)
            
    
    TITLE_EVENT = EVENT_LIST[0]
    DESC_EVENT = EVENT_LIST[1].replace("\n","")
    DATE_EVENT = EVENT_LIST[-1]
    
    time.sleep(0.8)
    print("\n")
    print("TITLE: ", TITLE_EVENT)
    print("DESCRIPTION: ", DESC_EVENT)
    print("DATE: ", DATE_EVENT)
    print("\n")



def GUYANA_REGION_ALERT():
    
    URL_TARGET = "https://hydromet.gov.gy/cap/en/alerts/rss.xml"
    REQ_TARGET = requests.get(URL_TARGET).text
    SOUP_TARGET = BeautifulSoup(REQ_TARGET,"html.parser")
    
    EVENT_LIST = []
    ITEM_ALL_CLASS = SOUP_TARGET.find("item")
    
    for X_LOOP in ITEM_ALL_CLASS:
        
        for X_ATT in X_LOOP:
            
            if X_ATT != " " and 1 < len(X_ATT) and X_ATT != "\n":
                
                EVENT_LIST.append(X_ATT)
            
    
    TITLE_EVENT = EVENT_LIST[0]
    DESC_EVENT = EVENT_LIST[1].replace("\n","")
    DATE_EVENT = EVENT_LIST[-1]

    time.sleep(0.8)
    print("\n")
    print("TITLE: ", TITLE_EVENT)
    print("DESCRIPTION: ", DESC_EVENT)
    print("DATE: ", DATE_EVENT)
    print("\n")



def HONG_KONG_REGION_ALERT():
    
    URL_TARGET = "https://alerts.weather.gov.hk/V1/cap_atom.xml"
    REQ_TARGET = requests.get(URL_TARGET).text
    SOUP_TARGET = BeautifulSoup(REQ_TARGET,"html.parser")


    AREA_URGENCY = "cap:urgency"
        
    FIND_TARGET = SOUP_TARGET.find_all("title")[-1].text
    FIND_EVENT = SOUP_TARGET.find_all(AREA_URGENCY)[-1].text
    
    time.sleep(0.8)
    print("\n")
    print("TITLE: ", FIND_TARGET)
    print("DESCRIPTION: ", FIND_EVENT)
    print("\n")



def INDIA_REGION_ALERT():
    
    URL_TARGET = "https://cap-sources.s3.amazonaws.com/in-imd-en/rss.xml"
    REQ_TARGET = requests.get(URL_TARGET).text
    SOUP_TARGET = BeautifulSoup(REQ_TARGET,"html.parser")
    
    EVENT_LIST = []
    ITEM_ALL_CLASS = SOUP_TARGET.find("item")
    
    for X_LOOP in ITEM_ALL_CLASS:
        
        for X_ATT in X_LOOP:
            
            if X_ATT != " " and 1 < len(X_ATT) and X_ATT != "\n":
                
                EVENT_LIST.append(X_ATT)
            
    
    TITLE_EVENT = EVENT_LIST[0]
    DESC_EVENT = EVENT_LIST[1].replace("\n","")
    DATE_EVENT = EVENT_LIST[-1]
    
    time.sleep(0.8)
    print("\n")
    print("TITLE: ", TITLE_EVENT)
    print("DESCRIPTION: ", DESC_EVENT)
    print("DATE: ", DATE_EVENT)
    print("\n")
    
    



def INDONESIA_REGION_ALERT():
    
    URL_TARGET = "https://signature.bmkg.go.id/alert/public/rss.xml"
    REQ_TARGET = requests.get(URL_TARGET).text
    SOUP_TARGET = BeautifulSoup(REQ_TARGET,"html.parser")
    
    EVENT_LIST = []
    ITEM_ALL_CLASS = SOUP_TARGET.find("item")
    
    for X_LOOP in ITEM_ALL_CLASS:
        
        for X_ATT in X_LOOP:
            
            if X_ATT != " " and 1 < len(X_ATT) and X_ATT != "\n":
                
                EVENT_LIST.append(X_ATT)
    
    
    TITLE_EVENT = EVENT_LIST[0]
    DESC_EVENT = EVENT_LIST[-2].replace("\n","")
    DATE_EVENT = EVENT_LIST[-1]
    
    time.sleep(0.8)
    print("\n")
    print("TITLE: ", TITLE_EVENT)
    print("DESCRIPTION: ", DESC_EVENT)
    print("DATE: ", DATE_EVENT)
    print("\n")
    

    
def KENYA_REGION_ALERT():
    
    URL_TARGET = "https://cap-sources.s3.amazonaws.com/ke-kmd-en/rss.xml"
    REQ_TARGET = requests.get(URL_TARGET).text
    SOUP_TARGET = BeautifulSoup(REQ_TARGET,"html.parser")
    
    EVENT_LIST = []
    ITEM_ALL_CLASS = SOUP_TARGET.find("item")
    
    for X_LOOP in ITEM_ALL_CLASS:
        
        for X_ATT in X_LOOP:
            
            if X_ATT != " " and 1 < len(X_ATT) and X_ATT != "\n":
                
                EVENT_LIST.append(X_ATT)
    
    
    TITLE_EVENT = EVENT_LIST[0]
    DESC_EVENT = EVENT_LIST[1].replace("\n","")
    DATE_EVENT = EVENT_LIST[-1]
    
    time.sleep(0.8)
    print("\n")
    print("TITLE: ", TITLE_EVENT)
    print("DESCRIPTION: ", DESC_EVENT)
    print("DATE: ", DATE_EVENT)
    print("\n")
    


def MADAGASCAR_REGION_ALERT():
    
    URL_TARGET = "https://cap-sources.s3.amazonaws.com/mg-meteo-en/rss.xml"
    REQ_TARGET = requests.get(URL_TARGET).text
    SOUP_TARGET = BeautifulSoup(REQ_TARGET,"html.parser")
    
    EVENT_LIST = []
    ITEM_ALL_CLASS = SOUP_TARGET.find("item")
    
    for X_LOOP in ITEM_ALL_CLASS:
        
        for X_ATT in X_LOOP:
            
            if X_ATT != " " and 1 < len(X_ATT) and X_ATT != "\n":
                
                EVENT_LIST.append(X_ATT)
    
    
    TITLE_EVENT = EVENT_LIST[0]
    DESC_EVENT = EVENT_LIST[1].replace("\n","")
    DATE_EVENT = EVENT_LIST[-1]
    
    time.sleep(0.8)
    print("\n")
    print("TITLE: ", TITLE_EVENT)
    print("DESCRIPTION: ", DESC_EVENT)
    print("DATE: ", DATE_EVENT)
    print("\n")



def MALAVI_REGION_ALERT():
    
    URL_TARGET = "https://cap-sources.s3.amazonaws.com/mw-met-en/rss.xml"
    REQ_TARGET = requests.get(URL_TARGET).text
    SOUP_TARGET = BeautifulSoup(REQ_TARGET,"html.parser")
    
    EVENT_LIST = []
    ITEM_ALL_CLASS = SOUP_TARGET.find("item")
    
    for X_LOOP in ITEM_ALL_CLASS:
        
        for X_ATT in X_LOOP:
            
            if X_ATT != " " and 1 < len(X_ATT) and X_ATT != "\n":
                
                EVENT_LIST.append(X_ATT)
    
    
    TITLE_EVENT = EVENT_LIST[0]
    DESC_EVENT = EVENT_LIST[1].replace("\n","")
    DATE_EVENT = EVENT_LIST[-1]
    
    time.sleep(0.8)
    print("\n")
    print("TITLE: ", TITLE_EVENT)
    print("DESCRIPTION: ", DESC_EVENT)
    print("DATE: ", DATE_EVENT)
    print("\n")



def MONGOLIA_REGION_ALERT():
    
    URL_TARGET = "https://cap-sources.s3.amazonaws.com/mn-namem-en/rss.xml"
    REQ_TARGET = requests.get(URL_TARGET).text
    SOUP_TARGET = BeautifulSoup(REQ_TARGET,"html.parser")
    
    EVENT_LIST = []
    ITEM_ALL_CLASS = SOUP_TARGET.find("item")
    
    for X_LOOP in ITEM_ALL_CLASS:
        
        for X_ATT in X_LOOP:
            
            if X_ATT != " " and 1 < len(X_ATT) and X_ATT != "\n":
                
                EVENT_LIST.append(X_ATT)
    
    
    TITLE_EVENT = EVENT_LIST[0]
    DESC_EVENT = EVENT_LIST[1].replace("\n","")
    DATE_EVENT = EVENT_LIST[-1]
    
    time.sleep(0.8)
    print("\n")
    print("TITLE: ", TITLE_EVENT)
    print("DESCRIPTION: ", DESC_EVENT)
    print("DATE: ", DATE_EVENT)
    print("\n")



def OMAN_REGION_TARGET():
    
    URL_TARGET = "https://cap-sources.s3.amazonaws.com/om-met-en/rss.xml"
    REQ_TARGET = requests.get(URL_TARGET).text
    SOUP_TARGET = BeautifulSoup(REQ_TARGET,"html.parser")
    
    EVENT_LIST = []
    ITEM_ALL_CLASS = SOUP_TARGET.find("item")
    
    for X_LOOP in ITEM_ALL_CLASS:
        
        for X_ATT in X_LOOP:
            
            if X_ATT != " " and 1 < len(X_ATT) and X_ATT != "\n":
                
                EVENT_LIST.append(X_ATT)
    
    
    TITLE_EVENT = EVENT_LIST[0]
    DESC_EVENT = EVENT_LIST[1].replace("\n","")
    DATE_EVENT = EVENT_LIST[-1]
    
    time.sleep(0.8)
    print("\n")
    print("TITLE: ", TITLE_EVENT)
    print("DESCRIPTION: ", DESC_EVENT)
    print("DATE: ", DATE_EVENT)
    print("\n")



def RUSSIA_REGION_ALERT():
    URL_TARGET = "https://meteoinfo.ru/hmc-output/cap/cap-feed/en/atom.xml"
    REQ_TARGET = requests.get(URL_TARGET).text
    SOUP_TARGET = BeautifulSoup(REQ_TARGET,"html.parser")
    DIV_ALL_CLASS = SOUP_TARGET.find("entry")
    
    FIND_TARGET = DIV_ALL_CLASS.find_all("summary")[-1].text
    FIND_EVENT = DIV_ALL_CLASS.find_all("dc:date")[-1].text
    
    time.sleep(0.8)
    print("\n")
    print("TITLE: ", FIND_EVENT)
    print("DESCRIPTION: ", FIND_TARGET)
    print("\n")
    
    


def SAUDI_ARABIA_ALERT():
    
    URL_TARGET = "https://ncm.gov.sa/Ar/alert/Pages/feedalerts.aspx"
    REQ_TARGET = requests.get(URL_TARGET).text
    SOUP_TARGET = BeautifulSoup(REQ_TARGET,"html.parser")
    
    EVENT_LIST = []
    ITEM_ALL_CLASS = SOUP_TARGET.find("item")
    
    for X_LOOP in ITEM_ALL_CLASS:
        
        for X_ATT in X_LOOP:
            
            if X_ATT != " " and 1 < len(X_ATT) and X_ATT != "\n":
                
                EVENT_LIST.append(X_ATT)
    
    TITLE_EVENT = EVENT_LIST[1]
    DESC_EVENT = EVENT_LIST[2].replace("\n","")
    DATE_EVENT = EVENT_LIST[-1]
    
    time.sleep(0.8)
    print("\n")
    print("TITLE: ", TITLE_EVENT)
    print("DESCRIPTION: ", DESC_EVENT)
    print("DATE: ", DATE_EVENT)
    print("\n")
    

    
def SOUTH_AFRICA_ALERT():
    
    URL_TARGET = "https://caps.weathersa.co.za/Home/RssFeed"
    REQ_TARGET = requests.get(URL_TARGET).text
    SOUP_TARGET = BeautifulSoup(REQ_TARGET,"html.parser")
    
    EVENT_LIST = []
    ITEM_ALL_CLASS = SOUP_TARGET.find("item")
    
    for X_LOOP in ITEM_ALL_CLASS:
        
        for X_ATT in X_LOOP:
            
            if X_ATT != " " and 1 < len(X_ATT) and X_ATT != "\n":
                
                EVENT_LIST.append(X_ATT)
    
    
    TITLE_EVENT = EVENT_LIST[1]
    DESC_EVENT = EVENT_LIST[2].replace("\n","")
    DATE_EVENT = EVENT_LIST[-1]
    
    time.sleep(0.8)
    print("\n")
    print("TITLE: ", TITLE_EVENT)
    print("DESCRIPTION: ", DESC_EVENT)
    print("DATE: ", DATE_EVENT)
    print("\n")
    
   
def SURINAME_AFRICA_ALERT():
    URL_TARGET = "https://cap-sources.s3.amazonaws.com/sr-meteo-en/rss.xml"
    REQ_TARGET = requests.get(URL_TARGET).text
    SOUP_TARGET = BeautifulSoup(REQ_TARGET,"html.parser")
    
    EVENT_LIST = []
    ITEM_ALL_CLASS = SOUP_TARGET.find("item")
    
    for X_LOOP in ITEM_ALL_CLASS:
        
        for X_ATT in X_LOOP:
            
            if X_ATT != " " and 1 < len(X_ATT) and X_ATT != "\n":
                
                EVENT_LIST.append(X_ATT)
    
    
    TITLE_EVENT = EVENT_LIST[0]
    DESC_EVENT = EVENT_LIST[1].replace("\n","")
    DATE_EVENT = EVENT_LIST[-1]
    
    time.sleep(0.8)
    print("\n")
    print("TITLE: ", TITLE_EVENT)
    print("DESCRIPTION: ", DESC_EVENT)
    print("DATE: ", DATE_EVENT)
    print("\n")
    
    

def TANZANIA_REGION_ALERT():
    
    URL_TARGET = "https://cap-sources.s3.amazonaws.com/tz-tma-en/rss.xml"
    REQ_TARGET = requests.get(URL_TARGET).text
    SOUP_TARGET = BeautifulSoup(REQ_TARGET,"html.parser")
    
    EVENT_LIST = []
    ITEM_ALL_CLASS = SOUP_TARGET.find("item")
    
    for X_LOOP in ITEM_ALL_CLASS:
        
        for X_ATT in X_LOOP:
            
            if X_ATT != " " and 1 < len(X_ATT) and X_ATT != "\n":
                
                EVENT_LIST.append(X_ATT)
    
    
    TITLE_EVENT = EVENT_LIST[0]
    DESC_EVENT = EVENT_LIST[1].replace("\n","")
    DATE_EVENT = EVENT_LIST[-1]
    
    time.sleep(0.8)
    print("\n")
    print("TITLE: ", TITLE_EVENT)
    print("DESCRIPTION: ", DESC_EVENT)
    print("DATE: ", DATE_EVENT)
    print("\n")



def TRINIDAD_AND_TOBAGO_ALERT():
    
    URL_TARGET = "http://metproducts.gov.tt/ttms/public/api/feed?type=rss"
    REQ_TARGET = requests.get(URL_TARGET).text
    SOUP_TARGET = BeautifulSoup(REQ_TARGET,"html.parser")
    
    EVENT_LIST = []
    ITEM_ALL_CLASS = SOUP_TARGET.find("item")
    
    for X_LOOP in ITEM_ALL_CLASS:
        
        for X_ATT in X_LOOP:
            
            if X_ATT != " " and 1 < len(X_ATT) and X_ATT != "\n":
                
                EVENT_LIST.append(X_ATT)


    TITLE_EVENT = EVENT_LIST[0]
    DESC_EVENT = EVENT_LIST[2].replace("\n","")
    DATE_EVENT = EVENT_LIST[-1]
    
    time.sleep(0.8)
    print("\n")
    print("TITLE: ", TITLE_EVENT)
    print("DESCRIPTION: ", DESC_EVENT)
    print("DATE: ", DATE_EVENT)
    print("\n")



def UGANDA_REGION_ALERT():
    URL_TARGET = "https://cap-sources.s3.amazonaws.com/ug-unma-en/rss.xml"
    REQ_TARGET = requests.get(URL_TARGET).text
    SOUP_TARGET = BeautifulSoup(REQ_TARGET,"html.parser")
    
    EVENT_LIST = []
    ITEM_ALL_CLASS = SOUP_TARGET.find("item")
    
    for X_LOOP in ITEM_ALL_CLASS:
        
        for X_ATT in X_LOOP:
            
            if X_ATT != " " and 1 < len(X_ATT) and X_ATT != "\n":
                
                EVENT_LIST.append(X_ATT)


    TITLE_EVENT = EVENT_LIST[0]
    DESC_EVENT = EVENT_LIST[1].replace("\n","")
    DATE_EVENT = EVENT_LIST[-1]
    
    time.sleep(0.8)
    print("\n")
    print("TITLE: ", TITLE_EVENT)
    print("DESCRIPTION: ", DESC_EVENT)
    print("DATE: ", DATE_EVENT)
    print("\n")



def ZIMBABWE_REGION_ALERT():
    
    URL_TARGET = "https://cap-sources.s3.amazonaws.com/zw-msd-en/rss.xml"
    REQ_TARGET = requests.get(URL_TARGET).text
    SOUP_TARGET = BeautifulSoup(REQ_TARGET,"html.parser")
    
    EVENT_LIST = []
    ITEM_ALL_CLASS = SOUP_TARGET.find("item")
    
    for X_LOOP in ITEM_ALL_CLASS:
        
        for X_ATT in X_LOOP:
            
            if X_ATT != " " and 1 < len(X_ATT) and X_ATT != "\n":
                
                EVENT_LIST.append(X_ATT)
    
    
    TITLE_EVENT = EVENT_LIST[0]
    DESC_EVENT = EVENT_LIST[1].replace("\n","")
    DATE_EVENT = EVENT_LIST[-1]
    
    time.sleep(0.8)
    print("\n")
    print("TITLE: ", TITLE_EVENT)
    print("DESCRIPTION: ", DESC_EVENT)
    print("DATE: ", DATE_EVENT)
    print("\n")




    
def get_info_parameters():
    
    OPTION_FUNCTION = OptionParser(add_help_option=False,epilog="DISASTER PANEL OF ISCI")
    OPTION_FUNCTION.add_option("-e",
                               "--earthquake",
                               help="Check earthquake",
                               dest="eq_print",
                               type="int")
    OPTION_FUNCTION.add_option("-f",
                               "--flood",
                               help="Check flood",
                               dest="fl_print",
                               type="int")
    OPTION_FUNCTION.add_option("-c",
                               "--cyclone",
                               help="Check cyclone",
                               dest="cy_print",
                               type="int")
    OPTION_FUNCTION.add_option("-v",
                               "--volcano",
                               help="Check volcano",
                               dest="vo_print",
                               type="int")
    OPTION_FUNCTION.add_option("-d",
                               "--drought",
                               help="Check drought",
                               dest="dr_print",
                               type="int")
    OPTION_FUNCTION.add_option("-w",
                               "--wildfire",
                               help="Check wildfire",
                               dest="wf_print",
                               type="int")
    OPTION_FUNCTION.add_option("-n",
                               "--nasaeonet",
                               help="Check Nasa EONET",
                               dest="nasa_e_print",
                               type="int")
    OPTION_FUNCTION.add_option("-l",
                               "--localalert",
                               help="Check latest local alert",
                               dest="alert_local",
                               type="string")
    OPTION_FUNCTION.add_option("-U",
                               "--lastalert",
                               help="Check latest alert from countries",
                               dest="alert_country",
                               type="string")
    OPTION_FUNCTION.add_option("-S",
                               "--seismicactivities",
                               help="Check seismic activities and center data",
                               dest="seismic_print",
                               type="int")
    OPTION_FUNCTION.add_option("-C",
                               "--checkearthquake",
                               help="Check earthquake based on coordinate",
                               dest="check_eq_print",
                               type="float")
    OPTION_FUNCTION.add_option("-R",
                               "--reportcyclone",
                               help="Check latest cyclone report",
                               dest="cy_report_print",
                               action="store_true")
    OPTION_FUNCTION.add_option("-E",
                               "--earthquakealternative",
                               help="Check alternative earthquake portal",
                               dest="eq_al_print",
                               action="store_true")
    OPTION_FUNCTION.add_option("-V",
                               "--volcanoalternative",
                               help="Check alternative volcano portal",
                               dest="vo_al_print",
                               action="store_true")
    
    
    
    OPTION_FUNCTION.add_option("-h",
                               "--help",
                               help="Help",
                               dest="help_print",
                               action="store_true")
    
    OPTIONS_RESULT, ARG_RESULT = OPTION_FUNCTION.parse_args()
    
    
    
    if OPTIONS_RESULT.help_print:
            
            how_to_use()
            sys.exit()
            
    elif OPTIONS_RESULT.eq_print:
        
        try:
            
            print("PROCESS STATUS: RUNNING, PLEASE WAIT")
            time.sleep(1.5)
            USAGE_IN = OPTIONS_RESULT.eq_print
            USAGE_IN = int(USAGE_IN) + 2

            get_earthquake(USAGE_IN)
            print("\n")
            print("REGISTRATIONS HAVE BEEN FOUND")
            print("\n")
            
            
        except:
            
            print("\n")
            print("NOT RUNNING, PLEASE CHECK YOUR CONNECTION OR PARAMETERS")
            print("\n")
            how_to_use()
            sys.exit()
            
    elif OPTIONS_RESULT.vo_print:
        
        try:
            
            print("PROCESS STATUS: RUNNING, PLEASE WAIT")
            time.sleep(1.5)
            USAGE_IN = OPTIONS_RESULT.vo_print
            USAGE_IN = int(USAGE_IN) - 1

            get_volcano(USAGE_IN)
            print("\n")
            print("REGISTRATIONS HAVE BEEN FOUND")
            print("\n")
            
            
        except:
            
            print("\n")
            print("NOT RUNNING, PLEASE CHECK YOUR CONNECTION OR PARAMETERS")
            print("\n")
            how_to_use()
            sys.exit()
            
    elif OPTIONS_RESULT.cy_print:
        
        try:
            
            print("PROCESS STATUS: RUNNING, PLEASE WAIT")
            time.sleep(1.5)
            USAGE_IN = OPTIONS_RESULT.cy_print
            USAGE_IN = int(USAGE_IN) - 1

            get_cyclone(USAGE_IN)
            print("\n")
            print("REGISTRATIONS HAVE BEEN FOUND")
            print("\n")
            
            
        except:
            
            print("\n")
            print("NOT RUNNING, PLEASE CHECK YOUR CONNECTION OR PARAMETERS")
            print("\n")
            how_to_use()
            sys.exit()
            
    elif OPTIONS_RESULT.fl_print:
        
        try:
            
            print("PROCESS STATUS: RUNNING, PLEASE WAIT")
            time.sleep(1.5)
            USAGE_IN = OPTIONS_RESULT.fl_print
            USAGE_IN = int(USAGE_IN) - 1

            get_flood(USAGE_IN)
            print("\n")
            print("REGISTRATIONS HAVE BEEN FOUND")
            print("\n")
            
            
        except:
            
            print("\n")
            print("NOT RUNNING, PLEASE CHECK YOUR CONNECTION OR PARAMETERS")
            print("\n")
            how_to_use()
            sys.exit()
            
    elif OPTIONS_RESULT.dr_print:
        
        try:
            
            print("PROCESS STATUS: RUNNING, PLEASE WAIT")
            time.sleep(1.5)
            USAGE_IN = OPTIONS_RESULT.dr_print
            USAGE_IN = int(USAGE_IN) - 1

            get_drought(USAGE_IN)
            print("\n")
            print("REGISTRATIONS HAVE BEEN FOUND")
            print("\n")
            
            
        except:
            
            print("\n")
            print("NOT RUNNING, PLEASE CHECK YOUR CONNECTION OR PARAMETERS")
            print("\n")
            how_to_use()
            sys.exit()
            
    elif OPTIONS_RESULT.wf_print:
        
        try:
            
            print("PROCESS STATUS: RUNNING, PLEASE WAIT")
            time.sleep(1.5)
            USAGE_IN = OPTIONS_RESULT.wf_print
            USAGE_IN = int(USAGE_IN) - 1

            get_wildfire(USAGE_IN)
            print("\n")
            print("REGISTRATIONS HAVE BEEN FOUND")
            print("\n")
            
            
        except:
            
            print("\n")
            print("NOT RUNNING, PLEASE CHECK YOUR CONNECTION OR PARAMETERS")
            print("\n")
            how_to_use()
            sys.exit()
            
    elif OPTIONS_RESULT.nasa_e_print:
        
        try:
            
            print("PROCESS STATUS: RUNNING, PLEASE WAIT")
            time.sleep(1.5)
            USAGE_IN = OPTIONS_RESULT.nasa_e_print
            USAGE_IN = int(USAGE_IN)
            
            get_nasa_eonet(USAGE_IN)
            print("\n")
            print("REGISTRATIONS HAVE BEEN FOUND")
            print("\n")
            
            
        except:
            
            print("\n")
            print("NOT RUNNING, PLEASE CHECK YOUR CONNECTION OR PARAMETERS")
            print("\n")
            how_to_use()
            sys.exit()
            
    elif OPTIONS_RESULT.seismic_print:
        
        try:
            
            print("PROCESS STATUS: RUNNING, PLEASE WAIT")
            time.sleep(1.5)
            USAGE_IN = OPTIONS_RESULT.seismic_print
            USAGE_IN = int(USAGE_IN)
            
            get_seismic_data(USAGE_IN)
            print("\n")
            print("REGISTRATIONS HAVE BEEN FOUND")
            print("\n")
            
            
        except:
            
            print("\n")
            print("NOT RUNNING, PLEASE CHECK YOUR CONNECTION OR PARAMETERS")
            print("\n")
            how_to_use()
            sys.exit()
            
    elif OPTIONS_RESULT.alert_local:
        
        try:
            
            print("PROCESS STATUS: RUNNING, PLEASE WAIT")
            time.sleep(1.5)
            USAGE_IN = str(OPTIONS_RESULT.alert_local).lower()
            ARG_RESULT = int(ARG_RESULT[0])
            get_local_based(USAGE_IN,ARG_RESULT)
            print("\n")
            print("REGISTRATIONS HAVE BEEN FOUND")
            print("\n")
            
            
        except:
            
            print("\n")
            print("NOT RUNNING, PLEASE CHECK YOUR CONNECTION OR PARAMETERS")
            print("\n")
            how_to_use()
            sys.exit()
            
    elif OPTIONS_RESULT.alert_country:
        
        try:
            
            print("PROCESS STATUS: RUNNING, PLEASE WAIT")
            time.sleep(1.5)
            USAGE_IN = str(OPTIONS_RESULT.alert_country).upper().replace("İ","I")
            
            if USAGE_IN == "BELGIUM":
                
                try:
                
                    print("\n")
                    print(USAGE_IN)
                    
                    time.sleep(0.8)
                    EUROPE_REGION_ALERT("belgium")
                
                except:
            
                    print("\n")
                    print(f"THERE IS NO RESPONSE FROM {USAGE_IN}")
                    print("\n")
            
            elif USAGE_IN == "BOSNA_HERZEGOVINA":
                
                try:
                
                    print("\n")
                    print(USAGE_IN)
                    
                    time.sleep(0.8)
                    EUROPE_REGION_ALERT("bosnia-herzegovina")
                
                except:
            
                    print("\n")
                    print(f"THERE IS NO RESPONSE FROM {USAGE_IN}")
                    print("\n")
                
            elif USAGE_IN == "BRAZIL":
                
                try:
                
                    print("\n")
                    print(USAGE_IN)
                    
                    time.sleep(0.8)
                    BRAZIL_REGION_ALERT()
                
                except:
            
                    print("\n")
                    print(f"THERE IS NO RESPONSE FROM {USAGE_IN}")
                    print("\n")
                
            elif USAGE_IN == "CHINA":
                
                try:
                
                    print("\n")
                    print(USAGE_IN)
                    
                    time.sleep(0.8)
                    CHINA_REGION_ALERT()
                
                except:
            
                    print("\n")
                    print(f"THERE IS NO RESPONSE FROM {USAGE_IN}")
                    print("\n")
                
            elif USAGE_IN == "CROATIA":
                
                try:
                
                    print("\n")
                    print(USAGE_IN)
                    
                    time.sleep(0.8)
                    EUROPE_REGION_ALERT("croatia")
                
                except:
            
                    print("\n")
                    print(f"THERE IS NO RESPONSE FROM {USAGE_IN}")
                    print("\n")
                
            elif USAGE_IN == "ESTONIA":
                
                try:
                
                    print("\n")
                    print(USAGE_IN)
                    
                    time.sleep(0.8)
                    EUROPE_REGION_ALERT("estonia")
                
                except:
            
                    print("\n")
                    print(f"THERE IS NO RESPONSE FROM {USAGE_IN}")
                    print("\n")
                
            elif USAGE_IN == "ECUADOR":
                
                try:
                    
                    print("\n")
                    print(USAGE_IN)
                    
                    time.sleep(0.8)
                    ECUADOR_REGION_ALERT()
                
                except:
            
                    print("\n")
                    print(f"THERE IS NO RESPONSE FROM {USAGE_IN}")
                    print("\n")
                
            elif USAGE_IN == "FINLAND":
                
                try:
                
                    print("\n")
                    print(USAGE_IN)
                    
                    time.sleep(0.8)
                    EUROPE_REGION_ALERT("finland")
                
                except:
            
                    print("\n")
                    print(f"THERE IS NO RESPONSE FROM {USAGE_IN}")
                    print("\n")
                
            elif USAGE_IN == "FRANCE":
                
                try:
                
                    print("\n")
                    print(USAGE_IN)
                    
                    time.sleep(0.8)
                    EUROPE_REGION_ALERT("france")
                
                except:
            
                    print("\n")
                    print(f"THERE IS NO RESPONSE FROM {USAGE_IN}")
                    print("\n")
                
            elif USAGE_IN == "GERMANY":
                
                try:
                
                    print("\n")
                    print(USAGE_IN)
                    
                    time.sleep(0.8)
                    EUROPE_REGION_ALERT("germany")
                
                except:
            
                    print("\n")
                    print(f"THERE IS NO RESPONSE FROM {USAGE_IN}")
                    print("\n")
                
            elif USAGE_IN == "GREECE":
                
                try:
                
                    print("\n")
                    print(USAGE_IN)
                    
                    time.sleep(0.8)
                    EUROPE_REGION_ALERT("greece")
                
                except:
            
                    print("\n")
                    print(f"THERE IS NO RESPONSE FROM {USAGE_IN}")
                    print("\n")
                
            elif USAGE_IN == "GUYANA":
                
                try:
                
                    print("\n")
                    print(USAGE_IN)
                    
                    time.sleep(0.8)
                    GUYANA_REGION_ALERT()
                
                except:
            
                    print("\n")
                    print(f"THERE IS NO RESPONSE FROM {USAGE_IN}")
                    print("\n")
                
            elif USAGE_IN == "HUNGARY":
                
                try:
                
                    print("\n")
                    print(USAGE_IN)
                    
                    time.sleep(0.8)
                    EUROPE_REGION_ALERT("hungary")
                
                except:
            
                    print("\n")
                    print(f"THERE IS NO RESPONSE FROM {USAGE_IN}")
                    print("\n")
                
            elif USAGE_IN == "HONG_KONG":
                
                try:
                
                    print("\n")
                    print(USAGE_IN)
                    
                    time.sleep(0.8)
                    HONG_KONG_REGION_ALERT()
                
                except:
            
                    print("\n")
                    print(f"THERE IS NO RESPONSE FROM {USAGE_IN}")
                    print("\n")
                
            elif USAGE_IN == "ICELAND":
                
                try:
                
                    print("\n")
                    print(USAGE_IN)
                    
                    time.sleep(0.8)
                    EUROPE_REGION_ALERT("iceland")
                
                except:
            
                    print("\n")
                    print(f"THERE IS NO RESPONSE FROM {USAGE_IN}")
                    print("\n")
                
            elif USAGE_IN == "ISRAEL":
                
                try:
                    
                    print("\n")
                    print(USAGE_IN)
                    
                    time.sleep(0.8)
                    EUROPE_REGION_ALERT("israel")
                
                except:
            
                    print("\n")
                    print(f"THERE IS NO RESPONSE FROM {USAGE_IN}")
                    print("\n")
                
            elif USAGE_IN == "ITALY":
                
                try:
                
                    print("\n")
                    print(USAGE_IN)
                    
                    time.sleep(0.8)
                    EUROPE_REGION_ALERT("italy")
                
                except:
            
                    print("\n")
                    print(f"THERE IS NO RESPONSE FROM {USAGE_IN}")
                    print("\n")
                
            elif USAGE_IN == "INDIA":
                
                try:
                
                    print("\n")
                    print(USAGE_IN)
                    
                    time.sleep(0.8)
                    INDIA_REGION_ALERT()
                
                except:
            
                    print("\n")
                    print(f"THERE IS NO RESPONSE FROM {USAGE_IN}")
                    print("\n")
                
            elif USAGE_IN == "INDONESIA":
                
                try:
                
                    print("\n")
                    print(USAGE_IN)
                    
                    time.sleep(0.8)
                    INDONESIA_REGION_ALERT()
                
                except:
            
                    print("\n")
                    print(f"THERE IS NO RESPONSE FROM {USAGE_IN}")
                    print("\n")
                
            elif USAGE_IN == "LATVIA":
                
                try:
                
                    print("\n")
                    print(USAGE_IN)
                    
                    time.sleep(0.8)
                    EUROPE_REGION_ALERT("latvia")
                
                except:
            
                    print("\n")
                    print(f"THERE IS NO RESPONSE FROM {USAGE_IN}")
                    print("\n")
                
            elif USAGE_IN == "LITHUANIA":
                
                try:
                
                    print("\n")
                    print(USAGE_IN)
                    
                    time.sleep(0.8)
                    EUROPE_REGION_ALERT("lithuania")
                
                except:
            
                    print("\n")
                    print(f"THERE IS NO RESPONSE FROM {USAGE_IN}")
                    print("\n")
                
            elif USAGE_IN == "KENYA":
                
                try:
                
                    print("\n")
                    print(USAGE_IN)
                    
                    time.sleep(0.8)
                    KENYA_REGION_ALERT()
                
                except:
            
                    print("\n")
                    print(f"THERE IS NO RESPONSE FROM {USAGE_IN}")
                    print("\n")
                
            elif USAGE_IN == "MADAGASCAR":
                
                try:
                
                    print("\n")
                    print(USAGE_IN)
                    
                    time.sleep(0.8)
                    MADAGASCAR_REGION_ALERT()
                
                except:
            
                    print("\n")
                    print(f"THERE IS NO RESPONSE FROM {USAGE_IN}")
                    print("\n")
                
            elif USAGE_IN == "MALAVI":
                
                try:
                
                    print("\n")
                    print(USAGE_IN)
                    
                    time.sleep(0.8)
                    MALAVI_REGION_ALERT()
                
                except:
            
                    print("\n")
                    print(f"THERE IS NO RESPONSE FROM {USAGE_IN}")
                    print("\n")
                
            elif USAGE_IN == "MONGOLIA":
                
                try:
                
                    print("\n")
                    print(USAGE_IN)
                    
                    time.sleep(0.8)
                    MONGOLIA_REGION_ALERT()
                
                except:
            
                    print("\n")
                    print(f"THERE IS NO RESPONSE FROM {USAGE_IN}")
                    print("\n")
                
            elif USAGE_IN == "MONTENEGRO":
                
                try:
                
                    print("\n")
                    print(USAGE_IN)
                    
                    time.sleep(0.8)
                    EUROPE_REGION_ALERT("montenegro")
                
                except:
            
                    print("\n")
                    print(f"THERE IS NO RESPONSE FROM {USAGE_IN}")
                    print("\n")
                
            elif USAGE_IN == "NETHERLANDS":
                
                try:
                
                    print("\n")
                    print(USAGE_IN)
                    
                    time.sleep(0.8)
                    EUROPE_REGION_ALERT("netherlands")
                
                except:
            
                    print("\n")
                    print(f"THERE IS NO RESPONSE FROM {USAGE_IN}")
                    print("\n")
                
            elif USAGE_IN == "NORWAY":
                
                try:
                
                    print("\n")
                    print(USAGE_IN)
                    
                    time.sleep(0.8)
                    EUROPE_REGION_ALERT("norway")
                
                except:
            
                    print("\n")
                    print(f"THERE IS NO RESPONSE FROM {USAGE_IN}")
                    print("\n")
                
            elif USAGE_IN == "PORTUGAL":
                
                try:
                
                    print("\n")
                    print(USAGE_IN)
                    
                    time.sleep(0.8)
                    EUROPE_REGION_ALERT("portugal")
                
                except:
            
                    print("\n")
                    print(f"THERE IS NO RESPONSE FROM {USAGE_IN}")
                    print("\n")
                
            elif USAGE_IN == "RUSSIA":
                
                try:
                
                    print("\n")
                    print(USAGE_IN)
                    
                    time.sleep(0.8)
                    RUSSIA_REGION_ALERT()
                
                except:
            
                    print("\n")
                    print(f"THERE IS NO RESPONSE FROM {USAGE_IN}")
                    print("\n")
                
            elif USAGE_IN == "SERBIA":
                
                try:
                
                    print("\n")
                    print(USAGE_IN)
                    
                    time.sleep(0.8)
                    EUROPE_REGION_ALERT("serbia")
                
                except:
            
                    print("\n")
                    print(f"THERE IS NO RESPONSE FROM {USAGE_IN}")
                    print("\n")
                
            elif USAGE_IN == "SLOVAKIA":
                
                try:
                
                    print("\n")
                    print(USAGE_IN)
                    
                    time.sleep(0.8)
                    EUROPE_REGION_ALERT("slovakia")
                
                except:
            
                    print("\n")
                    print(f"THERE IS NO RESPONSE FROM {USAGE_IN}")
                    print("\n")
                
            elif USAGE_IN == "SLOVENIA":
                
                try:
                
                    print("\n")
                    print(USAGE_IN)
                    
                    time.sleep(0.8)
                    EUROPE_REGION_ALERT("slovenia")
                
                except:
            
                    print("\n")
                    print(f"THERE IS NO RESPONSE FROM {USAGE_IN}")
                    print("\n")
                
            elif USAGE_IN == "SPAIN":
                
                try:
                    
                    print("\n")
                    print(USAGE_IN)
                    
                    time.sleep(0.8)
                    EUROPE_REGION_ALERT("spain")
                
                except:
            
                    print("\n")
                    print(f"THERE IS NO RESPONSE FROM {USAGE_IN}")
                    print("\n")
                
            elif USAGE_IN == "SAUDI_ARABIA":
                
                try:
                
                    print("\n")
                    print(USAGE_IN)
                    
                    time.sleep(0.8)
                    SAUDI_ARABIA_ALERT()
                
                except:
            
                    print("\n")
                    print(f"THERE IS NO RESPONSE FROM {USAGE_IN}")
                    print("\n")
                
            elif USAGE_IN == "SURINAME":
                
                try:
                
                    print("\n")
                    print(USAGE_IN)
                    
                    time.sleep(0.8)
                    SURINAME_AFRICA_ALERT()
                
                except:
            
                    print("\n")
                    print(f"THERE IS NO RESPONSE FROM {USAGE_IN}")
                    print("\n")
                
            elif USAGE_IN == "SOUTH_AFRICA":
                
                try:
                
                    print("\n")
                    print(USAGE_IN)
                    
                    time.sleep(0.8)
                    SOUTH_AFRICA_ALERT()
                
                except:
            
                    print("\n")
                    print(f"THERE IS NO RESPONSE FROM {USAGE_IN}")
                    print("\n")
                
            elif USAGE_IN == "TANZANIA":
                
                try:
                
                    print("\n")
                    print(USAGE_IN)
                    
                    time.sleep(0.8)
                    TANZANIA_REGION_ALERT()
                
                except:
            
                    print("\n")
                    print(f"THERE IS NO RESPONSE FROM {USAGE_IN}")
                    print("\n")
                
            elif USAGE_IN == "TRINIDAD_AND_TOBAGO":
                
                try:
                
                    print("\n")
                    print(USAGE_IN)
                    
                    time.sleep(0.8)
                    TRINIDAD_AND_TOBAGO_ALERT()
                
                except:
            
                    print("\n")
                    print(f"THERE IS NO RESPONSE FROM {USAGE_IN}")
                    print("\n")
                
            elif USAGE_IN == "UGANDA":
                
                try:
                    
                    print("\n")
                    print(USAGE_IN)
                    
                    time.sleep(0.8)
                    UGANDA_REGION_ALERT()
                    
                except:
            
                    print("\n")
                    print(f"THERE IS NO RESPONSE FROM {USAGE_IN}")
                    print("\n")
                
            elif USAGE_IN == "ZIMBABWE":
                
                try:
                
                    print("\n")
                    print(USAGE_IN)
                    
                    time.sleep(0.8)
                    ZIMBABWE_REGION_ALERT()
                
                except:
            
                    print("\n")
                    print(f"THERE IS NO RESPONSE FROM {USAGE_IN}")
                    print("\n")
                
            elif USAGE_IN == "OMAN":
                
                
                try:
                    
                    print("\n")
                    print(USAGE_IN)
                    
                    time.sleep(0.8)
                    OMAN_REGION_TARGET()
                
                except:
            
                    print("\n")
                    print(f"THERE IS NO RESPONSE FROM {USAGE_IN}")
                    print("\n")
                
            else:
                
                print("\n")
                print("PLEASE CHECK YOUR INPUT")
                print("\n")
            
            
        except:
            
            print("\n")
            print("NOT RUNNING, PLEASE CHECK YOUR CONNECTION OR PARAMETERS")
            print("\n")
            how_to_use()
            sys.exit()
            
    elif OPTIONS_RESULT.check_eq_print:
        
        try:
            
            print("PROCESS STATUS: RUNNING, PLEASE WAIT")
            print("\n")
            time.sleep(1.5)
            ARG_RESULT_LAT = float(OPTIONS_RESULT.check_eq_print)
            ARG_RESULT_LON = float(ARG_RESULT[0])
            print(f"TARGET COORDINATE: {ARG_RESULT_LAT} {ARG_RESULT_LON}")
            time.sleep(0.5)
            print("THIS PROCESS MAY TAKE TIME, DON'T CANCEL")
            print("\n")
            time.sleep(1.5)
            check_earthquakes_location(ARG_RESULT_LAT,ARG_RESULT_LON)
            print("\n")
            print("REGISTRATIONS HAVE BEEN FOUND")
            print("\n")
            
            
        except:
            
            print("\n")
            print("NOT RUNNING, PLEASE CHECK YOUR CONNECTION OR PARAMETERS")
            print("\n")
            how_to_use()
            sys.exit()
            
    elif OPTIONS_RESULT.cy_report_print:
        
        try:
            
            print("PROCESS STATUS: RUNNING, PLEASE WAIT")
            time.sleep(1.5)
            get_latest_cyclone_report()
            print("\n")
            print("REGISTRATIONS HAVE BEEN FOUND")
            print("\n")
            
            
        except:
            
            print("\n")
            print("NOT RUNNING, PLEASE CHECK YOUR CONNECTION OR PARAMETERS")
            print("\n")
            how_to_use()
            sys.exit()
            
    elif OPTIONS_RESULT.eq_al_print:
        
        try:
            
            print("PROCESS STATUS: RUNNING, PLEASE WAIT")
            time.sleep(1.5)
            get_alternative_earthquake()
            print("\n")
            print("REGISTRATIONS HAVE BEEN FOUND")
            print("\n")
            
            
        except:
            
            print("\n")
            print("NOT RUNNING, PLEASE CHECK YOUR CONNECTION OR PARAMETERS")
            print("\n")
            how_to_use()
            sys.exit()
            
    elif OPTIONS_RESULT.vo_al_print:
        
        try:
            
            print("PROCESS STATUS: RUNNING, PLEASE WAIT")
            time.sleep(1.5)
            get_alternative_volcano()
            print("\n")
            print("REGISTRATIONS HAVE BEEN FOUND")
            print("\n")
            
            
        except:
            
            print("\n")
            print("NOT RUNNING, PLEASE CHECK YOUR CONNECTION OR PARAMETERS")
            print("\n")
            how_to_use()
            sys.exit()
            

        
if __name__ == "__main__":
    
    if len(sys.argv) >= 1:

        get_info_parameters()
            
        
    elif len(sys.argv) == 0:
        
        how_to_use()
        
    else:
        
        pass

