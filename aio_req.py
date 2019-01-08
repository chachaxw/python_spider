from set_mm_header import set_header, referer_set
from aiomultiprocess import Pool
import aiohttp, asyncio, time, os

class Aio_mm(object):
    def __init__(self):
        self.folder = 'picture/'
        self.each_limit = 60

    async def get(self, url):
        i = url[24:29]
        j = url[30:-4]

        if not os.path.exists(self.folder + i):
            os.makedirs(self.folder + i)
        
        async with aiohttp.ClientSession() as session:
            print('Waiting for request url', url)
            response = await session.get(url, headers = set_header(url))
            pic = await response.read()

        if response.status == 404:
            return '404 not found!'

        print('Get response from', url, 'Result is:', response.status)

        with open(self.folder + '%s/%s.jpg'% (i, j), 'wb') as pp:
            pp.write(pic)

    async def makeurl(self, start, end, limit):
        urls = ['http://img1.mm131.me/pic/'+str(i)+'/'+str(j)+'.jpg' for i in range(start, end) for j in range(1, limit)]
        return await Pool().map(self.get, urls)

    def go_to_start(self, begin, end):
        task = asyncio.ensure_future(self.makeurl(begin, end, self.each_limit))
        loop = asyncio.get_event_loop()
        loop.run_until_complete(task)


if __name__ == '__main__':
    app = Aio_mm()

    start = time.time()
    app.go_to_start(4600, 4610)
    end = time.time()
    print('Finish Task ^_^, takes time:', end - start)   