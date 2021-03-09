import fbchat
from fbchat import Client
from getpass import getpass
from datetime import datetime
import time
import json

class Autochat:
    def __init__(self, username, password, friend_name, msg, year, month, day, hour, minn):
        self.username = username
        self.password = password
        self.friend_name = friend_name
        self.msg = msg
        self.msg_to_send = datetime(
            int(year), int(month), int(day), int(hour), int(minn), 00)

    def send_message(self):
        with open("session.json") as f:
            cookies = json.load(f)
        client = fbchat.Client(self.username, self.password, session_cookies=cookies)
        friends = client.searchForUsers(self.friend_name)
        friend = friends[0]
        count = 0
        while True:
            count += 1
            current_time = datetime.now()
            if current_time > self.msg_to_send:
                for m in self.msg:
                    time.sleep(2.5)
                    sent = client.send(fbchat.models.Message(m), friend.uid)
                    if sent:
                        print("Message sent successfully!!")
                break
            else:
                if count >= 60:
                    print(current_time.strftime("%H:%M:%S"))
                    count = 0
            time.sleep(1)


def app():
    ############################################## variables that needs to change according to users wish #############################################################

    username = ""  # email or phone no of id

    passs = ""  # password of id
    name = "Jihad Hossain"    # id name to send message
    msg = ['hello', 'hi i am working',
           'Its midnight I 😂😂😂😂😂😂😂 was thinking that I will wish you a happy birthday that"s why I made this bot to do it instead of me..:P']  # list of messages to send
    year = 2021  # the year of message to send
    month = 2    # the month of message to send
    day = 1     # the day of message to send
    hour = 17    # the hour of message to send, its in 24 hour formate
    minn = 47    # the min to send message

    ######################################################x-------variables that needs to change according to users wish----------x#######################################

    chat = Autochat(username, passs, name, msg, year, month, day,  hour, minn)
    chat.send_message()


if __name__ == "__main__":
    app()
