import requests
import re
headers = {'Accept-Encoding': 'identity'}
url = input("Enter a vocabulary.com URL: ")
r = requests.get(url, headers)
html = r.text
substring = "class=\"word dynamictext\""

matches = re.finditer(substring, html)
matches_positions = [match.start() for match in matches]

words = []
for i in matches_positions:
    words.append(html[i+43:html[i:].find("\">")+i])

title = html[html.find("<h1")+24:html.find("<h1")+html[html.find("<h1"):].find("</h1>")]
title = "".join(list(filter(lambda a: a not in ["<",">",":","\"","/","\\","|","?","*"], list(title))))
with open(f"word_lists/{title}.txt", "w") as f:
    for i in words:
        f.write(i+"\n")