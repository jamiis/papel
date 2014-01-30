'''
vision for arch:
    following = db.blogs.get(user)
    parsed = pool.map(spider, following)
    return httpresponse(parsed)
    get it?
'''
import urllib2
from multiprocessing.dummy import Pool as ThreadPool


urls = [
    "https://medium.com/building-things-on-the-internet/40e9b2b36148",
    "http://scikit-learn.org/stable/modules/hmm.html",
    "http://doc.scrapy.org/en/0.20/intro/tutorial.html",
    "http://nbviewer.ipython.org/url/norvig.com/ipython/xkcd1313.ipynb",
    "http://en.wikipedia.org/wiki/Wavelet",
    "http://en.wikipedia.org/wiki/Compressed_sensing",
    "http://mirkokiefer.com/blog/2013/03/cmake-by-example/",
]

pool = ThreadPool(4)

results = pool.map(urllib2.urlopen, urls)

pool.close()
pool.join()
