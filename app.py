from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
import certifi, random
ca = certifi.where()
client = MongoClient('mongodb+srv://test:sparta@cluster0.igj8fho.mongodb.net/cluster0?retryWrites=true&w=majority',  tlsCAFile=ca)
#client = MongoClient('mongodb+srv://test:sparta@cluster0.igj8fho.mongodb.net/cluster0?retryWrites=true&w=majority')
db = client.dbsparta
#랜덤 예시
#random.randint(1,3)
#1~3까지의 수 랜덤

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/select')
def select():
   return render_template('select.html')

@app.route("/select/result", methods=["POST"])
def Coffee_post():
   Caffeine = int(request.form['Caffeine_give'])
   Hot = int(request.form['Hot_give'])
   Sweet = int(request.form['Sweet_give'])
   if Caffeine == 0 and Hot == 0 and Sweet == 0: #000 쌉/차/디 SCD
       return jsonify({'msg':'/result/SCD'})
   elif Caffeine == 0 and Hot == 0 and Sweet == 1:#001 달/차/디 DCD
        return jsonify({'msg': '/result/DCD'})
   elif Caffeine == 0 and Hot == 1 and Sweet == 0:#010 쌉/뜨/디 SDD
        return jsonify({'msg': '/result/SDD'})
   elif Caffeine == 0 and Hot == 1 and Sweet == 1:#011 달/뜨/디 DDD
        return jsonify({'msg': '/result/DDD'})
   elif Caffeine == 1 and Hot == 0 and Sweet == 0:#100 쌉/차/카 SCC
        return jsonify({'msg': '/result/SCC'})
   elif Caffeine == 1 and Hot == 0 and Sweet == 1:#101 달/차/카 DCC
        return jsonify({'msg': '/result/DCC'})
   elif Caffeine == 1 and Hot == 1 and Sweet == 0:#110 쌉/뜨/카 SDC
        return jsonify({'msg': '/result/SDC'})
   elif Caffeine == 1 and Hot == 1 and Sweet == 1:#111 달/뜨/카 DDC
        return jsonify({'msg': '/result/DDC'})


   # if Caffeine == 0 and Hot == 0 and Sweet == 0:
   #    return jsonify({'msg':'/result/SCD'})#쌉차디//000
   # if Caffeine == 0 and Hot == 0 and Sweet == 1:
   #    return jsonify({'msg': '/result/DCD'})#달차디001
   # if Caffeine == 0 and Hot == 1 and Sweet == 0:
   #    return jsonify({'msg': '/result/SDD'})  # 쌉뜨디010
   # if Caffeine == 0 and Hot == 1 and Sweet == 1:
   #    return jsonify({'msg': '/result/DDD'})  # 달뜨디011
   # if Caffeine == 1 and Hot == 0 and Sweet == 0:
   #    return jsonify({'msg':'/result/SCC'})#쌉차카100
   # if Caffeine == 1 and Hot == 0 and Sweet == 1:
   #    return jsonify({'msg': '/result/DCC'})#달차카101
   # if Caffeine == 1 and Hot == 1 and Sweet == 0:
   #    return jsonify({'msg': '/result/SDC'})  # 쌉뜨카110
   # if Caffeine == 1 and Hot == 1 and Sweet == 1:
   #    return jsonify({'msg': '/result/DDC'})  #달뜨카111

@app.route('/result/SCC')#쌉/차/카
def resultSCC():
   return render_template('result_SCC.html')

@app.route("/result/SCC1", methods=["GET"])
def SCC_get():
    rand = random.randint(1, 3)
    data = db.CafeSapChaCa.find_one({'id': int(rand)})
    drink = data['Drink']
    img = data['image_url']
    cafe_data = {
        'Drink':drink,
        'image_url':img
    }
    return jsonify({'Cafe':cafe_data})

@app.route('/result/DCC')#달/차/카
def resultDCC():
   return render_template('result_DCC.html')

@app.route("/result/DCC1", methods=["GET"])
def DCC_get():
    rand = random.randint(1, 4)
    data = db.CafeDalChaCa.find_one({'id': int(rand)})
    drink = data['Drink']
    img = data['image_url']
    cafe_data = {
        'Drink': drink,
        'image_url': img
    }
    return jsonify({'Cafe': cafe_data})

@app.route('/result/SDC')#쌉/뜨/카
def resultSDC():
   return render_template('result_SDC.html')

@app.route("/result/SDC1", methods=["GET"])
def SDC_get():
    rand = random.randint(1, 2)
    data = db.CafeSapDuCa.find_one({'id': int(rand)})
    drink = data['Drink']
    img = data['image_url']
    cafe_data = {
        'Drink': drink,
        'image_url': img
    }
    return jsonify({'Cafe': cafe_data})

@app.route('/result/DDC')#달/뜨/카
def resultDDC():
   return render_template('result_DDC.html')

@app.route("/result/DDC1", methods=["GET"])
def DDC_get():
    rand = random.randint(1, 3)
    data = db.CafeDalDuCa.find_one({'id': int(rand)})
    drink = data['Drink']
    img = data['image_url']
    cafe_data = {
        'Drink': drink,
        'image_url': img
    }
    return jsonify({'Cafe': cafe_data})

@app.route('/result/DDD')#달/뜨/디
def resultDDD():
   return render_template('result_DDD.html')

@app.route("/result/DDD1", methods=["GET"])
def DDD_get():
    rand = random.randint(1, 3)
    data = db.CafeDalDuDe.find_one({'id': int(rand)})
    drink = data['Drink']
    img = data['image_url']
    cafe_data = {
        'Drink': drink,
        'image_url': img
    }
    return jsonify({'Cafe': cafe_data})

@app.route('/result/SDD')#쌉/뜨/디  //2개
def resultSDD():
   return render_template('result_SDD.html')

@app.route("/result/SDD1", methods=["GET"])
def SDD_get():
    rand = random.randint(1, 2)
    data = db.CafeSapDuDe.find_one({'id': int(rand)})
    drink = data['Drink']
    img = data['image_url']
    cafe_data = {
        'Drink': drink,
        'image_url': img
    }
    return jsonify({'Cafe': cafe_data})

@app.route('/result/DCD')#달/차/디 //3개
def resultDCD():
   return render_template('result_DCD.html')

@app.route("/result/DCD1", methods=["GET"])
def DCD_get():
    rand = random.randint(1, 3)
    data = db.CafeDalChaDe.find_one({'id': int(rand)})
    drink = data['Drink']
    img = data['image_url']
    cafe_data = {
        'Drink': drink,
        'image_url': img
    }
    return jsonify({'Cafe': cafe_data})

@app.route('/result/SCD')#쌉/차/디 //3개
def resultSCD():
   return render_template('result_SCD.html')

@app.route("/result/SCD1", methods=["GET"])
def SCD_get():
    rand = random.randint(1, 3)
    data = db.CafeSapChaDe.find_one({'id': int(rand)})
    drink = data['Drink']
    img = data['image_url']
    cafe_data = {
        'Drink': drink,
        'image_url': img
    }
    return jsonify({'Cafe': cafe_data})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)