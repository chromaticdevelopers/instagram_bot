from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from instagram_bot_app.models import Menu, OptionsMenu
from instagram_bot_app.serializers import MenuSerializer, OptionsMenuSerializer
import json
import requests
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from instagram_bot_app.models import UserStatus


class Instagram_hook(APIView):
    def post(self, request):
        if request.method == 'POST':
            try:
                print("getting call")
                # Parse JSON data from request body
                data = json.loads(request.body)
                print("data,data",data)
                entry = data.get('entry', [])
                for entry_item in entry:
                    messaging = entry_item.get('messaging', [])
                    for message_item in messaging:
                        sender_id = message_item['sender']['id']
                        if 'message' in message_item and 'text' in message_item['message']:
                            # If it's a normal message
                            msg = message_item['message']['text']
                            msg_id = message_item['message']['mid']
                            receiver_id = message_item['recipient']['id']
                            msg_data = {'msg': msg, 'msg_id': msg_id, 'sender_id': sender_id, 'receiver_id': receiver_id}
                            print("incoming", msg_data)
                            # Check if the sender is in the database
                            send_instgaram_message_start(message=msg_data['msg'], recipient_id=sender_id)
                        elif 'postback' in message_item:
                            # If it's a postback
                            payload = message_item['postback']['payload']
                            title = message_item['postback']['title']
                            print("postback", payload, title)
                            # Process the payload and send the appropriate response

                            if payload == 'Bridal':
                                # If it's a request for the main menu, send it
                                send_Bridal(recipient_id=sender_id)
                            elif payload == 'Hair Dressing':
                                # If it's an option, process it
                                send_Hair_Dressing(recipient_id=sender_id)

                            elif payload == 'Make up':
                                # If it's an option, process it
                                make_up(recipient_id=sender_id)
                            elif payload == "Family":
                                print("picking")
                                # If it's a request for the main menu, send it
                                Hair_group(recipient_id=sender_id)
                            elif payload == 'Double':
                                # If it's an option, process it
                                Hair_double(recipient_id=sender_id)

                            elif payload == 'Single':
                                # If it's an option, process it
                                Hair_single(recipient_id=sender_id)



                            elif payload == 'Full Bridal With Family':
                                # If it's a request for the main menu, send it
                                send_fullbridal(recipient_id=sender_id)
                            elif payload == 'Solo Bridal':
                                # If it's an option, process it
                                send_solobridal(recipient_id=sender_id)
                            elif payload == 'Couple':
                                # If it's an option, process it
                                CoupleBridal(recipient_id=sender_id) 

                            elif payload == 'Full Layer Makeup':
                                # If it's a request for the main menu, send it
                                makeup1(recipient_id=sender_id)
                            elif payload == 'Half Layer Makeup':
                                # If it's an option, process it
                                makeup2(recipient_id=sender_id)

                            elif payload == 'Family Makeup':
                                # If it's an option, process it
                                makeup3(recipient_id=sender_id) 
                                
                
                return HttpResponse('Success', status=200)
            except Exception as e:
                # Handle any exceptions
                print("Error:", str(e))
                return HttpResponse('Error', status=500)

        elif request.method == 'GET':
        
            hub_mode = request.GET.get('hub.mode')
            if hub_mode == 'subscribe':
                hub_challenge = request.GET.get('hub.challenge')
                hub_verify_token = request.GET.get('hub.verify_token')
                print("tokens",hub_challenge,hub_verify_token)
                return HttpResponse(hub_challenge)

