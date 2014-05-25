#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
from bottle import route, run, get, post, template, request, static_file
import json
import requests
import urllib2
key = open('key.txt','r')
clave = ""
for lineas in key:
	clave = clave + lineas
clave = clave.replace("\n","")


puertos = {1:'A coru&ntilde;a',3:'Vigo',4:'Vilagarc&iacute;a',5:'Ferrol',6:'R&iacute;a de 	Foz',7:'Corcubi&oacute;n',8:'R&iacute;a de Camari&ntilde;as',9:'R&iacute;a de Corme',10:'A guarda',11:'Ribeira',12:'Muros',13:'Pontevedra'}


@route('<path:path>')
def server_static(filepath):
    return static_file(filepath, root='/plantilla/static/images/')


@route('/index')
def index():
	return template('index1.html')


@get('/corcubion')
def corcubion():
	page = urllib2.urlopen('http://www.corcubion.info/es/historia')
        corcubion = page.read()
	html = re.findall('<p>.*',corcubion)
	return html
		
	
@post('/getTidesInfo')
def getTidesInfo():
	localidad = request.forms.get('localidad')
	url = 'http://servizos.meteogalicia.es/apiv2/findPlaces'	
	valores = {'location':localidad,'API_KEY':clave}
	req = requests.get(url, params=valores)
	response = json.loads(req.text)
	response['features'][0]['geometry']['coordinates']		
	longitud = str(response['features'][0]['geometry']['coordinates'][0])
	latitud = str(response['features'][0]['geometry']['coordinates'][1])
	
	mareas = request.forms.get('mareas')
	url = 'http://servizos.meteogalicia.es/apiv2/getTidesInfo'
        valores = {'coord':mareas,'API_KEY':clave}
        req = requests.get(url, params=valores)
        response = json.loads(req.text)
	response['features'][0]['geometry']['coordinates']
        pleamar = response['features'][0]['properties']['days'][0]['variables'][0]['summary'][0]['TimeInstant']
        bajamar = response['features'][0]['properties']['days'][0]['variables'][0]['summary'][1]['TimeInstant']
        state_high = response['features'][0]['properties']['days'][0]['variables'][0]['summary'][0]['state']
        state_low = response['features'][0] ['properties']['days'][0]['variables'][0]['summary'][1]['state']
	
	semanal = request.forms.get('semanal')
	ident = request.forms.get('ident')
	return template('plantilla1.html', localidad=localidad, longi=longitud, lati=latitud, plea=pleamar, baja=bajamar, state_high=state_high, state_low=state_low, id=ident, data=semanal)



        


		



















run(host='localhost', port=80, debug=True)
