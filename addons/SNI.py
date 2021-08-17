import ipaddress

class SNI:
    def __init__(self, flow, args):
        self.url = flow.requests.url
        self.flow = flow
        self.lst = args["list"]

    def request(self):
        for item in self.lst:
            if self.url == item["host"]:
                # If the hostname matches a route, then change the url, scheme and port to the corresponding upstream address and break the loop
                self.flow.requests.url = item["upstream"]["url"]
                self.flow.requests.scheme = item["upstream"]["scheme"]
                self.flow.requests.port = item["upstream"]["port"]
                return self.flow, True
            # If the hostname does not match a route, return the flow and indicate that the route has not been found.
            return self.flow, False
