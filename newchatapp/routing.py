from channels.routing import route



def message_handler(message):
    print(message['text'])


channel_routing = [
    route('websocket.connect', 'register.consumers.ws_add', path=r'^/chat/$'),
    route("websocket.receive", 'register.consumers.ws_echo'),  # we register our message handler
]