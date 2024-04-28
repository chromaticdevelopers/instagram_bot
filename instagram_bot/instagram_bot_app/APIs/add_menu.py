from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from instagram_bot_app.models import Menu
from instagram_bot_app.serializers import MenuSerializer, OptionsMenuSerializer


class MenuWithOptionsAPIView(APIView):
    def post(self, request):
        # Extract menu data from request
        menu_data = request.data.pop('menu', {})
        is_menu_empty = not Menu.objects.exists()
        # Set main_menu field in menu_data accordingly
        menu_data['main_menu'] = is_menu_empty
        if is_menu_empty:
            menu_data['successor_of'] = None
        elif not is_menu_empty and menu_data['successor_of'] == None :
            return Response({'error': 'provide successor of '}, status=status.HTTP_400_BAD_REQUEST)
        # Create menu serializer
        menu_serializer = MenuSerializer(data=menu_data)
        if menu_serializer.is_valid():
            # Save menu
            menu_instance = menu_serializer.save()
            # Extract options data from request
            options_data = request.data.pop('options', [])
            # Save options
            for option_data in options_data:
                option_data['menu'] = menu_instance.id  # Assign menu id to option
                option_serializer = OptionsMenuSerializer(data=option_data)
                if option_serializer.is_valid():
                    option_serializer.save()
                else:
                    # If option serializer is not valid, return error response
                    menu_instance.delete()  # Delete menu if options cannot be saved
                    return Response(option_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            # Return success response
            return Response({'message': 'Menu and options created successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response(menu_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
