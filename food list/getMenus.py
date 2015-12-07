import sys
import json
import subprocess
import os

def getMenu(filename):
	foodlist=[]
	reviews=open(filename,"r")
	json_review=json.load(reviews)
	#restaurant_id="4c_TKqGJ527OaWhBRhUCCg"		
	lat=json_review["lat"]
	longitude=json_review["long"]

	name=json_review["name"]#["name"]																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																														;
	json_request={
	  "api_key": "585735a1d9f3c3f02283e334c2797a00582cd271",
	  "fields":["menus"],
	  "venue_queries":[
		{
	 	"name":name,
		"location":{
			"geo" : {
        	  	"$in_lat_lng_radius" : [lat,longitude,500]
			}
		},
		"menus" : { "$present" : "true" }
    		}	
  	]
	};
	#print("curl -X POST https://api.locu.com/v2/venue/search -d '"+json.dumps(json_request)+"'");
#subprocess.call(['curl', '-X', 'POST', "https://api.locu.com/v2/venue/search", '-d', json.dumps(json_request)])
	output=subprocess.check_output(['curl', '-X', 'POST', "https://api.locu.com/v2/venue/search", '-d', json.dumps(json_request)])
	str=output.decode("utf-8")
	#print(str)
	json_output=json.loads(str)
	if json_output["status"]=="error":
		print(json_output)
		sys.exit(1)
	if not json_output["venues"]:
		return None
	menus=json_output["venues"][0]["menus"]
	for menu in menus:
		for section in menu["sections"]:
			for subsection in section["subsections"]:
				for content in subsection["contents"]:
					if(content["type"]=="ITEM"):
						foodlist.append(content["name"])
	return foodlist
if len(sys.argv) != 2:
        print ('USAGE: python preprocessor.py <path to reviews folder>')
        sys.exit(0)
count=0
directory_menus = os.path.dirname('menu/')
if not os.path.isdir(directory_menus):
	os.makedirs(directory_menus)
files=os.listdir(sys.argv[1])

for filename in files:
	foodlist=getMenu(sys.argv[1]+filename)
	if(foodlist!=None):
		menufile=open(os.path.splitext("menu/"+filename)[0]+".txt","w")
		menufile.write(str(foodlist))
		menufile.close()
