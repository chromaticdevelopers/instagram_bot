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
    

def send_Hair_Dressing( recipient_id=''):
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
                    "title": "Family",
                    "payload": "Family"
                },
                {
                    "type": "postback",
                    "title": "Double",
                    "payload": "Double"
                },
                {
                    "type": "postback",
                    "title": "Single",
                    "payload": "Single"
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
    
def make_up( recipient_id=''):
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
                    "title": "Full Layer Makeup",
                    "payload": "Full Layer Makeup"
                },
                {
                    "type": "postback",
                    "title": "Half Layer Makeup",
                    "payload": "Half Layer Makeup"
                },
                {
                    "type": "postback",
                    "title": "Family Makeup",
                    "payload": "Family Makeup"
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
    



def send_solobridal(message='', recipient_id=''):
    print("send", message, recipient_id)
    url = 'https://graph.facebook.com/v19.0/'
    page_id = '242698862268160'
    page_access_token = 'EAAGFqWZAZAX0QBOzd2762CYwTh6SZBBw3TZA5nOyPfPkT7RHThNWz5jQQ6HAvyrlRn5FGV79N8TJ4kjuZCFx5BARJHrpUtWmrLpBEx0Mz8tDZA96Kwolllc2cKhl4l4ikDJpsoRazmYqRpTZBk3MzbMbsGu1JGdsZCSEbBSbj53sLu4dUpdO7aL8bvBexH8xKXUS'

    response_message = {
        "attachment": {
            "type": "template",
            "payload": {
                "template_type": "generic",
                "elements": [
                    {
                        "title": "Zaras Full Bridal",
                        "image_url": "https://limelitesalonandspa.com/wp-content/uploads/2023/01/image.png",
                        "buttons": [
                            {
                                "type": "web_url",
                                "url": "www.fb.com",
                                "title": "Inquiry"
                            },
                            {
                                "type": "web_url",
                                "url": "www.fb.com",
                                "title": "Book Now"
                            }
                        ]
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
        print("res", response_data)
        return JsonResponse(response_data)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
    

def send_fullbridal(message='', recipient_id=''):
    print("send", message, recipient_id)
    url = 'https://graph.facebook.com/v19.0/'
    page_id = '242698862268160'
    page_access_token = 'EAAGFqWZAZAX0QBOzd2762CYwTh6SZBBw3TZA5nOyPfPkT7RHThNWz5jQQ6HAvyrlRn5FGV79N8TJ4kjuZCFx5BARJHrpUtWmrLpBEx0Mz8tDZA96Kwolllc2cKhl4l4ikDJpsoRazmYqRpTZBk3MzbMbsGu1JGdsZCSEbBSbj53sLu4dUpdO7aL8bvBexH8xKXUS'

    response_message = {
        "attachment": {
            "type": "template",
            "payload": {
                "template_type": "generic",
                "elements": [
                    {
                        "title": "Zaras Bridal- Family",
                        "image_url": "https://5.imimg.com/data5/SELLER/Default/2020/12/DU/SO/NH/2713142/best-family-makeup-service-in-gurgaon-500x500.jpg",
                        "buttons": [
                            {
                                "type": "web_url",
                                "url": "www.fb.com",
                                "title": "Inquiry"
                            },
                            {
                                "type": "web_url",
                                "url": "www.fb.com",
                                "title": "Book Now"
                            }
                        ]
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
        print("res", response_data)
        return JsonResponse(response_data)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
    
def CoupleBridal(message='', recipient_id=''):
    print("send", message, recipient_id)
    url = 'https://graph.facebook.com/v19.0/'
    page_id = '242698862268160'
    page_access_token = 'EAAGFqWZAZAX0QBOzd2762CYwTh6SZBBw3TZA5nOyPfPkT7RHThNWz5jQQ6HAvyrlRn5FGV79N8TJ4kjuZCFx5BARJHrpUtWmrLpBEx0Mz8tDZA96Kwolllc2cKhl4l4ikDJpsoRazmYqRpTZBk3MzbMbsGu1JGdsZCSEbBSbj53sLu4dUpdO7aL8bvBexH8xKXUS'

    response_message = {
        "attachment": {
            "type": "template",
            "payload": {
                "template_type": "generic",
                "elements": [
                    {
                        "title": "Zaras Bridal- Couple",
                        "image_url": "https://i.pinimg.com/564x/cf/ac/9f/cfac9f55dfa38070d6ba9154bfc9d5e5.jpg",
                        "buttons": [
                            {
                                "type": "web_url",
                                "url": "www.fb.com",
                                "title": "Inquiry"
                            },
                            {
                                "type": "web_url",
                                "url": "www.fb.com",
                                "title": "Book Now"
                            }
                        ]
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
        print("res", response_data)
        return JsonResponse(response_data)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
    

def CoupleBridal(message='', recipient_id=''):
    print("send", message, recipient_id)
    url = 'https://graph.facebook.com/v19.0/'
    page_id = '242698862268160'
    page_access_token = 'EAAGFqWZAZAX0QBOzd2762CYwTh6SZBBw3TZA5nOyPfPkT7RHThNWz5jQQ6HAvyrlRn5FGV79N8TJ4kjuZCFx5BARJHrpUtWmrLpBEx0Mz8tDZA96Kwolllc2cKhl4l4ikDJpsoRazmYqRpTZBk3MzbMbsGu1JGdsZCSEbBSbj53sLu4dUpdO7aL8bvBexH8xKXUS'

    response_message = {
        "attachment": {
            "type": "template",
            "payload": {
                "template_type": "generic",
                "elements": [
                    {
                        "title": "Zaras Bridal- Couple",
                        "image_url": "https://i.pinimg.com/564x/cf/ac/9f/cfac9f55dfa38070d6ba9154bfc9d5e5.jpg",
                        "buttons": [
                            {
                                "type": "web_url",
                                "url": "www.fb.com",
                                "title": "Inquiry"
                            },
                            {
                                "type": "web_url",
                                "url": "www.fb.com",
                                "title": "Book Now"
                            }
                        ]
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
        print("res", response_data)
        return JsonResponse(response_data)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
    


def Hair_single(message='', recipient_id=''):
    print("send", message, recipient_id)
    url = 'https://graph.facebook.com/v19.0/'
    page_id = '242698862268160'
    page_access_token = 'EAAGFqWZAZAX0QBOzd2762CYwTh6SZBBw3TZA5nOyPfPkT7RHThNWz5jQQ6HAvyrlRn5FGV79N8TJ4kjuZCFx5BARJHrpUtWmrLpBEx0Mz8tDZA96Kwolllc2cKhl4l4ikDJpsoRazmYqRpTZBk3MzbMbsGu1JGdsZCSEbBSbj53sLu4dUpdO7aL8bvBexH8xKXUS'

    response_message = {
        "attachment": {
            "type": "template",
            "payload": {
                "template_type": "generic",
                "elements": [
                    {
                        "title": "Zaras Hair dressing- Single",
                        "image_url": "https://i.pinimg.com/564x/cf/ac/9f/cfac9f55dfa38070d6ba9154bfc9d5e5.jpg",
                        "buttons": [
                            {
                                "type": "web_url",
                                "url": "www.fb.com",
                                "title": "Inquiry"
                            },
                            {
                                "type": "web_url",
                                "url": "www.fb.com",
                                "title": "Book Now"
                            }
                        ]
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
        print("res", response_data)
        return JsonResponse(response_data)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
    



def Hair_double(message='', recipient_id=''):
    print("send", message, recipient_id)
    url = 'https://graph.facebook.com/v19.0/'
    page_id = '242698862268160'
    page_access_token = 'EAAGFqWZAZAX0QBOzd2762CYwTh6SZBBw3TZA5nOyPfPkT7RHThNWz5jQQ6HAvyrlRn5FGV79N8TJ4kjuZCFx5BARJHrpUtWmrLpBEx0Mz8tDZA96Kwolllc2cKhl4l4ikDJpsoRazmYqRpTZBk3MzbMbsGu1JGdsZCSEbBSbj53sLu4dUpdO7aL8bvBexH8xKXUS'

    response_message = {
        "attachment": {
            "type": "template",
            "payload": {
                "template_type": "generic",
                "elements": [
                    {
                        "title": "Zaras Hair dressing- double",
                        "image_url": "https://image.wedmegood.com/resized-nw/1300X/wp-content/uploads/2022/11/43420f5926a32ca23a11708589ab039a.jpg",
                        "buttons": [
                            {
                                "type": "web_url",
                                "url": "www.fb.com",
                                "title": "Inquiry"
                            },
                            {
                                "type": "web_url",
                                "url": "www.fb.com",
                                "title": "Book Now"
                            }
                        ]
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
        print("res", response_data)
        return JsonResponse(response_data)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
    


def Hair_group(message='', recipient_id=''):
    print("send", message, recipient_id)
    url = 'https://graph.facebook.com/v19.0/'
    page_id = '242698862268160'
    page_access_token = 'EAAGFqWZAZAX0QBOzd2762CYwTh6SZBBw3TZA5nOyPfPkT7RHThNWz5jQQ6HAvyrlRn5FGV79N8TJ4kjuZCFx5BARJHrpUtWmrLpBEx0Mz8tDZA96Kwolllc2cKhl4l4ikDJpsoRazmYqRpTZBk3MzbMbsGu1JGdsZCSEbBSbj53sLu4dUpdO7aL8bvBexH8xKXUS'

    response_message = {
        "attachment": {
            "type": "template",
            "payload": {
                "template_type": "generic",
                "elements": [
                    {
                        "title": "Zaras Hair dressing- group",
                        "image_url": "https://image.wedmegood.com/resized-nw/1300X/wp-content/uploads/2022/11/c1d47984ba1667723d18a28e5e30792d.jpg",
                        "buttons": [
                            {
                                "type": "web_url",
                                "url": "www.fb.com",
                                "title": "Inquiry"
                            },
                            {
                                "type": "web_url",
                                "url": "www.fb.com",
                                "title": "Book Now"
                            }
                        ]
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
        print("res", response_data)
        return JsonResponse(response_data)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
    



def makeup1(message='', recipient_id=''):
    print("send", message, recipient_id)
    url = 'https://graph.facebook.com/v19.0/'
    page_id = '242698862268160'
    page_access_token = 'EAAGFqWZAZAX0QBOzd2762CYwTh6SZBBw3TZA5nOyPfPkT7RHThNWz5jQQ6HAvyrlRn5FGV79N8TJ4kjuZCFx5BARJHrpUtWmrLpBEx0Mz8tDZA96Kwolllc2cKhl4l4ikDJpsoRazmYqRpTZBk3MzbMbsGu1JGdsZCSEbBSbj53sLu4dUpdO7aL8bvBexH8xKXUS'

    response_message = {
        "attachment": {
            "type": "template",
            "payload": {
                "template_type": "generic",
                "elements": [
                    {
                        "title": "Zaras Make over- Full layer",
                        "image_url": "https://i.pinimg.com/564x/9a/af/5f/9aaf5f6824ffdd8cc5c2a8bfd3db925a.jpg",
                        "buttons": [
                            {
                                "type": "web_url",
                                "url": "www.fb.com",
                                "title": "Inquiry"
                            },
                            {
                                "type": "web_url",
                                "url": "www.fb.com",
                                "title": "Book Now"
                            }
                        ]
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
        print("res", response_data)
        return JsonResponse(response_data)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
    


def makeup2(message='', recipient_id=''):
    print("send", message, recipient_id)
    url = 'https://graph.facebook.com/v19.0/'
    page_id = '242698862268160'
    page_access_token = 'EAAGFqWZAZAX0QBOzd2762CYwTh6SZBBw3TZA5nOyPfPkT7RHThNWz5jQQ6HAvyrlRn5FGV79N8TJ4kjuZCFx5BARJHrpUtWmrLpBEx0Mz8tDZA96Kwolllc2cKhl4l4ikDJpsoRazmYqRpTZBk3MzbMbsGu1JGdsZCSEbBSbj53sLu4dUpdO7aL8bvBexH8xKXUS'

    response_message = {
        "attachment": {
            "type": "template",
            "payload": {
                "template_type": "generic",
                "elements": [
                    {
                        "title": "Zaras Make over- Half layer",
                        "image_url": "https://www.tahaayurveda.com/service/image/3132cebae10f7910e9adcca064296209.webp",
                        "buttons": [
                            {
                                "type": "web_url",
                                "url": "www.fb.com",
                                "title": "Inquiry"
                            },
                            {
                                "type": "web_url",
                                "url": "www.fb.com",
                                "title": "Book Now"
                            }
                        ]
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
        print("res", response_data)
        return JsonResponse(response_data)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
    



def makeup3(message='', recipient_id=''):
    print("send", message, recipient_id)
    url = 'https://graph.facebook.com/v19.0/'
    page_id = '242698862268160'
    page_access_token = 'EAAGFqWZAZAX0QBOzd2762CYwTh6SZBBw3TZA5nOyPfPkT7RHThNWz5jQQ6HAvyrlRn5FGV79N8TJ4kjuZCFx5BARJHrpUtWmrLpBEx0Mz8tDZA96Kwolllc2cKhl4l4ikDJpsoRazmYqRpTZBk3MzbMbsGu1JGdsZCSEbBSbj53sLu4dUpdO7aL8bvBexH8xKXUS'

    response_message = {
        "attachment": {
            "type": "template",
            "payload": {
                "template_type": "generic",
                "elements": [
                    {
                        "title": "Zaras Make over- Group",
                        "image_url": "https://cdn0.weddingwire.in/article/7269/3_2/1280/jpg/9627-kerala-bridal-makeup-weva-photography-lead-image.webp",
                        "buttons": [
                            {
                                "type": "web_url",
                                "url": "www.fb.com",
                                "title": "Inquiry"
                            },
                            {
                                "type": "web_url",
                                "url": "www.fb.com",
                                "title": "Book Now"
                            }
                        ]
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
        print("res", response_data)
        return JsonResponse(response_data)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)