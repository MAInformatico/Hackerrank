from html.parser import HTMLParser
class Parser(HTMLParser):
    def handle_starttag(self, tag, attrs):        
        print ('Start :',tag)
        for iter in attrs:
            print ('->',iter[0],'>',iter[1])
            
    def handle_endtag(self, tag):
        print ('End   :',tag)
        
    def handle_startendtag(self, tag, attrs):
        print ('Empty :',tag)
        for iter in attrs:
            print ('->',iter[0],'>',iter[1])
            
ObjectParser = Parser()
ObjectParser.feed(''.join([input().strip() for _ in range(int(input()))]))
