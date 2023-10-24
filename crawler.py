import webdev
import osutil
import math
import matmult

#Assigning Variables
#Data we will store for each url then clear or keep for the entire crawl
title = ""
urls = []
words = []
outlinks = []
tf = {}
inlinks = {}
idf = {}

#We will need the baseurl for making absolute links and the mainurl to make sure we dont have a duplicate
baseurl = ""
mainurl = ""

def scrape_url(url):
    global urls, inlinks, idf, words, title, outlinks, tf
    
    #Clear variables for new scrape
    title = ""
    words.clear()
    outlinks.clear()
    tf.clear()
    
    #Get the HTML string from webpage
    webString = webdev.read_url(url)
    
    #Make a new 'pointer' variable
    i=0
    #This is O(n) because the while loops in while loop are just continuing the parent loop.
    #We will keep adding to i until we reach the end of the loop
    while i < (len(webString)):
        #If we encounter an opening tag
        if webString[i] == "<":
            #Check if it is a title
            if webString[i+1:i+6] == "title":
                #Skip through any attributes
                while webString[i] != ">":
                    i+=1
                i+=1
                title = ""
                while not(webString[i]=="<" and webString[i+1]=="/"):
                    title += webString[i]
                    i+=1   
            #Detect Paragraph
            elif webString[i+1] == "p":
                #Skip through any attributes
                while webString[i] != ">":
                    i+=1
                i+=1
                word = ""
                #Until the end tag
                while not(webString[i]=="<" and webString[i+1]=="/"):
                    #Make a word and stop if there is a space or new line
                    if word != "" and (webString[i] == "" or webString[i:i+1] == "\n"):
                        words.append(word.strip())
                        word = ""
                    else:
                        word += webString[i]
                    i+=1
                #Counting words for tf and adding a url to a word if it appears in it
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
                #Actually calculate tf
                for j in tf:
                    tf[j] /= len(words)
                           
            #Detect Anchor
            elif webString[i+1] == "a":
                #Skip <a
                i+=3
                #Initialize link
                link = ""
                while not(webString[i]=="<" and webString[i+1]=="/"):
                    #Keep moving i until you find the href element
                    if webString[i-6:i] == "href=\"":
                        #Make a string until you encounter a quote
                        while webString[i] != "\"" and webString[i] != "\'":
                            link+=webString[i]
                            i+=1
                        #Turn the url into an absolute url
                        link = baseurl+link[2:]
                        #Add these links to a queue used for crawl() but dont do the first one.
                        if link not in urls and link != mainurl:
                            urls.append(link)
                        #Add to outgoinglinks later
                        if link not in outlinks:
                            outlinks.append(link)
                        
                    i+=1
        i+=1


def crawl(seed):
    global urls, words, outlinks, baseurl, mainurl, idf, inlinks
    
    #Clear these here because these will be used for the entire crawl process
    urls.clear()
    idf.clear()
    inlinks.clear()
    
    mainurl = seed
    
    #Finds the base url
    i=len(seed)-1
    while seed[i] != "/":
        i -= 1
    baseurl = seed[:i+1]    
    
    #First scrape in the seed
    scrape_url(seed)
    
    #Makes directories and deletes old ones if they exist
    if not(osutil.check_directory("data")):
        osutil.create_directory("data")
        osutil.create_directory("data/words")
        osutil.create_directory("data/incominglinks")
        osutil.create_directory("data/outgoinglinks")
        osutil.create_directory("data/pagerank")   
        osutil.create_directory("data/tf")
        osutil.create_directory("data/idf")
    else:
        osutil.delete_directory("data/incominglinks")
        osutil.delete_directory("data/outgoinglinks")
        osutil.delete_directory("data/tf")
        osutil.delete_directory("data/idf")
        osutil.delete_directory("data/pagerank")   
        osutil.delete_directory("data/words")
        osutil.delete_directory("data")
        
        osutil.create_directory("data")
        osutil.create_directory("data/words")
        osutil.create_directory("data/incominglinks")
        osutil.create_directory("data/outgoinglinks")
        osutil.create_directory("data/pagerank")   
        osutil.create_directory("data/tf")
        osutil.create_directory("data/idf")    
    #Make 'Global' files that will be used later
    osutil.create_file("data","baseurl.txt",[baseurl])
    osutil.create_file("data","title.txt",[title])
    osutil.create_file("data","links.txt",[seed])
    
    #Adding outgoinglinks and tf data
    osutil.create_file("data/words",title+".txt", words )
    osutil.create_file("data/outgoinglinks",title+".txt", outlinks)
    osutil.create_file_dict("data/tf",title+".txt",tf)
    
    #Begins scrape of all urls, adds urls not found in lists in scrape_url and continues to iterates through added urls 
    for i in urls:
        scrape_url(i)
        
        #Adding outgoinglinks and tf data
        osutil.create_file("data/words",title+".txt", words ) 
        osutil.create_file("data/outgoinglinks",title+".txt", outlinks)
        osutil.create_file_dict("data/tf",title+".txt",tf)
        
        #Adding to 'global' data
        osutil.append_file("data","title.txt",title)
        osutil.append_file("data","links.txt",i)
    
    #Calculating IDF and putting it in a file for each word in the dictioniary idf.
    documentnumber = len(osutil.read_file("data","links.txt"))
    for i in idf:
        idf[i]=math.log(documentnumber/(1+len(idf[i])),2)
        
    osutil.create_file_dict("data/idf",".txt",idf)
    
    #Finding incoming links
    links = osutil.read_file("data","links.txt")
    titles = osutil.read_file("data","title.txt")
    
    #Make a hashmap to access the title/file name for each url in constant time.
    linkMap = {}
    for i in range(len(links)):
        linkMap[links[i]]=titles[i]
    
    #Loop through each url
    for i in range(len(links)):
        #Find the current url and it's file_name/title
        link = links[i]
        linktitle = titles[i]
        
        #Read the links it goes too
        inlink = osutil.read_file("data/outgoinglinks",linktitle+".txt")
        
        #Look through each link it points too
        for j in inlink:
            #Find it's title
            intitle = linkMap[j]
            #If the file already exists, add the link we are reading from to the file of the link it pointed to. If it does not make a new one
            if osutil.check_file("data/incominglinks",intitle+".txt"):
                osutil.append_file("data/incominglinks",intitle+".txt",link)
            else:
                osutil.create_file("data/incominglinks",intitle+".txt",[link])
    
    #Calculating Pageranks
    #Make constants and important variables
    map = links
    matrix = []
    alpha = 0.1

    #This for loop maps each link to a matrix and applies all calculations to calculate adjacency to scale.
    for i in range(len(map)):
        x = osutil.read_file("data/incominglinks",titles[i]+".txt")
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

    #Initialize vector for distance calculation
    t = [[]]
    for i in range(len(map)):
        t[0].append(1/len(map))
    
    distance = 1
    
    #Keep multiplying the matrix until the distance between the old t and new t is less than 0.0001
    while distance > 0.0001:
        old_t = t
        t = matmult.mult_matrix(t,matrix)
        
        distance = matmult.euclidean_dist(t,old_t)
    
    #Add each pagerank value to its related file/webpage
    for i in range(len(titles)):
        osutil.create_file("data/pagerank",titles[i]+".txt", [t[0][i]])
        
