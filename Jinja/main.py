from flask import Flask,render_template
import json
from jinja2 import FileSystemLoader,Environment



with open('data.json','r') as json_file:
    data = json.load(json_file)

app = Flask(__name__)

@app.route('/')
def home():
    
    return render_template('home.html',data=data)


if __name__=='__main__':
    app.run(debug=True)