# coding utf-8
import requests
import json
import time

HOST_URL = "http://localhost:18080"


def get_api():
    start_time = time.clock()

    res = requests.get(
        HOST_URL + '/apiname_get',
        params={'foo': 'bar'})
    print(res.json())

    end_time = time.clock()
    eval_time = start_time - end_time

    print(str(eval_time) + "sec")


def post_api():
    start_time = time.clock()

    res = requests.post(
        HOST_URL + '/apiname_post',
        params={'foo': 'bar'})
    print(res.json())

    end_time = time.clock()
    eval_time = start_time - end_time

    print(str(eval_time) + "sec")


def json_print(res_json_str):
    res_json = json.loads(res_json_str)

    for x in res_json:
        print(x[name])
        print(x[score])


if __name__ == '__main__':

    get_api()
    post_api()

    for r in range(10):
        print("eval" + str(r))
        json_print(get_api())
