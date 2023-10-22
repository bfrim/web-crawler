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
    for i in range(len(phrase)):
        qvector.append(math.log(1+(words[phrase[i]]/len(phrase)))*searchdata.get_idf(phrase[i]))
    
    #Make a Vector Space Model for Documents
    for i in urls:
        vectors.append([])
    
    for i in range(len(phrase)):
        for j in range(len(urls)):
            vectors[j].append(searchdata.get_tf_idf(urls[j],phrase[i]))
    
    for i in vectors:
        print(i)
    
    print("\n",qvector)
    
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
    
    for i in range(len(cosine)):
        print(cosine[i],urls[i])
            
    
    
    if boost:
        for i in top:
            i["score"] *= searchdata.get_page_rank(i["url"])
        return top
    else:
        return top
    
search("papaya banana", False)