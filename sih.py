from bs4 import BeautifulSoup
import requests

response = requests.get("https://facilities.aicte-india.org/dashboard/pages/faculties.php")
web_page = response.text
# print(web_page)
soup = BeautifulSoup(web_page, "html.parser")
tag = soup.find_all(name="td")
texts = []
links = []
for a in tag:
    text = a.getText()
    print(text)
    texts.append(text)
    # link = a.get("href")
    # links.append(link)

#upvote = [int(s.getText().split()[0]) for s in soup.find_all(name="span", class_="score")]
print(texts)
# print(links)
# print(upvote)
# print(soup.select("span a").__getattribute__())

# for i in range(3):
#     largest = upvote.index(max(upvote))
#     print(texts[largest])
#     print((links[largest]))

with open("sih.txt", "w", encoding="utf-8") as file:
    for text in texts:
        file.write(text + "\n")

print("Data saved to 'scraped_data.txt'")


