#PROG_ASSIGN_23915_700743277
from flask import Flask, Response, request, render_template, jsonify,make_response
import pymongo
import json
from bson.objectid import ObjectId

#Creating the Flask app
app=Flask(__name__)

#Connecting to the Database
try:
    client = pymongo.MongoClient("mongodb+srv://<username>:<password>@cluster0.hlrnkae.mongodb.net/?retryWrites=true&w=majority")
    db = client.DB    
except:
    print("Error -connect to db")

#Get Request to fetch all the records in database
@app.route('/api', methods=['GET'])
def searchall():
  try:
    documents = db.Hulu.find()
    output = [{item: data[item] for item in data if item != '_id'} for data in documents]
    return jsonify(output)
  except Exception as ex:
    response = Response("Search Records Error!!",status=500,mimetype='application/json')
    return response

#Get Request with title parameter to fetch the specific record with given title
@app.route('/api/<string:title>', methods=['GET'])
def search_with_title(title):
  try:
    documents=db.Hulu.find({'title': title})
    output = [{item: data[item] for item in data if item != '_id'} for data in documents]
    if(output):
       response=jsonify(output)
       response.status_code=200
       return response
    else:
       response=jsonify("There is no record with title '"+title+"'")
       response.status_code=200
       return response     
  except Exception as ex:
    response = Response("Search Records Error!!",status=500,mimetype='application/json')
    return response

#Post Request to insert a new record
@app.route('/api', methods=['POST'])
def add_record():
  _json=request.json
  #Checking if json data contains all the columns correctly
  required=("id","title","description","score","rating", "clips_count","episodes_count","genres","seasons_count","company","released_at")
  for key in required:
     if key in _json:
        continue
     else:
         # Prompt the user to insert all the columns
         response=jsonify(key+" column is missing.Please insert all the columns")
         return response         
  _id=_json['id']
  _title=_json['title']
  _clips_count=_json['clips_count']
  _description=_json['description']
  _episodes_count=_json['episodes_count']
  _genres=_json['genres']
  _score=_json['score']
  _seasons_count=_json['seasons_count']
  _company=_json['company']
  _released_at=_json['released_at']
  _rating=_json['rating']
  if request.method == "POST":
    id = db.Hulu.insert_one({'id': _id,'title': _title,'clips_count': _clips_count,'description': _description,'episodes_count': _episodes_count,
    'genres': _genres,'score': _score,'seasons_count': _seasons_count,'company': _company,'released_at': _released_at,'rating': _rating})
    response=jsonify("Record with title '"+_title+"' inserted successfully")
    response.status_code= 200
    return response

#Patch Request to update a particular record with given title parameter
@app.route('/api/<string:title>',methods=['PATCH'])
def update_record(title):
    _title = title
    _json = request.json
    #Checking if json data contains all the columns correctly
    required=("id","title","description","score","rating")
    for key in required:
      if key in _json:
         continue
      else:
         # Prompt the user to insert all the columns
         response=jsonify(key+" column is missing.Please insert all the columns")
         return response 
    #Checking if json data contains other than id,title,description,score and rating
    not_required=("clips_count","episodes_count","genres","seasons_count","company","released_at")
    for key in not_required:
        if key in _json:
          # Prompt the user to insert only required values
          response=jsonify("Please insert Id, Title, Description, Score and Rating only")
          return response    
    _id = _json['id']
    _title = _json['title']
    _description = _json['description']
    _score = _json['score']
    _rating = _json['rating']
    if request.method == "PATCH":
        documents=db.Hulu.find({'title': title})
        output = [{item: data[item] for item in data if item != '_id'} for data in documents]
        if(output):
          document=db.Hulu.update_many( { 'title': title },{'$set':{'id':_id,'title':_title,'description':_description,'score':_score,'rating':_rating}})
          response = jsonify(" Record with title '"+title+"' updated successfully")
          response.status_code = 200
        else:
          response=jsonify("There is no record with title '"+title+"'. 0 records updated")      
        return response

#Delete Request to delete a particular record with given title parameter
@app.route('/api/<string:title>', methods=['DELETE'])
def delete_record(title):
  try:
    document=db.Hulu.find_one({'title': title})
    db.Hulu.delete_many({'title': title})
    response=jsonify("Deleted record with title '"+title+"' successfully")
    response.status_code = 200
    return response
  except Exception as ex:
    response = Response("Delete Records Error!!",status=500,mimetype='application/json')
    return response
   
#Launching the Flask app
if __name__ == '__main__':
    app.run(port=5000, debug=True)
