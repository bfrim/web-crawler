import webdev



def crawl(seed):
    x = webdev.read_url(seed)
    urls = []
    
    i=0
    
    print(x)
    
    while i < (len(x)):
        if x[i] == "<":
            #Detect title
            if x[i+1] == "t":
                i+=7
                title = ""
                while not(x[i]=="<" and x[i+1]=="/"):
                    title += x[i]
                    i+=1
                print("Title:",title)
                    
            #Detect Paragraph
            elif x[i+1] == "p":
                i+=3
                word = ""
                while not(x[i]=="<" and x[i+1]=="/"):
                    
                    if word != "" and (x[i] == "" or x[i] == "\n"):
                        # print(word)
                        word = ""
                    else:
                        word += x[i]
                    i+=1
            #Detect Anchor
            elif x[i+1] == "a":
                i+=3
                link = ""
                while not(x[i]=="<" and x[i+1]=="/"):
                    print(x[i-6:i])
                    if x[i-6:i] == "href=\"":
                        while x[i] != "\"" and x[i] != "\'":
                            link+=x[i]
                            i+=1
                        urls.append(link)
                    i+=1
        
        i+=1
    
    print(urls)
                
        
    
    return None

p = crawl('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html')

# print(p)


    # for i in webString:
    #     index = i.find("href=")
    #     lastindex = 0

    #     if index != -1:
    #         index+=6
    #         for j in range(index+1, len(i)):
    #             print(i[j])
    #             if i[j] == "\"" or i[j] == "\'":
    #                 urls.append(i[index:j])
    #                 break
            