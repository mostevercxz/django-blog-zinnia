from xmlrpclib import ServerProxy

#client = ServerProxy("http://localhost:8080")
# xmlrpc may treat datetime type as xmlrpclib.Datetime
client = ServerProxy("http://localhost:8080", allow_none=True, use_datetime=True)
client.hello_func()
