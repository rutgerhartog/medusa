from mitmproxy import http
import addons
import yaml

# Load config file
with open('routes.yaml') as fp:
    routes = yaml.safe_load(fp.read())

# This line requires an explanation: the correct class is loaded by globals()[addon["name"]]. The parentheses contain the arguments of the module (i.e. the flow and the other arguments).
addons = [globals()[addon["name"]](flow, addon["args"]) for addon in route["addons"]]

#
# for route in routes:
#     if route["type"] == "http":
#         # Use the HTTPFlow if the route is an HTTP route
#         def request(flow: http.HTTPFlow) -> None:
#             for addon in route["addons"]:
#                 try:
#                     # Run the addon and note its result (True or False)
#                     cls = eval("addons.{0}".format(addon))
#                     flow, result = cls.Request(flow, addon["args"]).perform()
#                 except:
#                     # If the addon does not have a Request class configured, it is probably a Response-only addon. Therefore, we ignore it for now.
#                     pass
#                 if not result:
#                     try:
#                         # Note that the void host has to have its route configured!
#                         void = route["void"]
#                         flow.request.host = void["host"]
#                         flow.request.scheme = void["scheme"]
#                         flow.request.port = void["port"]
#                         flow.request.headers["Host"] = void["host"]
#                     except KeyError:
#                         # If there is no void configured and the request is unwanted, kill the flow.
#                         flow.kill()
#
#
#
#         def response(flow: http.HTTPFlow):
#             blabla
