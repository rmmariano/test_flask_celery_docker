from worker_a import add_nums
from worker_b import sub_nums

from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route("/add")
def add():
    print('\nadd()')

    first_num = request.args.get('first_num')
    second_num = request.args.get('second_num')

    task = add_nums.delay(first_num, second_num)

    print('first_num: ', first_num)
    print('second_num: ', second_num)
    print('task: ', task)
    print('state: ', task.state)
    print('result: ', task.result)
    print('get(): ', task.get())

    return jsonify({'result': task.result}), 200


@app.route("/subtract")
def subtract():
    print('\nsubtract()')

    first_num = request.args.get('first_num')
    second_num = request.args.get('second_num')

    task = sub_nums.delay(first_num, second_num)

    print('first_num: ', first_num)
    print('second_num: ', second_num)
    print('task: ', task)
    print('state: ', task.state)
    print('result: ', task.result)
    print('get(): ', task.get())

    return jsonify({'result': task.result}), 200
