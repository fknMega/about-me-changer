#this was made by fknMega on github
import requests


about = input("Enter your about me: ")
combotype = input("Enter a number to select combo type, 1 for combo (user:pass:token) or 2 for normal (token): ")

def change(token):

    r = requests.Session()
    # gets cookies (100% delicious 😋)
    url = "https://discord.com/api/v9/experiments"
    k = r.get(url)
    
    # sends sex request
    url = "https://canary.discord.com/api/v9/users/%40me/profile"
    headers = {"accept": "/",
  
    "authorization": token,
  
    }
    body = {"bio": about}
    
    # Send the friend request
    res = r.patch(url, headers=headers, json=body)
    

    #print the response

    
    
    return res.status_code



f = open("tokens.txt", "r")
times = 0
for line in f:
     token = ""
     if combotype == "1":
        token = line.split(":")[2].replace("\n", "")
     else:
        token = line.replace("\n", "")

     res = change(token)

     if res == 200:
       print('+ Changed about me for: ' + token + ' - ' + str(times))
       times= times+1
     else:
       if res == 401:
          print('- Token is dead: ' + token)
       else:
          print(res)
    


