from urllib.request import urlopen
def read_text():
    quotes = open("/Users/tgsingh/Desktop/movie_quotes.txt")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)
    
def check_profanity(text_to_check):
    url = "http://www.wdylike.appspot.com/?q="+text_to_check
    print(url)
    connection = urlopen(url)
    output = connection.read()
    print(output)
    connection.close()

read_text()    


#for curse word check use www.wdyl.com made by google to check whether a word is a curse word or not
