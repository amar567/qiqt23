import json

# Opening JSON file
f = open('data.json')

# returns JSON object as
# a dictionary
data = json.load(f)

# Iterating through the json
# list
for i in data:
	# print(i)
	if len(i["Name"]) > 88 :
		N = 100 - (12 + len(i["Name"])) - 3
		VIDEO_ID = (i["Link"])
		title = ('QIQT23 | ' + i['Name'] + ' - ' + i["Title"][0:N] + '...' )
		description = ("Please visit https://qiqt2023.org/ for more information \n \n Speaker:" + i["Name"] + " - " + i["Affiliation"]  + "\n \n Abstract:" + i["Abstract"])
		thumbnail_path = ('./thumbnails/'+i["Image name"])
	else:
		N = len(i["Title"])
		VIDEO_ID = (i["Link"])
		title = ('QIQT23 | ' + i['Name'] + ' - ' + i["Title"][0:N] )
		description = ("Please visit https://qiqt2023.org/ for more information \n \nSpeaker:" + i["Name"] + " - " + i["Affiliation"] + "\n \nAbstract:" + i["Abstract"])
		thumbnail_path = ('./thumbnails/'+i["Image name"]+".png")


# Closing file
f.close()
