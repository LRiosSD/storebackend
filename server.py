from flask import Flask
from mock_data import catalog
from aboutme import me
import json



# create the server/app 
app = Flask("server")



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
    return json.dumps(catalog)

# deg /api/catalog/count
# return the number of products

@app.route("/api/catalog/count")
def get_count():
    count = len(catalog) #?? get the length of catalog
    return json.dumps(count)


# start the sever
app.run(debug=True)

