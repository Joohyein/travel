from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
import random
#import certifi
#ca = certifi.where()
#client = MongoClient('mongodb+srv://test:sparta@cluster0.igj8fho.mongodb.net/cluster0?retryWrites=true&w=majority',  tlsCAFile=ca)
client = MongoClient('mongodb+srv://test:sparta@cluster0.igj8fho.mongodb.net/cluster0?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/result/DDD')#달/뜨/디
def resultDDD():
   return render_template('result_DDD.html')
@app.route("/result/DDD", methods=["GET"])
def DDD_get():
    rand = random.randint(1, 3)
    return jsonify({'Cafe':db.CafeDalDuDe.find_one({'id': int(rand)})})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)