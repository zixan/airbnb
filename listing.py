import requests
import pprint
from lxml import html

url = 'https://www.airbnb.com/s?cdn_spdy=1&location=2709+College+Ave%2C+Berkeley%2C+CA%2C+United+States&ne_lat=37.890540257343716&ne_lng=-122.21133577169297&page={}&s_tag=Kdm7&search_by_map=true&sw_lat=37.829914173532664&sw_lng=-122.2954498464'

result = {'data':[]}

def main():
    for i in range(1,57):
        r = requests.get(url.format(str(i)))
        status = r.status_code
        if status != 200:
            raise 'Something went wrong...'
        text = r.text
        lat_coords = html.fromstring(text).xpath('//div[@class="listing"]/@data-lat')
        long_coords = html.fromstring(text).xpath('//div[@class="listing"]/@data-lng')
        for coords in zip(lat_coords, long_coords):
            data = {'lat':coords[0], 'long':coords[1]}
            result['data'].append(data)
    pprint.pprint(result)

if __name__ == '__main__':
    main()
