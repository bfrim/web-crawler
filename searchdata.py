import webdev
import osutil
import crawler
import math
import matmult

baseurl = ""

urls = []
titles = []
urlMap = {}

initialized = False

#Helper functions
def init(seed):
    global baseurl, initialized, urls, titles, urlMap
    if not(initialized):
        baseurl = osutil.read_file("data","baseurl.txt")[0]
        urls = osutil.read_file("data", "links.txt")
        titles = osutil.read_file("data","title.txt")
        
        urlMap = {}
        for i in range(len(urls)):
            urlMap[urls[i]]=titles[i]
            
        initialized = True
        print("Initialized")

def get_tag(URL):
    init(URL)
    if URL in urlMap:
        return urlMap[URL]
    else: return ''

def get_outgoing_links(URL):
    init(URL)
    tag = get_tag(URL)
    result = osutil.read_file("data/outgoinglinks",tag+".txt")
    
    if result == False:
        return None
    else:
        return result
    
def get_incoming_links(URL):
    init(URL)
    result = []
    tag = get_tag(URL)
    result = osutil.read_file("data/incominglinks",tag+".txt")
    
    if result == False:
        return None
    else:
        return result

def get_idf(word):
    result = osutil.read_file("data/idf",word+".txt")
    if result == False:
        return 0
    else:
        return float(result[0])
    
def get_tf(URL, word):
    init(URL)
    result = []
    tag = get_tag(URL)
    result = osutil.read_file("data/tf",word+tag+".txt")
    if result == False:
        return 0
    else:
        return float(result[0])

def get_tf_idf(URL, word):
    return math.log(1+get_tf(URL,word),2)*get_idf(word)

def get_page_rank(URL):
    init(URL)
    tag = get_tag(URL)
    result = osutil.read_file("data/pagerank",tag+".txt")
    
    if result == False:
        return -1
    else:
        return float(result[0])
