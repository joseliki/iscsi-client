from bottle import route, run
 
@route('/hello/<name>')
def index(name):
	return '<b>Hello %s!</b>' % name
 
if __name__ == '__main__':
	run(host='localhost', port=8080)
