import requests;

def getBookingAPI() :
    response = requests.get("https://restful-booker.herokuapp.com/booking")

    # to print status code
    print("status code: "+str(response.status_code))
    # to print response body
    # print("response body: \n"+response.text)

# to handle request headers and Body 
def authicationAPI():
    Url = "https://restful-booker.herokuapp.com/auth"
    Headers = {
        "Content-Type": "application/json"
    }

    Json = {
        "username" : "admin",
        "password" : "password123"
    }

    response2 = requests.post(url=Url, headers=Headers, json=Json)

    print("status code: "+str(response2.status_code))

    print("response body: \n"+response2.text)


