
'''
import urllib.request
url = "http://i9.mangapanda.com/akuma-no-riddle/1/akuma-no-riddle-4901925.jpg"

pageList = []


page = requests.get(url)

f_ext = os.path.splitext(url)[-1]
f_name = 'img{}'.format(f_ext)
with open(f_name, 'wb') as f:
    f.write(page.content)
'''
import requests
import re
import os
# TOTAL NUMBER OF PAGES IN EACH CHAPTER
totalChapter = 46
# pageList = []
# for i in range(1, totalChapter+1):

    # url='http://www.mangapanda.com/akuma-no-riddle/{}'.format(i)
    # r = requests.get(url)
    # content = str(r.content)
    # pages = content.count('option value="/akuma-no-riddle/{}'.format(i))
    # pageList.append(pages)
# print(pageList)
jpgNo = 4901845
pageNo = 1
count = 0
pageList = [42, 25, 9, 23, 17, 17, 
            17, 20, 10, 19, 16, 18, 
            25, 19, 24, 16, 17, 14, 
            17, 16, 20, 17, 11, 16, 
            17, 25, 17, 25, 18, 13, 
            21, 13, 16, 9, 17, 17, 
            12, 12, 16, 8, 12, 15, 
            15, 16, 7, 10]
print(pageList)
# for c in range(1, totalChapter+1):
for c in range(3, 4):
    for p in range(1, pageList[c-1]+1):
        url='http://www.mangapanda.com/akuma-no-riddle/{}/{}'.format(c,p)
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
    # break