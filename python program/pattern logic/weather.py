import  requests
import  json
import datetime as dt
print(dt.datetime.fromtimestamp(1624491535))
appid="dd6ffdb1194aadf57f688e76ad6f82c7"
city="Varanasi"
#url="https://api.openweathermap.org/data/2.5/weather?q={1}&appid={0}&units=metric".format(appid,city)
url="https://api.openweathermap.org/data/2.5/forecast?lat=25.3333&lon=83&appid=dd6ffdb1194aadf57f688e76ad6f82c7"
response=requests.get(url)
code=response.status_code
print(code)
#200 means success
#Status code 404 not found
#Sttus code 401 is not authorized
#print(response.text)
if code!=200:
    print("Error")
else:
    jsondata=json.loads(response.text)
    print(jsondata)
    city = jsondata['city']['name']
    print(city)
    jsondata=jsondata['list'][0]
    weather=jsondata.get("weather")[0]

    main_data=weather.get("main")
    main_description=weather.get("description")
    print(weather)
    print(main_data)
    print(main_description)
    temp=jsondata.get("main").get("temp")
    print(temp,"deg Celsius")