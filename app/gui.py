from flask import Flask, flash, redirect, render_template, request, session, abort

import logging
import random
import threading
import time

class Counter:

    def __init__(self, start=0):
        self.lock = threading.Lock()
        self.value = start

    def increment(self):
        logging.debug('Waiting for lock')
        self.lock.acquire()
        try:
            logging.debug('Acquired lock')
            self.value = self.value + 7
        finally:
            self.lock.release()


def sensor_counter(c):
	while True:
		
		time.sleep(1.0)
		c.increment()


counter = Counter()


sensor_thread = threading.Thread(target=sensor_counter, args=(counter,))
sensor_thread.start()

app = Flask(__name__)
@app.route('/')
def home():
    return "Hey there!"

@app.route('/articles/<articleid>')
def api_article(articleid):
    return 'You are reading ' + articleid

# The test.html template file must reside in a folder named
#   templates
# Perhaps there's a way to direct the server where to look
# if this needs to change
@app.route('/hello/<string:message>/')
def api_hello(message):
    return render_template(
        'test.html',message=message)

@app.route('/vuetest')
def api_vuetest():
    return app.send_static_file(
        'vuetest.html')

@app.route('/testendpoint')
def api_testendpoint():
    return str(counter.value)

if __name__ == '__main__':
    app.run(debug=True)

