import webdev
import osutil

#srape_url
title = ""
urls = []
localurls = []
words = []

#crawl
baseurl = ""
mainurl = ""


def crawl(seed):
    global urls, words, localurls, baseurl, mainurl
    
    urls.clear()
    
    mainurl = seed
    
    #find baseurl
    i=len(seed)-1
    while seed[i] != "/":
        i -= 1
    baseurl = seed[:i+1]
    print("Base URL is",baseurl)
    
    
    #First scrape
    print("Initiaiting first scrape from seed:", seed)
    scrape_url(seed)
    
    if not(osutil.check_directory("data")):
        osutil.create_directory("data")
        print("Created new directory for data")
    else:
        osutil.delete_directory("data")
        osutil.create_directory("data")
        print("Deleted old directory and created new data directory")
    
    
    osutil.create_file("data","baseurl.txt",[baseurl])
    
    osutil.create_file("data",title+".txt", words )
    print("Words added to data directory", seed)
    osutil.create_file("data",title+"links.txt", localurls)
    print("Links on page added to data directory", seed)
    osutil.create_file("data","title.txt",[title])
    print("Made titiles directory")
    osutil.create_file("data","links.txt",[seed])
    print("Made links directory")
    print()
    
    
    #All scrapes
    print("Beginning scrape of all pages... \n")
    for i in urls:
        scrape_url(i)
        
        osutil.append_file("data","title.txt",title)
        print("Title added to data directory from", i)
        osutil.create_file("data",title+".txt", words )
        print("Words added to data directory from", i)
        osutil.create_file("data",title+"links.txt", localurls)
        print("Links on page added to data directory from", i)
        osutil.append_file("data","links.txt",i)
        print("Link added to main directory")
        print()
    
    
    return None

def scrape_url(url):
    
    global localurls, urls, words, title
    
    words.clear()
    localurls.clear()
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
                        link = baseurl+link[2:]
                        if link not in urls and link != mainurl:
                            urls.append(link)
                        if link not in localurls:
                            localurls.append(link)
                    i+=1
        i+=1

            