import subprocess 
import math 
from itertools import count

def distance_interpolation(rssi): 
      c_dat = -2*math.pow((rssi-64.886),2)*0.000947957
      d = 0.401+(-0.3534)*math.pow(2.718,c_dat)  
      return d 
def distance_RSSI(Pt,Pl,rssi): 
      A = Pt-Pl 
      c_dat = (A-rssi)*0.014336239
      d = math.pow(10,c_dat) 
      return d  
       
for r in count(0):
   bssid_list = subprocess.check_output("iwlist scanning",shell=True)
   data_raw_decode = bssid_list.decode() # decode the raw data 
   BSSID_key_search = ['Quality', 'Signal level']
   #Finding the Signal strange from the list index
   for i in data_raw_decode.split(":"): 
         #print(i.split("=")) 
         try:
           #print(i.split("=")) 
           if len(i.split("=")) == 3:
                    #print(i.split("="),i.split("=")[1].split(" ")[0],i.split("=")[2].split("\n")[0].split(" ")[0])
                    rssi = int(i.split("=")[2].split("\n")[0].split(" ")[0])
                    Pl = int(i.split("=")[1].split(" ")[0].split("/")[0])
                    Pt = int(i.split("=")[1].split(" ")[0].split("/")[1])
                    #distance = distance_interpolation(rssi)
                    distance = distance_RSSI(Pt,Pl,rssi)
                    print("Output distance ",Pt,Pl,rssi," dbm",distance-2.55," m")
           #print(i.split("=")[0])   #Quality
           #if i.split("=")[0].split("\n")[1] == BSSID_key_search[0]: 
           #          print("RSSI level",i.split("=")[1])
         except: 
              pass 
