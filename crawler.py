import webdev
import osutil
import math

#srape_url
title = ""
urls = []

words = []

outlinks = []

inlinks = {}

tf = {}
idf = {}


#crawl
baseurl = ""
mainurl = ""
def get_tag(url):
    tag = ""
    i = len(baseurl)
    while url[i] != ".":
        tag += url[i]
        i+=1
    return tag

def crawl(seed):
    global urls, words, outlinks, baseurl, mainurl, idf, inlinks
    
    urls.clear()
    idf.clear()
    inlinks.clear()
    
    mainurl = seed
    
    #find baseurl
    i=len(seed)-1
    while seed[i] != "/":
        i -= 1
    baseurl = seed[:i+1]
    print("Base URL is",baseurl)
    
    
    #First scrape
    scrape_url(seed)
    
    if not(osutil.check_directory("data")):
        osutil.create_directory("data")
        osutil.create_directory("data/words")
        osutil.create_directory("data/incominglinks")
        osutil.create_directory("data/outgoinglinks")
        osutil.create_directory("data/tf")
        osutil.create_directory("data/idf")
    else:
        osutil.delete_directory("data/incominglinks")
        osutil.delete_directory("data/outgoinglinks")
        osutil.delete_directory("data/tf")
        osutil.delete_directory("data/idf")
        osutil.delete_directory("data/words")
        osutil.delete_directory("data")
        
        osutil.create_directory("data")
        osutil.create_directory("data/words")
        osutil.create_directory("data/incominglinks")
        osutil.create_directory("data/outgoinglinks")
        osutil.create_directory("data/tf")
        osutil.create_directory("data/idf")    
    
    osutil.create_file("data","baseurl.txt",[baseurl])
    osutil.create_file("data","title.txt",[title])
    osutil.create_file("data","links.txt",[seed])
    
    
    osutil.create_file("data/words",title+".txt", words )
    
    osutil.create_file("data/outgoinglinks",title+".txt", outlinks)
    
    osutil.create_file_dict("data/tf",title+".txt",tf)
    
    

    #All scrapes
    print("Beginning scrape of all pages... \n")
    for i in urls:
        scrape_url(i)
        
        #word data
        osutil.create_file("data/words",title+".txt", words ) 
        #outgoing links
        osutil.create_file("data/outgoinglinks",title+".txt", outlinks)
        #tf data
        osutil.create_file_dict("data/tf",title+".txt",tf)
        
        #data
        osutil.append_file("data","title.txt",title)
        osutil.append_file("data","links.txt",i)
    
    #idf data
    documentnumber = len(osutil.read_file("data","links.txt"))
    for i in idf:
        idf[i]=math.log(documentnumber/(1+len(idf[i])),2)
        
    osutil.create_file_dict("data/idf",".txt",idf)
    
    #incoming links
    links = osutil.read_file("data","links.txt")
    titles = osutil.read_file("data","title.txt")
    
    linkMap = {}
    for i in range(len(links)):
        linkMap[links[i]]=titles[i]
        
    for i in range(len(links)):
        link = links[i]
        linktitle = titles[i]
        
        inlink = osutil.read_file("data/outgoinglinks",linktitle+".txt")
        
        for j in inlink:
            intitle = linkMap[j]
            if osutil.check_file("data/incominglinks",intitle+".txt"):
                osutil.append_file("data/incominglinks",intitle+".txt",link)
            else:
                osutil.create_file("data/incominglinks",intitle+".txt",[link])
    
    
    return None

def scrape_url(url):
    
    global urls, words, title, outlinks, inlinks, tf, idf
    
    title = ""
    words.clear()
    
    outlinks.clear()
    tf.clear()
    
    
    x = webdev.read_url(url)
    
    
    i=0
    
    #This is O(n) because the while loops in while loop are just continuing the parent loop.
    while i < (len(x)):
        #If we encounter an opening tag
        if x[i] == "<":
            #Detect title
            if x[i+1:i+6] == "title":
                while x[i] != ">":
                    i+=1
                i+=1
                title = ""
                while not(x[i]=="<" and x[i+1]=="/"):
                    title += x[i]
                    i+=1   
            #Detect Paragraph
            elif x[i+1] == "p":
                i+=3
                word = ""
                while not(x[i]=="<" and x[i+1]=="/"):
                    if word != "" and (x[i] == "" or x[i] == "\n"):
                        words.append(word.strip())
                        word = ""
                    else:
                        word += x[i]
                    i+=1
                #Time to calculate some idf and tf :)
                for j in words:
                    #tf conditionals
                    if j not in tf:
                        tf[j] = 1
                    elif j in tf:
                        tf[j] += 1
                    #idf conditionals
                    if j not in idf:
                        idf[j] = [url]
                    elif j in idf:
                        if url not in idf[j]:
                            idf[j].append(url)
                for j in tf:
                    tf[j] /= len(words)
                           
            #Detect Anchor
            elif x[i+1] == "a":
                i+=3
                link = ""
                while not(x[i]=="<" and x[i+1]=="/"):
                    if x[i-6:i] == "href=\"":
                        while x[i] != "\"" and x[i] != "\'":
                            link+=x[i]
                            i+=1
                        link = baseurl+link[2:]
                        #Links conditional
                        if link not in urls and link != mainurl:
                            urls.append(link)
                        if link not in outlinks:
                            outlinks.append(link)
                        
                    i+=1
        i+=1
        
p = crawl("http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html")
            