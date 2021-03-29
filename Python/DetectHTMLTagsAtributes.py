from html.parser import HTMLParser
class Parser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for it in attrs:
            print('->',it[0],'>',it[1])

parser = Parser()
for _ in range(int(input())):
    parser.feed(input())
