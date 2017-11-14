# -*- coding: utf-8 -*-
#fixed issue with old gevent library: $pip uninstall gevent $pip install gevent==1.1b4


#Demo Flask application to test the operation of Flask with socket.io. Aim is to create a webpage that is constantly updated with tweets that contain specific user-defined keywords from a background python process.
#added the HTML and Javascript files to make the webpage work!
def Nothing():
    return 1

#initially the below was: from flask.ext.socketio import SocketIO, emit
from flask_socketio import emit, SocketIO
from flask import Flask, render_template, url_for, copy_current_request_context
from random import random # it is already in the standard library
from time import sleep # it is already in the standard library
from threading import Thread, Event #threading already in library
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json


def earthquakedateconverter(date):
    splitted_string = date.split()

    day_number = splitted_string[2]
    month = splitted_string[1]

    time = splitted_string[3]
    hours = time.split(':')[0]
    mins = time.split(':')[1]
    secs = time.split(':')[2]
    day = splitted_string[0]

    hours = int(hours)  # hours is string till now
    if hours >= 21:

        hours = hours + 3 - 24  # fix hour
        hours = str(hours)
        hours = '0' + hours
        timesequence = [hours, mins, secs]
        splitted_string[3] = (':'.join(timesequence))

        if day == 'Mon':  # nameday fix - add one
            splitted_string[0] = 'Tue'
        elif day == 'Tue':
            splitted_string[0] = 'Wed'
        elif day == 'Wed':
            splitted_string[0] = 'Thu'
        elif day == 'Thu':
            splitted_string[0] = 'Fri'
        elif day == 'Fri':
            splitted_string[0] = 'Sat'
        elif day == 'Sat':
            splitted_string[0] = 'Sun'
        elif day == 'Sun':
            splitted_string[0] = 'Mon'

        # day number fix
        day_number = int(day_number) + 1
        day_number = str(day_number)

        # month number fix
        if month == 'Jan':
            if (int(day_number) > 28):
                month = 'Feb'
                day_number = '01'

        if month == 'Feb':
            if (int(day_number) > 28):
                month = 'Mar'
                day_number = '01'

        if month == 'Mar':
            if (int(day_number) > 31):
                month = 'Apr'
                day_number = '01'

        if month == 'Apr':
            if (int(day_number) > 30):
                month = 'May'
                day_number = '01'

        if month == 'May':
            if (int(day_number) > 31):
                month = 'Jun'
                day_number = '01'

        if month == 'Jun':
            if (int(day_number) > 30):
                month = 'Jul'
                day_number = '01'

        if month == 'Jul':
            if (int(day_number) > 31):
                month = 'Aug'
                day_number = '01'

        if month == 'Aug':
            if (int(day_number) > 31):
                month = 'Sept'
                day_number = '01'

        if month == 'Sept':
            if (int(day_number) > 30):
                month = 'Oct'
                day_number = '01'

        if month == 'Oct':
            if (int(day_number) > 31):
                month = 'Nov'
                day_number = '01'

        if month == 'Nov':
            if (int(day_number) > 30):
                month = 'Dec'
                day_number = '01'

        if month == 'Dec':
            if (int(day_number) > 31):
                month = 'Jan'
                day_number = '01'

        splitted_string[2] = day_number
        splitted_string[1] = month

    else:  # if time <21:00
        a = str(int(hours) + 3)
        if (int(hours) + 3) < 10:
            a = '0' + str(int(hours) + 3)
        timesequence = [a, mins, secs]
        splitted_string[3] = (':'.join(timesequence))

    reproduced_date_sequence = [splitted_string[0], splitted_string[1], splitted_string[2], splitted_string[3],
                                splitted_string[4], splitted_string[5]]
    reproduced_date = (' '.join(reproduced_date_sequence))
    return (reproduced_date)



__author__ = 'Vasilis & Andrew' #just metadata - doing nothing but stating the author of this

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!' #This is a secret key that is used by Flask to sign cookies. It's also used by extensions like Flask-Bcrypt. You should define this in your instance
                                    # folder to keep it out of version control. You can read more about instance folders in the next section. http://explore-flask.readthedocs.io/en/latest/configuration.html
                                    #RECOMMENDED: This should be a complex random value.
app.config['DEBUG'] = True          #Gives you some handy tools for debugging errors. This includes a web-based stack trace and interactive Python console for errors.
                                    #Should be set to True in development and False in production. Make sure DEBUG is set to False in production. Leaving it on will allow users to run arbitrary Python code on your server.

#turn the flask app into a socketio app
socketio = SocketIO(app)  #default directory websockets use is "/socket.io" for server AND client - https://github.com/miguelgrinberg/Flask-SocketIO/issues/302

thread = Thread()    #creating an object of class Thread from threading library - https://docs.python.org/3/library/threading.html
thread_stop_event = Event() #creating an object of class Thread from threading library - same link as above. This is one of the simplest mechanisms for communication between threads: one thread signals an event and other
                            # threads wait for it. An event object manages an internal flag that can be set to true with the set() method and reset to false with the clear() method. The wait() method blocks until the flag is true.

class TweetStreamThread(Thread): #we define the class TweetStreamThread which concerns a thread that will run the main code
    def __init__(self):         #This method always happens
        super(TweetStreamThread, self).__init__()   #super() calls the parent's class constructor (all the way back to Object) and it runs before the current class's constructor.

    def maincode(self):  #Run main code of our app and emit to a socketio instance (broadcast)

        print("in maincode")

        # consumer key, consumer secret, access token, access secret. Need to set those values so that the app has access to Twitter data
        ckey = 
        csecret = 
        atoken = 
        asecret = 

        class listener(StreamListener):
            def on_data(self, data):
                tweet_dict = json.loads(data, encoding="utf-8")  # transforms string to dictionary
                try:  # we use the exception utility because of the occasional tweet that fails in the stream
                    text = tweet_dict["text"]  # store tweet's text
                    id_integer = tweet_dict["user"]["id"]  # store tweet's id (unique integer id for specific user)
                    created_at=tweet_dict["created_at"]

                    print(id_integer, text)
                    print(created_at, 'UTC =>',earthquakedateconverter(created_at),"GMT+3")
                    number=id_integer
                    socketio.emit('newnumber', {'number':'GMT+3: ' + earthquakedateconverter(created_at)+' | '+text}, namespace='/test')

                except KeyError:
                    pass

            def on_error(self, status):
                print(status)

        auth = OAuthHandler(ckey, csecret)
        auth.set_access_token(atoken, asecret)

        twitterStream = Stream(auth, listener())

        filter_string=['seismos', u'σεισμος',u'σεισμός',u'εγκέλαδος',u'ρίχτερ'] #u needed before each word to convert greek strings to unicode for the filter method to handle properly
        twitterStream.filter(track=filter_string)

    def run(self):
        try:
            print('in Thread run method')
            self.maincode()
        except:
            raise

@app.route('/')
def index():    #only by sending this page first will the client be connected to the socketio instance
    return render_template('index_test2_bootstrap.html')

@socketio.on('connect', namespace='/test')
def test_connect():
    # need visibility of the global thread object
    global thread
    print('Client connected')

    #if not thread.isAlive(): #if there is no thread then Create one and start it's activity. Return whether the thread is alive. This method returns True just before the run() method starts until just after the run() method terminates.
    print ("Starting Thread")
    thread = TweetStreamThread()
    thread.start() #Start the thread's activity. The start() method starts a thread by calling the run() method.

@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected')

if __name__ == '__main__':
    socketio.run(app)
