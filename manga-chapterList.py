import requests

url='http://www.mangapanda.com/akuma-no-riddle/4'

# in case you need a session

r = requests.get(url)
# or without a session: r = requests.get(url)
content = str(r.content)
# print(str(content))
print(content.count('option value="/akuma-no-riddle/4') )