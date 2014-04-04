import requests
import json
from bottle import route, run

@route('/mareas')
def getTidesInfo():
	API='tntmnZ85PrQ6AGw6ihuUGhqs894jl66UI8p4ph4rmbvcno3MIApKE0o2N1awzT2p'
	req = requests.get('http://servizos.meteogalicia.es/apiv2/getTidesInfo', params={'coord':'API_KEY':API})
	response = json.loads(req.text)
	print response['type']
run(host='localhost', port=8080, debug=True)

@route('/location')
def location():
        API='tntmnZ85PrQ6AGw6ihuUGhqs894jl66UI8p4ph4rmbvcno3MIApKE0o2N1awzT2p'
        req = requests.get('http://servizos.meteogalicia.es/apiv2/findPlaces', params={'location':'%s','API_KEY':API})
        response = json.loads(req.text)
        print response['type']
run(host='localhost', port=8080, debug=True)

