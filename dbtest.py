from pymongo import MongoClient
db_name = 'mydb'
db_host = 'ds149934.mlab.com'
db_port = 49934
db_user = 'Hector Huapaya'
db_pass = 'Admision1'

connection = MongoClient(db_host,db_port)
db = connection[db_name]
db.authenticate(db_user,db_pass)
user_collection = db.user
user_records = user_collection.find()
for cur_user in user_records:
    print(cur_user['user'] + ' ' + cur_user['pass'] + '\n')