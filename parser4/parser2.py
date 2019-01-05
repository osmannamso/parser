import json
from parser4.models import Twogis
import multiprocessing.dummy as mp

def do_print(i):
    import urllib.request
    import json
    from parser4.models import Twogis
    iss = '000000000000' + str(i)
    oid = '700000010' + iss[-8:]
    contents = urllib.request.urlopen(
        "https://catalog.api.2gis.ru/2.0/catalog/branch/get?is_poi=true&type=filial&id=" + oid + "&see_also_size=4&fields=items.adm_div%2Citems.region_id%2Citems.segment_id%2Citems.reviews%2Citems.timezone_offset%2Citems.point%2Citems.links%2Citems.name_ex%2Citems.org%2Citems.group%2Citems.see_also%2Citems.dates%2Citems.external_content%2Citems.flags%2Citems.ads.options%2Citems.email_for_sending.allowed%2Csearch_attributes&stat%5Bsid%5D=1b951a60-1318-49e0-b907-327dbe926443&stat%5Buser%D=4f01b697-f36f-4651-a208-3ed1a5b1a550&key=rutnpt3272&r=203673874").read()
    d = json.loads(contents)
    map = Twogis()
    map.oid = int(oid)
    if 'result' in d:
        dore = d['result']['items'][0]
        map.address = dore['address_name']
        map.name = dore['org']['name']
        map.lon = dore['point']['lon']
        map.lat = dore['point']['lat']
        # if hasattr(dore, 'address_name') and hasattr(dore, 'name') and hasattr(dore, 'lon') and hasattr(dore, 'lat'):
        if int(map.lat) == 43 and int(map.lon) == 76 and len(Twogis.objects.filter(oid=map.oid, name=map.name, address=map.address)) == 0:
            map.save()
            print('added' + oid)
    print('nope' + oid)

p = mp.Pool(100)
p.map(do_print, range(20000000, 45000000))  # range(0,1000) if you want to replicate your example
p.close()
p.join()

print('asd')