import webdev
import osutil
import crawler
import math

baseurl = ""

urls = []
titles = []

initialized = False

#Helper functions
def init(seed):
    global baseurl, initialized, urls, titles
    if not(initialized):
        # crawler.crawl(seed)
        baseurl = osutil.read_file("data","baseurl.txt")[0]
        urls = osutil.read_file("data", "links.txt")
        titles = osutil.read_file("data","title.txt")
        
        initialized = True

def get_tag(url):
    init(url)
    tag = ""
    i = len(baseurl)
    while url[i] != ".":
        tag += url[i]
        i+=1
    return tag

#Important functions
#Complete
def get_outgoing_links(URL):
    init(URL)
    if URL in urls:
        tag = get_tag(URL)
        result = osutil.read_file("data/outgoinglinks",tag+".txt")
        return result
    else:
        return None
    
def get_incoming_links(URL):
    init(URL)
    result = []
    tag = get_tag(URL)
    result = osutil.read_file("data/incominglinks",tag+".txt")
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
   
#Barnabes Work
#In progress
def get_page_rank(URL):
    pass


