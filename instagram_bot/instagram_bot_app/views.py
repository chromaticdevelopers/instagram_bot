import json
import requests
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from instagram_bot_app.models import UserStatus


@csrf_exempt
def instagram_webhook(request):
    if request.method == 'POST':
        try:
            print("getting call")
            # Parse JSON data from request body
            data = json.loads(request.body)
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
                        elif payload.startswith('OPTION_'):
                            # If it's an option, process it
                            # process_option(payload, sender_id)
                            pass
            
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
        
def send_instgaram_message_start(message='', recipient_id=''):
    print("send",message,recipient_id)
    url = 'https://graph.facebook.com/v19.0/'
    page_id = '242698862268160'
    page_access_token = 'EAAGFqWZAZAX0QBOzd2762CYwTh6SZBBw3TZA5nOyPfPkT7RHThNWz5jQQ6HAvyrlRn5FGV79N8TJ4kjuZCFx5BARJHrpUtWmrLpBEx0Mz8tDZA96Kwolllc2cKhl4l4ikDJpsoRazmYqRpTZBk3MzbMbsGu1JGdsZCSEbBSbj53sLu4dUpdO7aL8bvBexH8xKXUS'

    if message == message:
        response_message = {
    "attachment": {
        "type": "template",
        "payload": {
            "template_type": "button",
            "text": "Welcome to Zara's Makeover. Please select an option:",
            "buttons": [
                {
                    "type": "postback",
                    "title": "Bridal",
                    "payload": "Bridal"
                },
                {
                    "type": "postback",
                    "title": "Hair Dressing",
                    "payload": "Hair Dressing"
                },
                {
                    "type": "postback",
                    "title": "Make up",
                    "payload": "Make up"
                }
            ]
        }
    }
}
    # Prepare the request data
    params = {
        'recipient': {'id': recipient_id},
        'message': response_message,
        'access_token': page_access_token
    }

    # Send the message
    msg_url = url + page_id + '/messages'
    try:
        response = requests.post(url=msg_url, json=params)
        response_data = response.json()
        print("res",response_data)
        return JsonResponse(response_data)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
    

def send_Bridal( recipient_id=''):
    print("send",recipient_id)
    url = 'https://graph.facebook.com/v19.0/'
    page_id = '242698862268160'
    page_access_token = 'EAAGFqWZAZAX0QBOzd2762CYwTh6SZBBw3TZA5nOyPfPkT7RHThNWz5jQQ6HAvyrlRn5FGV79N8TJ4kjuZCFx5BARJHrpUtWmrLpBEx0Mz8tDZA96Kwolllc2cKhl4l4ikDJpsoRazmYqRpTZBk3MzbMbsGu1JGdsZCSEbBSbj53sLu4dUpdO7aL8bvBexH8xKXUS'

    
    response_message = {
    "attachment": {
        "type": "template",
        "payload": {
            "template_type": "button",
            "text": "Please select an option:",
            "buttons": [
                {
                    "type": "postback",
                    "title": "Full Bridal With Family",
                    "payload": "Full Bridal With Family"
                },
                {
                    "type": "postback",
                    "title": "Solo Bridal",
                    "payload": "Solo Bridal"
                },
                {
                    "type": "postback",
                    "title": "Couple",
                    "payload": "Couple"
                }
            ]
        }
    }
    }
    # Prepare the request data
    params = {
        'recipient': {'id': recipient_id},
        'message': response_message,
        'access_token': page_access_token
    }

    # Send the message
    msg_url = url + page_id + '/messages'
    try:
        response = requests.post(url=msg_url, json=params)
        response_data = response.json()
        print("res",response_data)
        return JsonResponse(response_data)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)