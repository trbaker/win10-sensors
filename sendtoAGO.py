import requests as r
import json
from datetime import datetime
import pytz

indexlist = [171759,164627,9738,109008,127637,108520,127637,130777,127613,109006,24105,54769]


# time with timezone adjust
now = datetime.utcnow()
timezone = pytz.timezone("America/Chicago")
now = timezone.localize(now)
now.tzinfo
print(now)

for i in indexlist:
    url = 'https://api.purpleair.com/v1/sensors/' + str(i) + '/?api_key=xxxxx&fields=latitude,longitude,pm10.0,name'
    x = r.get(url)
    # print(x.text)
    response_dict = json.loads(x.text)
    print("Processing: " + response_dict['sensor']['name'])
    AGOurl = 'https://services4.arcgis.com/ZLxHvZNeliOC3hOr/arcgis/rest/services/survey123_34c0b147a8774f309f5bed1d4d2cf3ff_form/FeatureServer/0/addFeatures'
    mylat = response_dict['sensor']['latitude']
    mylon = response_dict['sensor']['longitude']
    mypm10 = response_dict['sensor']['pm10.0']
    myname = response_dict['sensor']['name']

    today = str(now.strftime("%m/%d/%Y, %H:%M:%S"))
    params={"f":"pjson","token":"","rollbackOnFailure":"false","features":'{ \
        "geometry": {"x":'+ str(mylon) + ',"y":'+ str(mylat) + '}, "attributes" : { \
            "comments" : "' + myname + '", \
            "teacher" : "vs.content", \
            "lat" : '+ str(mylat) + ', \
            "lon": '+ str(mylon) + ', \
            "sdate" : "' + today + '", \
            "pm10" :  '+ str(mypm10) + ' }}'
        }

    print(params)
    z = r.post(AGOurl, params=params)
    print(z.text)
    print('.')

    
    
