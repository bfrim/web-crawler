import osutil
import searchdata
import math

def search(phrase, boost):
    urls = osutil.read_file('data',"links.txt")
    titles = osutil.read_file('data',"title.txt")
    
    top = []
    vectors = []
    
    phrase = phrase.split()
    qvector = []
    words = {}
    #Make the Query Vector
    for i in phrase:
        if i in words:
            words[i] +=1
        else:
            words[i] = 1
        
    for i in words:
        qvector.append(math.log(1+words[i]/len(phrase))*searchdata.get_idf(i))
    
    #Make a Vector Space Model for Documents
    for i in urls:
        vectors.append([])
    
    for i in words:
        for j in range(len(urls)):
            vectors[j].append(searchdata.get_tf_idf(urls[j],i))
    
    
    numerator = 0
    leftdenom = 0
    rightdenom = 0
    
    cosine = []
    for i in range(len(vectors)):
        numerator = 0
        leftdenom = 0
        rightdenom = 0
        for j in range(len(qvector)):
            numerator += vectors[i][j]*qvector[j]
            leftdenom += (qvector[j])**2
            rightdenom += (vectors[i][j])**2
        if numerator == 0:  
            cosine.append(0)
        else: cosine.append((numerator)/((leftdenom**0.5)*(rightdenom**0.5)))
    
    if boost:
        for i in range(len(cosine)):
            cosine[i] *= searchdata.get_page_rank(urls[i])
    
    already_picked = []
    
    for i in range(10):
        high = -1
        high_index = -1
        for j in range(len(cosine)):
            if (cosine[j] > high) and (j not in already_picked):
                high = cosine[j]   
                high_index = j
        top.append({"url":urls[high_index],"title":titles[high_index],"score":cosine[high_index]})
        already_picked.append(high_index)

    return top