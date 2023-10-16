import webdev

# If the given URL was not found during the crawling process, this function must return the value None.
def get_outgoing_links(URL):
    links = []
    page_content = webdev.read_url(URL)

    link_start = page_content.find("<a href=")
    while link_start != -1:
        opening_quote = page_content.find('"', link_start)
        ending_quote = page_content.find('"', opening_quote + 1)
        url = page_content[opening_quote, 1:ending_quote]
        links.append[url]

        link_start = page_content.find("<a href=")
    
    return links

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