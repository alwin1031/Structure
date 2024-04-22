from urllib.request import urlopen
# import html2text

def load_seq(input_code):
    url='https://www.rcsb.org/fasta/entry/'+str(input_code)+'/display'
    page = urlopen(url)
    html_content = page.read()
    # rendered_content = html2text.html2text(html_content)
    # print(html_content)
    file = open(str(input_code)+'.txt', 'wb+')
    file.write(html_content)
    file.close()


if __name__ == '__main__':
    import sys
    import os
    
    input_code = sys.argv[1]
    load_seq(input_code)
