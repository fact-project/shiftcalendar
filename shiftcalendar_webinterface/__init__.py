import os
from datetime import datetime, timedelta
import json

from .authentication import login_manager, basic_auth, authenticate_user


from flask import Flask, jsonify, render_template, redirect, request, flash, Markup
from flask_login import login_user, login_required, logout_user
from flask_socketio import SocketIO
from flask_login import current_user

from twilio.rest import TwilioRestClient
from twilio.exceptions import TwilioException
import peewee

from shiftcalendar.database import connect_databases
from shiftcalendar.models import Role, CalendarEntry, LegacyCalendarEntry
from shiftcalendar.logbook_models import Users



app = Flask(__name__)
app.secret_key = b'\xf8P\x04\xd8Nk4ve\x8d\xd8\xe3\x9f\xccx`\xf3\x88\xb6\rQ\xf4\xc7\x8a'
login_manager.init_app(app)

user2id = {}
uid2name = {}

@app.before_first_request
def init_db():
    connect_databases()
    q = Users.select(Users.username, Users.uid)
    for d in q:
        user2id[d.username] = d.uid
        uid2name[d.uid] = d.username

@app.before_request
def _db_connect():
    pass

@app.teardown_request
def _db_close(exc):
    """
    if not database.is_closed():
        database.close()
    """

@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html')


@app.route('/roles')
@login_required
def get_roles():
    return json.dumps(list(Role.select().dicts()))

@app.route('/usernames')
@login_required
def get_usernames():
    q = Users.select(Users.username, Users.uid).dicts()
    l = [d for d in q]
    for d in l:
        d['user_id'] = d.pop('uid')
    return json.dumps(l)

@app.route('/events', methods=["GET"])
#@login_required
def get_events():
    def str2date(s):
        return datetime.strptime(s, '%Y-%m-%d')

    start = request.args.get('start', default="2011-01-01", type=str2date)
    end = request.args.get('end', default="2100-01-01", type=str2date)
    l = list(CalendarEntry
        .select(Role, CalendarEntry)
        .join(Role)
        .where((start < CalendarEntry.start) & (end > CalendarEntry.end))
        .dicts())
    for d in l:
        d['url'] = ''
        d['allDay'] = 0
        d['title'] = uid2name[d['user_id']]
    return jsonify(l)

@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'GET':
        return redirect('/')

    username = request.form['username']
    password = request.form['password']

    user = authenticate_user(username, password)

    if user is not None:
        login_user(user)
        return redirect('/')
    else:
        flash('Wrong username/password', 'alert-danger')
        return redirect('/')


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
    return redirect('/')

"""
def remove_alert(uuid):
    (
        Alert.select()
        .where(Alert.uuid == uuid)
        .get()
    ).delete_instance()


def add_alert(alert):
    alert['acknowledged'] = False
    Alert(**alert).save()


def acknowledge_alert(uuid):
    alert = (
        Alert.select()
        .where(Alert.uuid == uuid)
        .get()
    )
    alert.acknowledged = True
    alert.save()


def retrieve_alerts():
    comp_date = datetime.utcnow() - timedelta(hours=24)
    alerts = (
        Alert
        .select()
        .order_by(Alert.timestamp.desc())
        .where(Alert.timestamp > comp_date)
    )
    return [alert.to_dict() for alert in alerts]


def update_clients():
    alerts = retrieve_alerts()
    socket.emit('update', json.dumps(alerts))
"""


"""
@app.route('/alerts', methods=['GET'])
def get_alerts():
    alerts = retrieve_alerts()
    return jsonify(alerts)



@app.route('/alerts', methods=['POST'])
@basic_auth.login_required
def post_alert():
    alert = request.json
    try:
        add_alert(alert)
    except peewee.InternalError as e:
        return jsonify(status='Could not add alert', message=str(e)), 422

    update_clients()
    return jsonify(status='ok')


@app.route('/alerts/<uuid>', methods=['PUT', 'DELETE'])
@login_required
def update_alert(uuid):

    if request.method == 'PUT':
        try:
            acknowledge_alert(uuid)
            update_clients()
            return jsonify(status='ok')
        except Alert.DoesNotExist:
            return jsonify(status='No such alert'), 404

    elif request.method == 'DELETE':
        try:
            uuid = request.args['uuid']
            remove_alert(uuid)
            update_clients()
        except KeyError:
            return jsonify(status='No such alert'), 404


@app.route('/alerts/<uuid>', methods=['GET'])
def get_alert(uuid):
    try:
        alert = Alert.get(uuid=uuid)
        return jsonify(alert.to_dict())
    except Alert.DoesNotExist:
        return jsonify(status='No such alert'), 404

"""


