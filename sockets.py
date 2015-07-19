from flask import Flask, render_template
from flask.ext.socketio import SocketIO, emit
from random import randint
import gevent

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key_placeholder'
socketio = SocketIO(app)




@app.route('/')
def index():
	return render_template('index.html')

@socketio.on('tick', namespace='/test')
def test_tick(msg):
	while True:
		stock1 = randint(20,30)
		stock2 = randint(25,45)
		stock3 = randint(22,29)
		print number
		emit('incoming tick', {'data':stock1})
		gevent.sleep(.2)

@socketio.on('connect', namespace='/test')
def test_connect():
	print 'Client connected'

@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print 'Client disconnected'



if __name__ == '__main__':
	socketio.run(app)
