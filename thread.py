from set_mm_header import set_header, referer_set
from concurrent import futures
import requests, os, time

class Thread_mm(object):

    def __init__(self):
        self.folder = 'picture/'
        self.each_limit = 60
    
    def get(self, url, i, j):
        response = requests.get(url, headers=set_header(url))
        pic = response.content

        if response.status.code == 404:
            return '404 not found'
        if not os.path.exists(self.folder + i):
            os.makedirs(self.folder + i)
        with open(self.folder + '%s/%s.jpg'% (i, j), 'wb') as pp:
            pp.write(pic)
        return 'Get Pictures Ok!'

    def req(self, ij):
        i = ij[:4]
        j = ij[4:]
        url = 'http://img1.mm131.me/pic/'+i+'/'+j+'.jpg'
        print('Waiting for request url', url)
        result = self.get(url, i, j)
        print('Get response from', url, 'Result is:', result)
        
    def go_to_start(self, begin, end, works = 100, **kw):
        with futures.ThreadPoolExecutor(works) as e:
            e.map(self.req, [ str(i) + str(j) for i in range(begin, end) for j in range(1, self.each_limit) ])


if __name__ == '__main__':
    app = Thread_mm()

    start = time.time()
    app.go_to_start(2500, 2510)
    end = time.time()
    print('Finish Task ^_^, takes time:', end - start)