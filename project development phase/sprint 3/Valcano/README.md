# CEI Natural Disaster Tracking Portal
(cc) Climatic Eye of ISCI



_We are an initiative that conducts studies in the field of Space Science,
publishes projects and reports, offers analytical perspectives and data analysis to stop the global climate catastrophe._

_This software network was created by ISCI-Lab to detect natural disasters on the planet._

_It is completely open source and open to suggestions and edits from all developers._

_Each function can be edited and run when necessary. If you want to run the whole code, run the CEI_NDT.py in your panel._


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
