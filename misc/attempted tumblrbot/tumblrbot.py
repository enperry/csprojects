import pytumblr

# Authenticate via OAuth
client = pytumblr.TumblrRestClient(
    # redacted
)

# Make the request
posts = client.posts("luv-cat.tumblr.com", limit = 1, type = "photo") 

# print((posts["posts"]))
templist = []
for i in posts["posts"]:  
    templist.append(i.keys())
print(templist)
# posts['posts'].keys()
# someday i will finish this but the tumblr api is a nightmare to navigate
