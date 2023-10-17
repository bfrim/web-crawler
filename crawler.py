import webdev

title = ""
urls = []
words = []


def crawl(seed):
    global urls, words
    
    urls.clear()
    
    scrape_url(seed)
    
    print(title)
    print(words)
    print(urls)
    
    for i in urls:
        scrape_url("http://people.scs.carleton.ca/~davidmckenney/tinyfruits" + i[1:])
        
        print(title)
        print(words)
        print(urls)
    
    
    return None

def scrape_url(url):
    
    global urls, words, title
    
    words.clear()
    title = ""
    
    x = webdev.read_url(url)
    
    
    i=0
    
    #This is O(n) because the while loops in while loop are just continuing the parent loop.
    while i < (len(x)):
        #If we encounter an opening tag
        if x[i] == "<":
            #Detect title
            if x[i+1] == "t":
                i+=7
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
            #Detect Anchor
            elif x[i+1] == "a":
                i+=3
                link = ""
                while not(x[i]=="<" and x[i+1]=="/"):
                    if x[i-6:i] == "href=\"":
                        while x[i] != "\"" and x[i] != "\'":
                            link+=x[i]
                            i+=1
                        if link not in urls:
                            urls.append(link)
                    i+=1
        i+=1
p = crawl('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html')

            