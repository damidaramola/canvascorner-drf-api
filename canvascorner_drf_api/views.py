from rest_framework.decorators import api_view
from rest_framework.response import Response

"""create a root_route and return 
   a custom message
"""


@api_view()
def root_route(request):
    return Response({
        "message": "Welcome to my django rest framework API"
    })
