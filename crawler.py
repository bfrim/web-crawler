import webdev



def crawl(seed):
    webString = webdev.read_url(seed)
    urls = []
    webString=webString.split("\n")
    
    for i in webString:
        index = i.find("href=")
        lastindex = 0

        if index != -1:
            index+=6
            for j in range(index+1, len(i)):
                print(i[j])
                if i[j] == "\"" or i[j] == "\'":
                    urls.append(i[index:j])
                    break
            
            
    
    print(urls)
                
        
    
    return None

p = crawl('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html')

# print(p)