"""
(cc) Creative Commons / 2020-2021 ISCI - LAB DEVELOPERS
We are an initiative that conducts studies in the field of Space Science, publishes projects and reports, offers analytical perspectives and data analysis to stop the global climate catastrophe.
We believe that science changes the future.
initiative.isc@protonmail.com
initiative.isc@tutanota.com
"""

from __future__ import print_function

try:
    
    from PIL import Image, ImageDraw, ImageFont
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
