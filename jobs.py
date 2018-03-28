# activities.py

from flask import Flask, render_template
import requests
import json

app = Flask(__name__, template_folder='.')

@app.route('/')
def homepage():
 params = {
   'api_key': {API-KEY}
 }
 print 'Getting results from parsehub'
 r = requests.get(
     'https://www.parsehub.com/api/v2/projects/{PROJECT-KEY}/last_ready_run/data',
     params=params)
 print "Got results"
 #print titles
 return render_template('jobs.html', jobs=json.loads(r.text)['title'])

if __name__ == '__main__':
 app.run(debug=True)
