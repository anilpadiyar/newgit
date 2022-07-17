import pymongo

client = pymongo.MongoClient("mongodb+srv://ineuron:mongodb123@cluster0.goi2j.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d ={
    'name':'anil',
    'email':'apadiyar@csc.com  ',
    'surname':'padiyar'
}
d1 ={
    'name':'anil',
    'email':'apadiyar@csc.com  ',
    'surname':'padiyar'
}
db1 =client[]