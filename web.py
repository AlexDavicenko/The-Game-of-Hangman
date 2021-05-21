import requests
import re


def pull(url):
    if "www.vocabulary.com/lists/" not in url:
        return False
    if "https://" not in url:
        url = "https://"+url

    headers = {'Accept-Encoding': 'identity'}
    r = requests.get(url, headers)
    html = r.text

    if "Page Not Found</h1>" in html:
        return False

    substring = "class=\"word dynamictext\""
    matches = re.finditer(substring, html)
    matches_positions = [match.start() for match in matches]

    words = []
    for i in matches_positions:
        words.append(html[i+43:html[i:].find("\">")+i])

    title = html[html.find("<h1")+24:html.find("<h1")+html[html.find("<h1"):].find("</h1>")]
    title = "".join(list(filter(lambda a: a not in ["<",">",":","\"","/","\\","|","?","*"], list(title))))

    if not title:
        title = html[(html.find("<h1 class=\"title\""))+18:html[html.find("<h1 class=\"title\""):].find("</h1>")+html.find("<h1 class=\"title\"")]

    with open("words_lists/Untitled.txt" if not title else f"word_lists/{title}.txt", "w") as f:
        for i in words:
            f.write(i+"\n")

    return f"word_lists/{title}.txt"
