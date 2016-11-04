## install pip, install twitter
import twitter
import datetime
import random


##function to get twitter
# or string
#t = Twitter(auth=OAuth(token, token_key, con_secret, con_secret_key))

##Define array
def RandomGen():
    phrases = ["Hey there, Tiger.","How's my host human doing?'","Smooth Sailing.","Just checking in!","Remember, you're are the face; I am the fluff!","Think it's time for a shave? Naahhhhhhh","...and growing!","Beards are the best", "might be time for a wash","ever thought of investing in styling products",""] 
    randPhrase = random.choice(phrases)
    return randPhrase

randtwit = RandomGen()
post = randtwit +" @NAME" 
print(post)

#t.statuses.update(status='post')


