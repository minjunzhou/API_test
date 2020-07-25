#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask
from flask import request

test_app = Flask(__name__)

@test_app.route('/shopee/test', methods=['GET'])
def test_task():
    # 需要从request对象读取表单内容：
    #url:http://localhost.charlesproxy.com:5000/shopee/test?a=1&b=nihao
    #a 非必填，int型，b必填，string型

    #b参数，a参数都有，但是a或b类型错误，则返回 empty or wrong params
    #b参数有，a参数没有，但是b参数类型错误，则返回 empty or wrong params
    # b参数有，b为string类型，默认即为string,则返回success

    # b参数有（类型正确），a有（类型正确）/a没有，则返回success-------2case
    if request.args.get('b') != None:
        if request.args.get('a') != None and request.args.get('a').isdigit():
            return {"error_code": 0,
                    "error_message": "success",
                    "reference": request.args.get('b') + ' ' + request.args.get('a')}
        elif request.args.get('a')==None:
            return {"error_code": 0,
                    "error_message": "success",
                    "reference": request.args.get('b')}

    #b参数有，b类型正确，a参数存在，但a参数类型不正确,返回empty or wrong params-----1case
    if request.args.get('b') != None:
        if request.args.get('a') != None and not request.args.get('a').isdigit():
            return {"error_code": 21,
                    "error_message": "empty or wrong params",
                    "reference": None}

    # b参数没有，a存在,a参数类型正确或不正确，都应该返回empty or wrong params————————2case
    if request.args.get('b')==None and request.args.get('a') != None:
        return {"error_code": 21,
                "error_message": "empty or wrong params",
                "reference": None}

    # a,b参数都没有，则返回system error------1case
    return {"error_code": 11,
            "error_message": "system error",
            "reference": None}


if __name__ == '__main__':
    test_app.run()
