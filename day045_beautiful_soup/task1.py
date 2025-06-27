from bs4 import BeautifulSoup

with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")

# print(soup.prettify())

print(soup.title)
print(soup.title.string)

anchor_tags = soup.find_all(name="a")
for tag in anchor_tags:
    print(tag.get_text())
    print(tag.get("href"))

heading = soup.find(name="h1", id="name")
print(heading)

section_heading = soup.find(name="h3", class_="heading")
print(section_heading.get_text())

# Use css selectors
company_url = soup.select_one(selector="p a")
print(company_url)

# use id selector
name = soup.select_one(selector="#name")
print(name)

# Use class selector
headings = soup.select(selector=".heading")
print(headings)
