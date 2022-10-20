from flask_pymongo import pymongo
CONNECTION_STRING = "mongodb+srv://masterboy376:S10a09m2004@samprivatecluster.ebbjt.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(CONNECTION_STRING)
db = client.get_database('blog_blaze')
# posts = pymongo.collection.Collection(db, 'posts')

# mongodb+srv://masterboy376:S10a09m2004@samprivatecluster.ebbjt.mongodb.net/evergoods?retryWrites=true&w=majority