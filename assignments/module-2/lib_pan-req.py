import requests
import pandas

url="https://fakestoreapi.com/products"

req=requests.get(url)
data=req.json()
total=0

p=pandas.DataFrame(data)[["id","title","price"]]


for i in data:
    total +=i['price']

print(p)

print("sum of price:",total)







"""print(data)

for i in data:
    print("product id:",i["id"])
    print("product name:",i["title"])
    print("price:",["price"])"""