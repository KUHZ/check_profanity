import urllib
def read_text():
     quotes = open("/Users/gu/Desktop/Python/check_profanity/movie_quotes.txt")
     contents_of_file = quotes.read()
     #print(contents_of_file)
     profanity_check(contents_of_file)
     quotes.close()

def profanity_check(text):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text)
    output = connection.read()
    #print(output)
    connection.close()
    if "false" in output:
        print("it's good")
    elif "ture" in output:
        print("watch your language")
    else:
        print("can't scan the text")


read_text()
