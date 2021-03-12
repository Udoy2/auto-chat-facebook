# -*- coding: UTF-8 -*-

import json
import fbchat


def generate(username, password):
    client = fbchat.Client(username, password)
    cookies = client.getSession()
    with open("session.json", "w") as f:
        json.dump(cookies, f)
