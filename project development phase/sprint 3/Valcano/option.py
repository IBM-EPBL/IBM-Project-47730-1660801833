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
