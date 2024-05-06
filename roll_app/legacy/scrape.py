from bs4 import BeautifulSoup


'''scrape character skills from Pathbuilder.
   copy html code from Pathbuilder into txt file
   adjust name and filepath before running code'''

name = "player1"
filepath = "pathbuilder_test.txt"

with open(filepath, "r") as f:
    htmldata = f.read()

soup = BeautifulSoup(htmldata, "html.parser")

skills = list(soup.find_all("div", class_="section-skill-name"))
totals = list(soup.find_all("div", class_="section-skill-total"))

skills = [str(v) for v in skills]
totals = [str(v) for v in totals]


combined = [{"name": name}]

for index, i in enumerate(skills):
    i = i.removeprefix('<div class="section-skill-name">')
    skills[index] = i.removesuffix('</div>')

for index, i in enumerate(totals):
    i = i.removeprefix('<div class="section-skill-total">')
    i = i.removeprefix('<div class="section-skill-total" style="margin-left: 57px;">')
    i = i.removeprefix('+')
    totals[index] = int(i.removesuffix('</div>'))

for i in range(len(skills)):
    combined.append({skills[i]: totals[i]})

print(skills)
print(totals)
print(combined)
