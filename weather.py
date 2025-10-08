#
import requests
import json
from datetime import datetime

limit = '1000'

# noaa weather data coded:  https://www.ncei.noaa.gov/pub/data/ghcn/daily/ghcnd-stations.txt

token = 'SQiYKAUlUnZLRYHYwUbdEbRnVIeVdfvA'
#url = "http://www.ncei.noaa.gov/cdo-web/api/v2/stations=WXK31&startdate=2024-01-04&enddate=2024-01-05"


#get all texas stations with and offset 
url = 'https://www.ncei.noaa.gov/cdo-web/api/v2/stations?locationid=FIPS:48&limit=1000&offset=1000'

url = 'https://www.ncei.noaa.gov/cdo-web/api/v2/stations?locationid=FIPS:48&limit=1000'
#url = 'https://www.ncei.noaa.gov/cdo-web/api/v2/stations?locationid=FIPS:48009'

#get daily summaries 
#url = ' https://www.ncei.noaa.gov/cdo-web/api/v2/data?datasetid=GHCND&stationid=GHCND:USC00418139&startdate=2024-01-01&enddate=2024-01-31&limit=1000'


#NORMAL_DLY
url = ' https://www.ncei.noaa.gov/cdo-web/api/v2/data?datasetid=NORMAL_DLY&stationid=GHCND:USC00418139'

#url = "http://www.ncei.noaa.gov/cdo-web/api/v2/COOP:COOP:419729"

#Local GHCND List
#Complete List
'''
US1TXBZS004  30.6389  -96.3222   90.8 TX COLLEGE STATION 2.7 NNW                     
US1TXBZS012  30.5650  -96.2856   89.9 TX COLLEGE STATION 2.9 SSE                     
US1TXBZS013  30.5836  -96.3138   89.3 TX COLLEGE STATION 1.2 S                       
US1TXBZS017  30.6035  -96.2862   83.2 TX COLLEGE STATION 1.6 E                       
US1TXBZS020  30.6186  -96.2862   80.2 TX COLLEGE STATION 2.0 NE                      
US1TXBZS022  30.6190  -96.2980   85.0 TX COLLEGE STATION 1.5 NE                      
US1TXBZS034  30.6161  -96.3351  100.6 TX COLLEGE STATION 1.7 NW                      
US1TXBZS040  30.6277  -96.2089   70.4 TX COLLEGE STATION 6.4 ENE                     
US1TXBZS041  30.5636  -96.2873   93.6 TX COLLEGE STATION 3.0 SSE                     
US1TXBZS042  30.6188  -96.3373  104.2 TX COLLEGE STATION 1.9 NW                      
US1TXBZS043  30.6207  -96.3238   93.9 TX COLLEGE STATION 1.6 NNW                     
US1TXBZS050  30.5940  -96.3270   92.0 TX COLLEGE STATION 1.0 WSW                     
US1TXBZS062  30.6611  -96.3147   86.0 TX BRYAN 3.0 E                                 
US1TXBZS075  30.6014  -96.3145   85.6 TX COLLEGE STATION 0.1 WNW                     
US1TXBZS077  30.6470  -96.3237   88.4 TX BRYAN 2.9 ESE                               
US1TXBZS083  30.6236  -96.3479   99.1 TX COLLEGE STATION 2.6 NW                      
US1TXBZS088  30.7138  -96.3902  111.3 TX BRYAN 3.5 NNW                               
US1TXBZS092  30.5774  -96.3146   93.0 TX COLLEGE STATION 1.6 S                       
US1TXBZS096  30.6042  -96.3284   96.0 TX COLLEGE STATION 1.0 WNW                     
US1TXBZS097  30.6240  -96.3199   97.5 TX COLLEGE STATION 1.7 NNW                     
US1TXBZS098  30.7714  -96.3734  104.5 TX BRYAN 7.1 N                                 
US1TXBZS099  30.6216  -96.3990   93.9 TX BRYAN 3.8 SSW                               
US1TXBZS100  30.5595  -96.3711   82.9 TX COLLEGE STATION 4.5 SW                      
US1TXBZS102  30.6338  -96.3510  108.2 TX BRYAN 2.5 SSE                               
US1TXBZS103  30.5994  -96.3257   97.5 TX COLLEGE STATION 0.8 W                       
US1TXBZS104  30.5728  -96.3002   96.6 TX COLLEGE STATION 2.0 SSE                     
US1TXBZS106  30.6928  -96.2822   92.4 TX BRYAN 5.2 ENE                               
US1TXBZS107  30.5647  -96.2791   95.1 TX COLLEGE STATION 3.2 SE                      
US1TXBZS109  30.6259  -96.2948   80.5 TX COLLEGE STATION 2.0 NNE                     
US1TXBZS111  30.6204  -96.4000   97.8 TX BRYAN 3.9 SSW                               
US1TXBZS112  30.5189  -96.2967   88.7 TX COLLEGE STATION 5.7 S                       
US1TXBZS114  30.5180  -96.2970   88.7 TX COLLEGE STATION 5.8 S                       
US1TXBZS117  30.5373  -96.2000   73.5 TX COLLEGE STATION 8.0 ESE                     
US1TXBZS118  30.6226  -96.2846   81.4 TX COLLEGE STATION 2.3 NE                      
US1TXBZS120  30.6361  -96.2611   86.6 TX COLLEGE STATION 3.9 NE                      
US1TXBZS123  30.6885  -96.1966   79.6 TX BRYAN 10.1 E                                
US1TXBZS125  30.6540  -96.3082   88.7 TX BRYAN 3.5 ESE                               
US1TXBZS127  30.5971  -96.2786   81.1 TX COLLEGE STATION 2.0 E                       
US1TXBZS128  30.6534  -96.3117   83.8 TX BRYAN 3.3 ESE                               
US1TXBZS129  30.5947  -96.2728   82.6 TX COLLEGE STATION 2.4 E                       
US1TXBZS131  30.6543  -96.3531   97.2 TX BRYAN 1.2 SE                                
US1TXBZS133  30.6068  -96.3298   95.7 TX COLLEGE STATION 1.1 WNW                     
US1TXBZS134  30.5793  -96.3055   93.6 TX COLLEGE STATION 1.5 SSE                     
US1TXBZS136  30.7140  -96.2215   84.1 TX BRYAN 9.1 ENE   
'''

station = 'US1TXBZS118'
start_date = '2024-04-01'
end_date = '2024-04-03'
#get all available data sets 
url = 'https://www.ncei.noaa.gov/cdo-web/api/v2/datasets?stationid=GHCND:'+station
#url = 'https://www.ncei.noaa.gov/cdo-web/api/v2/data?datasetid=GHCND&stationid=GHCND:'+station+'&startdate='+start_date+'&enddate='+end_date

headers = {"token":token}

r = requests.get(url, "dataset", headers = headers).text
print(r)
response = json.loads(r)
response_meta = response['metadata']
response = response['results']
#response = response[0]
print(response)
print(response_meta)

with open("daily_College_Station.json", "w") as f:
	json.dump(response, f)