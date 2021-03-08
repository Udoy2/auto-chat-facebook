import fbchat
from fbchat import Client
from getpass import getpass

username = ""
client = fbchat.Client(username, getpass())
no_of_friends = int(input("Number of friends: "))
for i in range(no_of_friends):
    name = str(input("Name: "))
    friends = client.searchForUsers(name)
    friend = friends[0]
    msg = str(input("Message : "))
    sent = client.send(fbchat.models.Message(msg), friend.uid)
    if sent:
        print("Message sent successfully!!")
