
from flask import Flask, abort, request
from mock_data import catalog
from aboutme import me
import random
import json
from flask_cors import CORS
from config import db
from bson import ObjectId




# create the server/app 
app = Flask("server")
CORS(app) #allow the server to be called from any orgin



@app.route("/", methods=["get"])
def home_page():
    return "Under costruction!"

@app.route("/about")
def about_me():
    return "Leonardo Rios"

@app.route("/myaddress")
def get_address():
    test()
    address=me["address"]
    # return address["street"] + "  " + address["city"]
    # return f"42{} st.{}"
    return f"{address['street']} {address['city']}"


@app.route("/test")
def test():
    return "I'm a simple test"

#############################################
############### API Endpoint ################
#############################################


@app.route("/api/catalog")
def get_catalog():
    
    cursor = db.products.find({})
    results = []
    for prod in cursor:
        prod["_id"] = str(prod["_id"])
        results.append(prod)

    return json.dumps(results)

@app.route("/api/catalog", methods = ["POST"])
def save_products():
    product = request.get_json() #read the payload as a dictionary from json string

    # validate
    # title and longer thatn 5 characters
    if not "title" in product or len(product["title"]) < 5 :
        return abort(400, "Title too short, must be 5 characters long")
    
    # should be a price
    if not "price" in product:
        return abort(400, "Price is required")


    # the price should be an int or a float
    if not isinstance(product["price"], int) and not isinstance(product["price"], float):
        return abort(400, "Price is not a valid price")

    # the price should greater than zero
    if product["price"] <= 0:
        return abort(400, "Price should be higher than $0")

    db.products.insert_one(product)

    # hack to fix _id problem
    product["_id"]= str(product["_id"])


    return json.dumps(product)

# get /api/catalog/count
# return the number of products

@app.route("/api/catalog/count")
def get_count():
    cursor = db.products.find({})
    count = 0
    for prod in cursor:
        count +=1 
        
    json.dumps(count)

# get /api/catalog/sum
# return sum of all prices
@app.route("/api/catalog/sum")
def get_sum():
    total = 0
    cursor = db.products.find({})
    for prod in cursor:
        total+=prod["price"]

        res = f"${total}"
        return json.dumps(res)


# get  /api/product/<id>
# get prod by id
@app.route("/api/product/<id>")
def get_product(id):

    if not ObjectId.is_valid(id):
        return abort(400, "id is not a valid ObjectId")

    prod = db.products.find_one({"_id": ObjectId(id) })

    if not prod:
        return abort(400, "Product not found")

    prod["_id"] = str(prod["_id"])
    return json.dumps(prod)

    # return abort(404) 

# get /api/product/most_expensive
@app.route("/api/products/most_expensive")
def get_most_expensive():
    cursor = db.products.find({})
    pivot = catalog[0]

    for prod in cursor:
        if prod["price"] > pivot["price"]:
            pivot = prod
    
    pivot["_id"]=str(pivot["_id"])
        
    return json.dumps(pivot)

# get /api/categories
#  return a list of strings, representing the UNIQUE categories

@app.route("/api/categories")
def get_categories():
    cursor = db.products.find({})
    
    res = []    
    for prod in cursor:
        category = prod["category"]

        if not category in res: 
            res.append(category)

    return json.dumps(res)

# create an end point that allows the client (react) to retrieve 
# all the products that belong to a specific category
# the client will then send the category and expect a list of products in return



# ? what the URL??  /api/catalog/<category>
@app.route("/api/catalog/<category>")
def products_by_category(category):
    res = []
    cursor = db.products.find({"Catagory":category})

    # fix the id and move the products to res
    for prod in cursor:
        prod["_id"] = str(prod["_id"])
        res.append(prod)
    return json.dumps(res)


################################################
######### API methods for coupon codes##########
################################################

coupons = []

# {
# code:"querty"
# discount:10
# }

# get all get  /api/coupons

# save new post  /api/coupons


# get the code get  /api/coupons/<code>

@app.route("/api/coupons")
def get_coupons():
    return json.dumps(coupons)


@app.route("/api/coupons", methods=["POST"])
def save_coupons():
    coupon = request.get_json()

    db.coupons.insert_one(coupon)
    coupon["_id"] = str(coupon["_id"])
    
    return json.dumps(coupon)


@app.route("/api/coupons/<coupon>")
def get_coupon_by_code(code):
    for coupon in coupons:
        if coupon["code"] == code:
            return json.dumps(coupon)

    return abort(404)



# start the sever
app.run(debug=True)

