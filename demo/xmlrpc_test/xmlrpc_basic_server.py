from SimpleXMLRPCServer import SimpleXMLRPCServer
from SocketServer import ThreadingMixIn

def hello_func():
    print "hello world from the server"

# only can handle one request at one time
server=SimpleXMLRPCServer(("", 8080), allow_none=True)
server.register_function(hello_func)
server.serve_forever()

class ThreadXMLRPCServer(ThreadingMixIn, SimpleXMLRPCServer):
    pass

"""
# handle multiple requests at the same time
class ThreadXMLRPCServer(ThreadingMixIn, SimpleXMLRPCServer):
    def _marshaled_dispatch(self, data, dispatch_method = None):
        try:
            params, method = xmlrpclib.loads(data, use_datetime=True)

            # generate response
            if dispatch_method is not None:
                response = dispatch_method(method, params)
            else:
                response = self._dispatch(method, params)
            # wrap response in a singleton tuple
            response = (response,)
            response = xmlrpclib.dumps(response, methodresponse=1,
                    allow_none=self.allow_none, encoding=self.encoding)
        except Fault, fault:
            response = xmlrpclib.dumps(fault, allow_none=self.allow_none,
                    encoding=self.encoding)
        except:
            # report exception back to server
            exc_type, exc_value, exc_tb = sys.exc_info()
            response = xmlrpclib.dumps(
                    xmlrpclib.Fault(1, "%s:%s" % (exc_type, exc_value)),
                    encoding=self.encoding, allow_none=self.allow_none,
                    )

        return response

server=ThreadXMLRPCServer(("", 8080), allow_none=True)
server.register_function(hello_func)
server.serve_forever()
"""
