from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
#import certifi
#ca = certifi.where()
#client = MongoClient('mongodb+srv://test:sparta@cluster0.igj8fho.mongodb.net/cluster0?retryWrites=true&w=majority',  tlsCAFile=ca)
client = MongoClient('mongodb+srv://test:sparta@cluster0.igj8fho.mongodb.net/cluster0?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/select')
def select():
   return render_template('select.html')

@app.route('/result')
def result():
   return render_template('result.html')

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)