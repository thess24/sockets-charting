from flask import Flask, render_template
from flask.ext.socketio import SocketIO, emit
from random import randint
import gevent

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)




@app.route('/')
def index():
	return render_template('index.html')

@socketio.on('tick', namespace='/test')
def test_tick(msg):
	while True:
		number = randint(0,9)
		print number
		emit('incoming tick', {'data':number})
		gevent.sleep(.2)

@socketio.on('connect', namespace='/test')
def test_connect():
    emit('my response', {'data': 'Connected'})

@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected')



if __name__ == '__main__':
	socketio.run(app)


# find way for function to submit large amounts of random numbers to websocket endpoint -- route through http endpt from other fxn?
# take data from websocket and graph