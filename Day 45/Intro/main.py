from bs4 import BeautifulSoup
with open("website.html", "r") as file:
    content = file.read()

soup = BeautifulSoup(content, "html.parser")
# print(soup.title)
# print(soup.title.name)

# find_all - gives us all the elements with the tag
all_anchor_tags = soup.find_all(name = "a")
# print(all_anchor_tags)

for tag in all_anchor_tags:
    # print(tag.getText())
    # print(tag.get("href"))
    pass

# going into the h3 where the class reside
section_heading = soup.find(name = "h3", class_ = "heading")
print(section_heading.getText())

company_url = soup.select_one(selector= "p a")
print(company_url.getText)
