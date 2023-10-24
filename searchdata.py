import osutil
import math

#Global variables used to reduce runtime complexity
baseurl = ""
urls = []
titles = []
urlMap = {}
initialized = False

#This init function will find the baseurl, and add all urls, and titles to lists. It will also make a hashmap to reduce runtime complexity when finding a filename for a url.
#O(n) 
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

#Returns the correct filename for a url, blank if not found.
#O(1) if init() has been run, O(n) otherwise
def get_tag(URL):
    init(URL)
    if URL in urlMap:
        return urlMap[URL]
    else: return ''

#Returns the outgoing links from the directory data/outgoinglinks.
#O(n) 
def get_outgoing_links(URL):
    init(URL)
    tag = get_tag(URL)
    result = osutil.read_file("data/outgoinglinks",tag+".txt")
    
    if result == False:
        return None
    else:
        return result

#Returns the incoming links from the directory data/incominglinks.
#O(n) 
def get_incoming_links(URL):
    init(URL)
    result = []
    tag = get_tag(URL)
    result = osutil.read_file("data/incominglinks",tag+".txt")
    
    if result == False:
        return None
    else:
        return result

#Returns the idf value from the directory data/idf.
#O(1) if init() has been run, O(n) otherwise
def get_idf(word):
    result = osutil.read_file("data/idf",word+".txt")
    if result == False:
        return 0
    else:
        return float(result[0])

#Returns the tf value from the directory data/tf.
#O(1) if init() has been run, O(n) otherwise
def get_tf(URL, word):
    init(URL)
    result = []
    tag = get_tag(URL)
    result = osutil.read_file("data/tf",word+tag+".txt")
    if result == False:
        return 0
    else:
        return float(result[0])

#Returns the value tf_idf using the previous two functions
#O(1) if init() has been run, O(n) otherwise
def get_tf_idf(URL, word):
    return math.log(1+get_tf(URL,word),2)*get_idf(word)

#Returns the pagerank value from the directory, data/pagerank
#O(1) if init() has been run, O(n) otherwise
def get_page_rank(URL):
    init(URL)
    tag = get_tag(URL)
    result = osutil.read_file("data/pagerank",tag+".txt")
    
    if result == False:
        return -1
    else:
        return float(result[0])
