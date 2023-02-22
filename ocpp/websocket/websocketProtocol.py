import websockets

class WebSocket:

    # default constructor
    def __init__(self,uri,subprotocols,ping_interval,ping_timeout):
        self.uri = uri
        self.subprotocols = subprotocols
        self.ping_interval = ping_interval
        self.ping_timeout = ping_timeout

    def connect(self):
        #returns WebSocketClientProtocol
        return websockets.connect(self.uri, subprotocols = self.subprotocols, ping_interval = self.ping_interval, ping_timeout = self.ping_timeout)

    def on_disconnect(self):
        #behaviour of disconnection
        print("disconnect")

    def on_recv(self,raw_msg):
        print(raw_msg[1])
        if(int(raw_msg[1]) == 2):
            print("Call")
        elif(int(raw_msg[1]) == 3):
            print("Result")
    
