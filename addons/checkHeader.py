class CheckHeader:
    def __init__(self, flow, args):
        self.allowlist = args["allowlist"]
        self.denylist = args["denylist"]
        self.header_name = args["header_name"]
        self.flow = flow


    def request(self):
        try:
            self.ua = flow.request.headers[self.header_name]
        except KeyError:
            self.ua = []
        if self.ua in self.denylist:
            return self.flow, False
        if self.ua in self.allowlist:
            return self.flow, True
        else:
            return self.flow, False
        if not self.allowlist:
            return self.flow, True
