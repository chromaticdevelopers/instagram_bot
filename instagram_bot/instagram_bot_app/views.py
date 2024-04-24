import json
import requests
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def instagram_webhook(request):
    if request.method == 'POST':
        try:
            print("getting call")
            # Parse JSON data from request body
            data = json.loads(request.body)
            msg = data['entry'][0]['messaging'][0]['message']['text']
            msg_id = data['entry'][0]['messaging'][0]['message']['mid']
            sender_id = data['entry'][0]['messaging'][0]['sender']['id']
            receiver_id = data['entry'][0]['messaging'][0]['recipient']['id']
            msg_data = {'msg': msg, 'msg_id': msg_id, 'sender_id': sender_id, 'receiver_id': receiver_id}
            print(msg_data)
            send_instgaram_message(message=msg_data['msg'], recipient_id=msg_data['sender_id'])
            
            return HttpResponse('Success', status=200)
        except Exception as e:
            print(e)
            return HttpResponse('Error', status=500)

    elif request.method == 'GET':
    
        hub_mode = request.GET.get('hub.mode')
        if hub_mode == 'subscribe':
            hub_challenge = request.GET.get('hub.challenge')
            hub_verify_token = request.GET.get('hub.verify_token')
            print("tokens",hub_challenge,hub_verify_token)
            return HttpResponse(hub_challenge)
        
def send_instgaram_message(message='', recipient_id=''):
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
                                    "text": "Please select an option:",
                                    "buttons": [
                                        {
                                            "type": "postback",
                                            "title": "Option 1",
                                            "payload": "OPTION_1"
                                        },
                                        {
                                            "type": "postback",
                                            "title": "Option 2",
                                            "payload": "OPTION_2"
                                        },
                                        {
                                            "type": "postback",
                                            "title": "Option 3",
                                            "payload": "OPTION_3"
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
    #     response_message = '''
    #         Hello welcome user,
    #         These are the options you can choose from:
    #         0 - Main menu
    #         1 - First option
    #         2 - Second option
    #         3 - Third option
    #     '''
    # elif message == '1':
    #     response_message = "Option 1"
    # elif message == '2':
    #     response_message = "Option 2"
    # elif message == '3':
    #     response_message = "Option 3"
    # else:
    #     response_message = "For the main menu, type 0"

    # msg_url = url + page_id + '/messages'
    # params = {
    #     'recipient': {'id': recipient_id},
    #     'message': {'text': response_message},
    #     'access_token': page_access_token
    # }
    # print(msg_url)
    # try:
    #     response = requests.post(url=msg_url, json=params)
    #     response_data = response.json()
    #     print(response_data)
    #     return JsonResponse(response_data)
    # except Exception as e:
    #     return JsonResponse({'error': str(e)}, status=500)