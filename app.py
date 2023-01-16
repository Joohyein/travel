from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
#import certifi
#ca = certifi.where()
#client = MongoClient('mongodb+srv://test:sparta@cluster0.igj8fho.mongodb.net/cluster0?retryWrites=true&w=majority',  tlsCAFile=ca)
client = MongoClient('mongodb+srv://test:sparta@cluster0.igj8fho.mongodb.net/cluster0?retryWrites=true&w=majority')
db = client.dbsparta
