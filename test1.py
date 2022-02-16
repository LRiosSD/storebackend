

from audioop import add


def print_name():
    print("you name")

def test_dict():
    print("-----Dictionary-----")

    me = {
        "first":"Leonardo",
        "last" : "Rios",
        "age" : 100,
        "hobbies": [],
        "address": {
            "street":"Small street",
            "city": "Sandy Aye-Go"
        }

    }

    print (me["first"] + " " + me["last"])

    address=me["address"]
    print(address["street"] + "" +address["city"])



print_name()
test_dict()