import webdev
import osutil
import crawler

baseurl = ""
urls = []
initialized = False

def init(seed):
    global baseurl, initialized, urls
    if not(initialized):
        crawler.crawl(seed)
        baseurl = osutil.read_file("data","baseurl.txt")[0]
        urls = osutil.read_file("data", "links.txt")
        initialized = True

def get_tag(url):
    init(url)
    tag = ""
    i = len(baseurl)
    while url[i] != ".":
        tag += url[i]
        i+=1
    return tag
    
# If the given URL was not found during the crawling process, this function must return the value None.
def get_outgoing_links(URL):
    init(URL)
    if URL in urls:
        tag = get_tag(URL)
        result = osutil.read_file("data",tag+"links.txt")
        return result
    else:
        return None

print(get_outgoing_links("http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html"))

def get_incoming_links(URL):
    pass

def get_page_rank(URL):
    pass

def get_idf(word):
    pass

def get_tf(URL, word):
    pass

def get_tf_idf(URL, word):
    pass