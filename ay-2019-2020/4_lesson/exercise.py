import json
from datetime import datetime

print("############## Exercise 1 ")
data = {}

data["name"] = "marilena"
data["age"] = 25
data["profession"] = "student"

list_courses = ["comp-think", "comp-ling", "scholarly-editing", "knowledge-repr"]

data["courses"] = list_courses

data["profession"] = "digital humanist"

for k,v in data.items():
    print(k,v)

for k in sorted(data.keys()):
    print(k)

for course in data["courses"]:
    if "comp" in course:
        print(course)

sent = data["name"]+" is a "+str(data["age"])+"-year-old "+data["profession"]+". Currently, s/he is attending several courses, namely: "+", ".join(list_courses)
print(sent)

print("############## Exercise 2 ")
with open('data.json', 'r', encoding='utf8') as data:
    got = json.load(data)

num_episodes = len(got["Episodes"])
print(num_episodes)

for ep in got["Episodes"]:
    if float(ep["imdbRating"]) > 9.0:
        print(ep["Title"])

    date_ep = datetime.strptime(ep["Released"], "%Y-%m-%d")
    begin_date = datetime.strptime("2011-05-31", "%Y-%m-%d")
    end_date = datetime.strptime("2011-06-30", "%Y-%m-%d")
    if date_ep < end_date and date_ep > begin_date:
        print(ep["Title"])
