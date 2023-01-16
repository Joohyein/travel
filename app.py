from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
<<<<<<< HEAD
import random
#import certifi
#ca = certifi.where()
#client = MongoClient('mongodb+srv://test:sparta@cluster0.igj8fho.mongodb.net/cluster0?retryWrites=true&w=majority',  tlsCAFile=ca)
client = MongoClient('mongodb+srv://test:sparta@cluster0.igj8fho.mongodb.net/cluster0?retryWrites=true&w=majority')
=======
import certifi, random
ca = certifi.where()
client = MongoClient('mongodb+srv://test:sparta@cluster0.igj8fho.mongodb.net/cluster0?retryWrites=true&w=majority',  tlsCAFile=ca)
#client = MongoClient('mongodb+srv://test:sparta@cluster0.igj8fho.mongodb.net/cluster0?retryWrites=true&w=majority')
>>>>>>> d661709447461c14cb68b9b7307e7e05419d315f
db = client.dbsparta
#랜덤 예시
#random.randint(1,3)
#1~3까지의 수 랜덤

<<<<<<< HEAD
@app.route('/result/DDD')#달/뜨/디
def resultDDD():
   return render_template('result_DDD.html')
@app.route("/result/DDD", methods=["GET"])
def DDD_get():
    rand = random.randint(1, 3)
    return jsonify({'Cafe':db.CafeDalDuDe.find_one({'id': int(rand)})})
=======
@app.route('/')
def home():
   return render_template('index.html')

@app.route('/select')
def select():
   return render_template('select.html')

@app.route("/select/result", methods=["POST"])
def Coffee_post():
   Caffeine = request.form['Caffeine_give']
   Hot = request.form['Hot_give']
   Sweet = request.form['Sweet_give']

   if Caffeine == 0 and Hot == 0 and Sweet == 0:
      return jsonify({'msg':'/result/SCD'})#쌉차디
   if Caffeine == 0 and Hot == 0 and Sweet == 1:
      return jsonify({'msg': '/result/DCD'})#달차디
   if Caffeine == 0 and Hot == 1 and Sweet == 0:
      return jsonify({'msg': '/result/CDD'})  # 쌉뜨디
   if Caffeine == 0 and Hot == 1 and Sweet == 1:
      return jsonify({'msg': '/result/DDD'})  # 달뜨디
   if Caffeine == 1 and Hot == 0 and Sweet == 0:
      return jsonify({'msg':'/result/SCC'})#쌉차카
   if Caffeine == 1 and Hot == 0 and Sweet == 1:
      return jsonify({'msg': '/result/DCC'})#달차카
   if Caffeine == 1 and Hot == 1 and Sweet == 0:
      return jsonify({'msg': '/result/SDC'})  # 쌉뜨카
   if Caffeine == 1 and Hot == 1 and Sweet == 1:
      return jsonify({'msg': '/result/DDC'})  #달뜨카


@app.route('/result/SCC')#쌉/차/카
def resultSCC():
   return render_template('result/SCC.html')

@app.route("/result/SCC", methods=["GET"])
def SCC_get():
    rand = random.randint(1, 3)
    return jsonify({'Cafe':db.CafeSapChaCa.find_one({'id': int(rand)})})

@app.route('/result/DCC')#달/차/카
def resultDCC():
   return render_template('result/DCC.html')

@app.route("/result/DCC", methods=["GET"])
def DCC_get():
    rand = random.randint(1, 4)
    return jsonify({'Cafe':db.CafeDalChaCa.find_one({'id': int(rand)})})

@app.route('/result/SDC')#쌉/뜨/카
def resultSDC():
   return render_template('result/SDC.html')

@app.route("/result/SDC", methods=["GET"])
def SDC_get():
    rand = random.randint(1, 2)
    return jsonify({'Cafe':db.CafeSapDuCa.find_one({'id': int(rand)})})

@app.route('/result/DDC')#달/뜨/카
def resultDDC():
   return render_template('result/DDC.html')

@app.route("/result/DDC", methods=["GET"])
def DDC_get():
    rand = random.randint(1, 3)
    return jsonify({'Cafe':db.CafeDalDuCa.find_one({'id': int(rand)})})

@app.route('/result/DDD')#달/뜨/디
def resultDDD():
   return render_template('result_DDD.html')

@app.route("/result/DDD1", methods=["GET"])
def DDD_get():
    rand = random.randint(1, 3)
    Cafe_menu = db.CafeDalDuDe.find_one({'id': int(rand)})
    return jsonify({'Cafe':[Cafe_menu]})

@app.route('/result/SDD')#쌉/뜨/디  //2개
def resultSDD():
   return render_template('result/SDD.html')

@app.route("/result/SDD", methods=["GET"])
def SDD_get():
    rand = random.randint(1, 2)
    return jsonify({'Cafe':db.CafeSapDuDe.find_one({'id': int(rand)})})

@app.route('/result/DCD')#달/차/디 //3개
def resultDCD():
   return render_template('result/DCD.html')

@app.route("/result/DCD", methods=["GET"])
def DCD_get():
    rand = random.randint(1, 3)
    return jsonify({'Cafe':db.dbsparta.CafeDalChaDe.find_one({'id': int(rand)})})

@app.route('/result/SCD')#쌉/차/디 //3개
def resultSCD():
   return render_template('result/SCD.html')

@app.route("/result/SCD", methods=["GET"])
def SCD_get():
    rand = random.randint(1, 3)
    return jsonify({'Cafe':db.CafeSapChaDe.find_one({'id': int(rand)})})
>>>>>>> d661709447461c14cb68b9b7307e7e05419d315f

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)