# -*- coding: UTF-8 -*-

from fbchat import Client
from fbchat.models import *

username = ""
client = Client(username, "humansuper534@human@#")

print("Own id: {}".format(client.uid))

client.send(Message(text="Hi me!"), thread_id=client.uid,
            thread_type=ThreadType.USER)

client.logout()
