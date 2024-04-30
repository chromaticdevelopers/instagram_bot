
from django.http import JsonResponse
import requests
from instagram_bot_app.models import Menu ,OptionsMenu


payload = 'b5043f48-0f51-461d-b839-a6dc5cdc72ea'
option = OptionsMenu.objects.get(payload='b5043f48-0f51-461d-b839-a6dc5cdc72ea')

def call_main_menu(message, recipient_id):
    print("inside function json")
    url = 'https://graph.facebook.com/v19.0/'
    page_id = '242698862268160'
    page_access_token = 'EAAGFqWZAZAX0QBO9NlxnDuZBmHrZBnYE1sG8Dm3JeyXZBaczVuXwjZCjtZC6YXpRYaQZBijwb9RZALJCSlmqANu4Hoq7Y0bu4zvuZBdDr0oBWcH5bnZAyDhx9UYQhTpZBI2ZB72ssTZCnFG9vax6ZCcZAyZCoKEyZCjyExtyZAREr3atZCBklveIxDZCPexRYyipSLYkwm4siqUKO'
    buttons = []
    main_menu = Menu.objects.get(main_menu=True)
    if main_menu:
        title=main_menu.title
        sub_title =main_menu.subtitle
        options = OptionsMenu.objects.filter(menu_id=main_menu.id)
        if options:
            print("optons",options)
            for option in options:
                button = {}
                if option.type == 'URL':
                    button['type'] = 'web_url'
                    button['url'] = str(option.payload)
                    button['title'] = option.title
                elif option.type == 'BUTTON':
                    button['type'] = 'postback'
                    button['payload'] = str(option.payload)
                    button['title'] = option.title
                buttons.append(button)
        if main_menu.image_url is not None:
            template_type= "generic"
        else:
            template_type="button"

        if template_type =='generic':
            response_message = {
                            "attachment": {
                                "type": "template",
                                "payload": {
                                "template_type": "generic",
                                "elements": [
                                    {
                                        "title": main_menu.title,
                                        "image_url": main_menu.image_url,
                                        "buttons": buttons
                                    }
                                ]
                            }
                        }
                    }
        params = {
            'recipient': {'id': recipient_id},
            'message': response_message,
            'access_token': page_access_token
        }

        print("data",response_message)
        # Send the message
        msg_url = url + page_id + '/messages'
        try:
            response = requests.post(url=msg_url, json=params)
            response_data = response.json()
            print("res", response_data)
            return JsonResponse(response_data)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
        


def postback_response(payload: str, title: str,recipient_id:str):
    option_menu = OptionsMenu.objects.get(payload=payload, title=title)
    url = 'https://graph.facebook.com/v19.0/'
    page_id = '242698862268160'
    page_access_token = 'EAAGFqWZAZAX0QBO9NlxnDuZBmHrZBnYE1sG8Dm3JeyXZBaczVuXwjZCjtZC6YXpRYaQZBijwb9RZALJCSlmqANu4Hoq7Y0bu4zvuZBdDr0oBWcH5bnZAyDhx9UYQhTpZBI2ZB72ssTZCnFG9vax6ZCcZAyZCoKEyZCjyExtyZAREr3atZCBklveIxDZCPexRYyipSLYkwm4siqUKO'
    buttons = []
    if option_menu:
        main_menu = Menu.objects.get(successor_of=option_menu)
        if main_menu:
            options = OptionsMenu.objects.filter(menu=main_menu)
            print("optons",options)
            for option in options:
                button = {}
                if option.type == 'URL':
                    button['type'] = 'web_url'
                    button['url'] = str(option.payload)
                    button['title'] = option.title
                elif option.type == 'BUTTON':
                    button['type'] = 'postback'
                    button['payload'] = str(option.payload)
                    button['title'] = option.title
                buttons.append(button)
            if main_menu.image_url is not None:
                template_type= "generic"
            else:
                template_type="button"

            if template_type =='generic':
                response_message = {
                                "attachment": {
                                    "type": "template",
                                    "payload": {
                                    "template_type": "generic",
                                    "elements": [
                                        {
                                            "title": main_menu.title,
                                            "image_url": main_menu.image_url,
                                            "buttons": buttons
                                        }
                                    ]
                                }
                            }
                        }
            params = {
                'recipient': {'id': recipient_id},
                'message': response_message,
                'access_token': page_access_token
            }

            print("data",response_message)
            # Send the message
            msg_url = url + page_id + '/messages'
            try:
                response = requests.post(url=msg_url, json=params)
                response_data = response.json()
                print("res", response_data)
                return JsonResponse(response_data)
            except Exception as e:
                return JsonResponse({'error': str(e)}, status=500)


            



    

    