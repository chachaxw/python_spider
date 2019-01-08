#!/usr/bin/python3
from thread import Thread_mm
from aio_req import Aio_mm
import os,time,requests
from lxml import etree

def getdir():
    if os.path.exists(folder) and len(os.listdir(folder)) > 0:
        return int(max(os.listdir(folder)))
    else:
        return default_start

def getnew():
    try:
        url = 'http://www.mm131.com/xinggan/'
        content = etree.HTML(requests.get(url).text)
        href = content.xpath('//dl[@class="list-left public-box"]//dd[1]/a/@href')[0]
        newid = href[-9:-5]
        return int(newid)

    except Exception as e:
        return default_end

def main_start(begin, end):
    start_time = time.time()

    if os.name == 'nt':
        app = Thread_mm()
        app.go_to_start(begin, end)
    else:
        app = Aio_mm()
        app.go_to_start(begin, end)

    end_time = time.time()
    print('Finish Task ^_^, takes time:', end_time - start_time)


if __name__ == '__main__':
    print("This is a python program")

    folder = 'mm131/'

    default_start, default_end = 2400, 2410

    finished, newid = getdir(), getnew()

    main_start(finished, newid)
