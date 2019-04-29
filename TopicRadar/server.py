from flask import Flask, jsonify, request, Response, render_template, redirect
import json, time
from apscheduler.schedulers.background import BackgroundScheduler
from flask_pymongo import PyMongo
from flask_cors import CORS
from bson.objectid import ObjectId
import math
from bson import ObjectId
# Chris's code
import GoogleReq

import SearchEngine

#################Scheduler#######################

def Data_Pull():
	print("Getting Google data")
	TrendsUS = GoogleReq.trends_ONLY_JSON("US")
	print(TrendsUS)
	Articles = SearchEngine.getNewsSources(TrendsUS)
	print(Articles)
	storeNewData('US', Articles)
	print("Data Pull Complete...")
	return
	
def Delete_Default_Data():
	print("Deleting Data")
	checkTime('US')
	print("Deleting complete...")
	return
	
def updateLocationData(RC):
	TrendsLOC = GoogleReq.trends_ONLY_JSON(RC)
	print(TrendsLOC)
	Articles = SearchEngine.getNewsSources(TrendsLOC)
	storeNewData(RC, Articles)
	print("Data Pull Complete...")
	print()
	js = JSONEncoder().encode(getData(RC))
	return js

##################################################

#######Fields##############
scheduler = BackgroundScheduler()
scheduler.add_job(Data_Pull, 'interval', minutes=60) # CHange to minutes=15
scheduler.add_job(Delete_Default_Data, 'interval', minutes=60)# CHange to minutes=31
scheduler.start()
app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "http://localhost:4200"}})
app.config['MONGO_URI'] = 'mongodb+srv://TopicRadarUser:0Ym4p1IOpTrmOKbA@topicradar-jmk3c.mongodb.net/TopicRadarDB?retryWrites=true'
mongo = PyMongo(app)
############################

#################DataBase##########################
def storeNewData(location, JSON):
	trend_JSON = []
	article_JSON = []
	z = 0
	for x in JSON:
		article_dict = {'article_id' : x['Article_id'], 'article_title' : x['Title'], 'article_URL' : x['URL'], 'article_post_date' : x['post_date'], 'article_thumbnail' : x['Thumbnail']}
		article_JSON.append(article_dict)
		z = z + 1
		if z%10 == 0:
			trend_dict = {'trend_id' : x['Trend_id'], 'trend_name' : x['Trend'], 'articles' : article_JSON}
			trend_JSON.append(trend_dict)
			article_JSON = []
	data = mongo.db.data
	data.insert_one({'location_tag' : location, 'date_added' : time.time(), 'trends' : trend_JSON})
		
def checkTime(location):
	data = mongo.db.data
	dateAdded = getData(location)['date_added']
	# change 18 to 1800 =15min 
	#add a try catch
	if (dateAdded + 1800) < time.time():
		deleteData(location)
		
def deleteData(location):
	data = mongo.db.data
	data.delete_many({"location_tag" : location})

def getData(location):
	data = mongo.db.data
	for document in data.find({"location_tag" : location}).sort("date_added", -1).limit(1):
		calledData = document
	return calledData

####################################################


########################JSON#########################
class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)

####################################################

#################Routes##############################
@app.route("/")
def defaultSearch():
	# have cookie then use cookie
	RC = request.cookies.get('location')
	if RC is not None:
		print('Location code:'+RC)
		try:
			Json = JSONEncoder().encode(getData(RC))
		except:
			Json = updateLocationData(RC)
	else:
		Json = JSONEncoder().encode(getData('US'))
	resp = Response(Json, status=200, mimetype='application/json')
	resp.headers['Link'] = '127.0.0.1/trenddata'
	return resp

@app.route("/region/<RC>", methods=['GET'])
def regionCodeSearch(RC):
	try:
		Json = JSONEncoder().encode(getData(location))
	except:
		print("No Data for " + RC + ", running update")
		Json = updateLocationData(RC)
	finally:
		checkTime(RC)
	print(Json)
	resp = Response(Json, status=200, mimetype='application/json')
	resp.headers['Link'] = '127.0.0.1/trenddata'
	return resp
	
@app.route("/setLocation/<RC>", methods=['GET'])
def setRegionCookie(RC):
	redirect_to_index = redirect('/')
	response = app.make_response(redirect_to_index )
	response.set_cookie('location',value=RC)
	return response
	
@app.route("/init", methods=['GET'])
def init():
	deleteData('US')
	deleteData('RU')
	deleteData('GB')
	deleteData('BE')
	
	array = ['US','RU','GB', 'BE']
	
	for x in array:
		print("Getting Google data")
		TrendsUS = GoogleReq.trends_ONLY_JSON(x)
		print(TrendsUS)
		Articles = SearchEngine.getNewsSources(TrendsUS)
		print(Articles)
		storeNewData(x, Articles)
		print("Data Pull Complete...")
	
	return redirect("127.0.0.7:5000/")
	
@app.route("/test", methods=['GET'])
def test():
	#array = ['US','RU','GB', 'BE', 'CA', 'SE']
	
	#for x in array:
		#TrendsUS = GoogleReq.trends_ONLY_JSON(x)
		#print(TrendsUS)
	getData('US')
	return "Good"
	
####################################################
	
if __name__ == '__main__':
	app.run(host = '127.0.0.1',port=5000,threaded=True)