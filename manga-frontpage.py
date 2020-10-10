import requests
import re
import os

def getFrontPageImage(url):
    r = requests.get(url)
    content = str(r.content)
    content = content.replace("\"", '')
    content = content.replace("=", ' ')
    content = content.replace(">", ' ')
    content = content.replace("<", ' ')
    contentList = content.split(' ')
    with open("file.txt", 'w') as f:
        f.write(str(contentList))
    for i in range(len(contentList)):
        if contentList[i] == 'img' and contentList[i+1] == 'src' :
            print(contentList[i+2])
            jpglink = contentList[i+2]
            if jpglink != '':
                frontpage = requests.get(jpglink)
                f_ext = os.path.splitext(jpglink)[-1]
                f_name = 'frontpage{}'.format(f_ext)
                with open(f_name, 'wb') as f:
                    f.write(frontpage.content)

def getPageCountPerChapter(url, totalChapter, name):
    pageList = []
    for i in range(1, totalChapter+1):
        _url = url + '/{}'.format(i)
        r = requests.get(_url)
        content = str(r.content)
        pages = content.count('option value="/{}/{}'.format(name, i))
        pageList.append(pages)
    return pageList
    
name = input("Enter the name of the manga:").lower().replace(' ', '-')
totalChapter = int(input("Enter total Chapter count:"))
homeurl = "http://www.mangapanda.com/{}".format(name)
getFrontPageImage(homeurl)
pageList = getPageCountPerChapter(homeurl, totalChapter, name)
count = 0
for c in range(1, totalChapter+1):
    for p in range(1, pageList[c-1]+1):
        url='http://www.mangapanda.com/{}/{}/{}'.format(name, c,p)
        r = requests.get(url)
        content = str(r.content)
        # print(url)
        content = content.replace("\\\'", '')
        content = content.replace(";\\\n", '')
        contentList = content.split(' ')
        with open("file.txt", 'w') as f:
            f.write(str(contentList))
        # regex = r"^https://i[0-9]+\.mangapanda\.com/akuma-no-riddle/[0-9]+/akuma-no-riddle-[0-9]+\.jpg;\\\n$"
        for i in range(len(contentList)):
            if contentList[i] == 'document[pu]':
                # print(contentList[i+2].replace(';\\n', ''))
                jpglink = contentList[i+2].replace(';\\n', '')
                count += 1
                if jpglink != '':
                    page = requests.get(jpglink)
                    f_ext = os.path.splitext(jpglink)[-1]
                    f_name = 'img{}{}'.format(count, f_ext)
                    with open(f_name, 'wb') as f:
                        f.write(page.content)