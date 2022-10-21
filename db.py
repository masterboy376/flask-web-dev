from flask_pymongo import pymongo
import json

with open('config.json', 'r') as f:
    params = json.load(f)['params']

if(params['local_server']):
    CONNECTION_STRING = params['local_uri']
else:
    CONNECTION_STRING = params['prod_uri']

client = pymongo.MongoClient(CONNECTION_STRING)
db = client.get_database('blog_blaze')
# posts = pymongo.collection.Collection(db, 'posts')

# mongodb+srv://masterboy376:S10a09m2004@samprivatecluster.ebbjt.mongodb.net/evergoods?retryWrites=true&w=majority