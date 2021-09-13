import  requests
import  json
appid="dd6ffdb1194aadf57f688e76ad6f82c7"
city="Varanasi"
url="http://api.openweathermap.org/data/2.5/weather?q={1}&appid={0}".format(appid,city)
response=requests.get(url)
print(response.status_code)
print(response.text)
jsondata=json.loads(response.text)
print(type(  jsondata))
print(jsondata["weather"][0]['description'])