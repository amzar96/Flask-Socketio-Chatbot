from flask import Flask, render_template, request
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'nsvnCHI0n5'
socketio = SocketIO(app)


@app.route('/', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@app.route('/start', methods=['POST'])
def sessions():
    username = request.form['username']
    return render_template('session.html', user=username)

@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    socketio.emit('my response', json)

if __name__ == '__main__':
    socketio.run(app, debug=True)