from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbhomework


## HTML 화면 보여주기
@app.route('/')
def homework():
    return render_template('index.html')


# 주문하기(POST) API
@app.route('/order', methods=['POST'])
def save_order():
    name = request.form['name']
    amount = request.form['amount']
    address = request.form['address']
    phone_number = request.form['phonenumber']

    order = {
        'name': name,
        'amount': amount,
        'address': address,
        'phone number': phone_number,
    }

    db.week04homework.insert_one(order)
    return jsonify({'result': 'success', 'msg': '주문 완료! 즐거운 인코그니토 하세요!'})


# 주문 목록보기(Read) API
@app.route('/order', methods=['GET'])
def view_orders():
    orders = list(db.week04homework.find({}, {'_id': False}))


    return jsonify({'result': 'success', 'orders': orders, 'msg': '주문이 업로드 되었습니다!'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
