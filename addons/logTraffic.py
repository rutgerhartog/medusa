from mitmproxy import ctx
import json

class LogTraffic:
    def __init__(self, flow, args):
        self.flow = flow
        self.type = self.args['type']


    def request(self):

# Request
# Request headers
# SRC IP
# parse auth cookie to include username and such
# Query / post parameters


# Response
# status code
# headers
