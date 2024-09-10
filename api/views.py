from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
def hello_world(request):
    """
    A simple API view that returns a JSON response."""
    return Response({"message": "Hello, World!"})
