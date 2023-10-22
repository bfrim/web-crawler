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
        # crawler.crawl(seed)
        baseurl = osutil.read_file("data","baseurl.txt")[0]
        urls = osutil.read_file("data", "links.txt")
        titles = osutil.read_file("data","title.txt")
        
        urlMap = {}
        for i in range(len(urls)):
            urlMap[urls[i]]=titles[i]
            
        initialized = True

def get_tag(URL):
    init(URL)
    if URL in urlMap:
        return urlMap[URL]
    else: return ''

#Important functions
#Complete
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
   
#Barnabes Work
#In progress
def get_page_rank(URL):
    init(URL)
    map = urls
    matrix = []
    alpha = 0.1

    for i in range(len(map)):
        x = get_incoming_links(map[i])
        matrix.append([])
        for j in range(len(map)):
            if map[j] in x:
                matrix[i].append(1)
                matrix[i][j] /= len(x)
                matrix[i][j] = (1-alpha)*matrix[i][j]
                matrix[i][j] += alpha/len(map)
            else:
                matrix[i].append(0)
                matrix[i][j] += alpha/len(map)
        
    # for i in range(len(map)):
    #     divisor = len(get_incoming_links(map[i]))
    #     for j in range(len(map)):
    #         matrix[i][j] /= divisor
    #         matrix[i][j] = (1-alpha)*matrix[i][j]
    #         matrix[i][j] += alpha/len(map)


    t = [[]]
    for i in range(len(map)):
        t[0].append(1/len(map))
    
    distance = 1
    
    while distance > 0.0001:
        old_t = t
        t = matmult.mult_matrix(t,matrix)
        
        distance = matmult.euclidean_dist(t,old_t)

    try:
        index = map.index(URL)
    except ValueError:
        return -1
    
    return t[0][index]
