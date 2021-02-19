from worker_a import add_nums
from worker_b import sub_nums

from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route("/add")
def add():
    # curl "localhost:5000/add?first_num=3&second_num=2"
    print('\nadd()')

    first_num = int(request.args.get('first_num'))
    second_num = int(request.args.get('second_num'))

    task = add_nums.delay(first_num, second_num)

    # print('first_num: ', first_num)
    # print('second_num: ', second_num)
    # print('task: ', task)
    # print('state: ', task.state)
    # print('result: ', task.result)
    # print('backend: ', task.backend)
    # print('get(): ', task.get()) # <-- it does not work

    return jsonify({'result': task.get()}), 200


@app.route("/subtract")
def subtract():
    # curl "localhost:5000/subtract?first_num=3&second_num=2"
    print('\nsubtract()')

    first_num = int(request.args.get('first_num'))
    second_num = int(request.args.get('second_num'))

    task = sub_nums.delay(first_num, second_num)

    # print('first_num: ', first_num)
    # print('second_num: ', second_num)
    # print('task: ', task)
    # print('state: ', task.state)
    # print('result: ', task.result)
    # print('backend: ', task.backend)
    # print('get(): ', task.get())

    return jsonify({'result': task.get()}), 200
