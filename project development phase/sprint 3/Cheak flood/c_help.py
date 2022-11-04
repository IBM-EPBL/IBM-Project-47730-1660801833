def how_to_use():
    
    try:
        
        MY_TEXT = "ISC INITIATIVE"
    
        MY_FONT = ImageFont.truetype("verdanab.ttf", 11)
        MY_SIZE = MY_FONT.getsize(MY_TEXT)
        
        MY_IMG = Image.new("1",MY_SIZE,"black")
        DRAW_FUNC = ImageDraw.Draw(MY_IMG)
        DRAW_FUNC.text((0, 0), MY_TEXT, "white", font=MY_FONT)
        
        PIX_RES = np.array(MY_IMG, dtype=np.uint8)
        CHAR_RES = np.array([' ','#'], dtype="U1")[PIX_RES]
        
        STR_RES = CHAR_RES.view('U' + str(CHAR_RES.shape[1])).flatten()
        print("\n".join(STR_RES))
        
    except:
        
        pass
    
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
          
          python SCRIPT.py -h (for help)
          python SCRIPT.py -R (for latest cyclone report)
          python SCRIPT.py -E (for alternative earthquake portal)
          python SCRIPT.py --earthquakealternative (for alternative earthquake portal)
          python SCRIPT.py --reportcyclone (for latest cyclone report)
          python SCRIPT.py -e 10 (for earthquake)
          python SCRIPT.py --earthquake 10 (for earthquake)
          python SCRIPT.py -l thunder 25 (for thunder local)
          python SCRIPT.py --localalert thunder 25 (for thunder local)
          python SCRIPT.py -C 31.425 44.123 (for earthquake checking)
          python SCRIPT.py --checkearthquake 31.425 44.123 (for tearthquake checking)
          python SCRIPT.py -U SPAIN (for latest alert from countries)
          python SCRIPT.py --lastalert SPAIN (for latest alert from countries)
          
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
