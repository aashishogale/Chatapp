import json
from urllib import parse

from channels import Group
from channels.sessions import channel_session
from channels.auth import channel_session_user, channel_session_user_from_http

@channel_session
@channel_session_user_from_http
def ws_add(message, room):
    query = parse.parse_qs(message['query_string'])
    if 'username' not in query:
        return
    Group('chat-%s' % room).add(message.reply_channel)
    message.channel_session['room'] = room
    message.channel_session['username'] = query['username'][0]
    print(message.channel_session['username'])

    # query = parse.parse_qs(message['query_string'])
    # if 'username' not in query:
    #     return
    # Group('chat-%s' % room).add(message.reply_channel)
    # message.reply_channel.send({'accept': True})
    # message.channel_session['room'] = room
    # print("hello")
   
    # message.channel_session['username'] = query['username'][0]
    


@channel_session
def ws_echo(message):
    data = json.loads(message['text'])
    print('room', data['username'])
    print("notfound", message.content['text'])
    # if 'username' not in message.channel_session:
    #     print("notfound", message.content['text'])
    #     return
    room = 'public' #message.channel_session['room']
    Group('chat-%s' % room).send({
        'text': json.dumps({
            'message': data['text'],
            'username': data['username']
        }),
    })