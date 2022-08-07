import requests

URL = "http://127.0.0.1:5000/users"

def deactivate_user(id):

    #user = {
    #    "active": active
    #}
    
    url = URL+"/"+id

    response = requests.delete(url)
    if response.status_code == 204:
        print(
            "Successfuly deactivated the id: %d", id)
    else:
        print(
            "Something went wrong while trying to deactivate user id: %s" %id
        )

if __name__ == "__main__":
    fid = input ("Type in the user's id to deactivate: ")
    deactivate_user(fid)