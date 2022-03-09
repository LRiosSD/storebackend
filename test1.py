

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


def younger_person():
    ages = [12,42,32,50,56,14,78,30,51,89,12,38,67,10]

    # print the smallest number
    pivot = ages[0]
    for age in ages:
        if age < pivot:
            pivot = age
    
    print(f"The result is : {pivot}")


print_name()
test_dict()

younger_person()

#  function to rint your n ame
# call the function 