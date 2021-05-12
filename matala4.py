import requests
import json
try:
    file=open("dests.txt",encoding = 'utf8')
    data = dict()
    for line in file:
        arrival=line
        from_city='תל אביב'
        google_key="AIzaSyCi2zNdeBVyQe95SYyIJQn6Mye0wcoeiXE"
        distance_url='https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins=%s&destinations=%s&key=%s' %(from_city,arrival,google_key)
        result=requests.get(distance_url).json()
        distance=result['rows'][0]['elements'][0]['distance']['text']
        duration=result['rows'][0]['elements'][0]['duration']['text']

        geo_url="https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s" % (arrival,google_key)
        result1=requests.get(geo_url).json()
        point=result1['results'][0]['geometry']['location']
        lng=point['lng']
        lat=point['lat']
        tupple=(distance,duration,lng,lat)
        data[arrival]=tupple

    print_data=json.dumps(data,ensure_ascii=False,indent=4).encode('utf8')
    print(print_data.decode())

    farest_from_tlv = sorted(data,key=data.get,reverse=True)
    top3 = farest_from_tlv[0:3]
    print("שלוש המדינות הרחוקות ביותר מתל אביב הן:  ",top3)
except:
    print("משהו השתבש או שאינו חוקי,אנא נסה שנית")