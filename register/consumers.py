import json
import datetime
from urllib import parse
from django.utils import timezone
from channels import Group
from channels.sessions import channel_session
from channels.auth import channel_session_user, channel_session_user_from_http
from register.models import ChatMessages
@channel_session
@channel_session_user_from_http
def ws_add(message):
    # 
    # query = parse.parse_qs(message.content['query_string'])
    # print(message['query string'])
    # if 'username' not in query:
    #      return
   
    # Group('chat').add(message.reply_channel)
  
    # message.channel_session['room'] = room
    # message.channel_session['username'] = query['username'][0]
    # print("helloadd",message.channel_session['username'])
  
    message.reply_channel.send({"accept": True})
    # query = parse.parse_qs(message['query_string'])
    # if 'username' not in query:
    #     return
    Group('chat').add(message.reply_channel)
   
    # message.reply_channel.send({'accept': True})
    # message.channel_session['room'] = room
    # print("hello")
   
    # message.channel_session['username'] = query['username'][0]
    


@channel_session
def ws_echo(message):
    data = json.loads(message.content['text'])
    print('room', data['username'])
    print("notfound", message.content['text'])
    # if 'username' not in message.channel_session:
    #     print("notfound", message.content['text'])
    #     return
    message=ChatMessages(message=data['text'],name=data['username'])
    message.save()
    room = 'public' #message.channel_session['room']
    Group('chat').send({
        'text': json.dumps({
            'message': data['text'],
            'username': data['username'],
            'created': data['created']
        }),
    })