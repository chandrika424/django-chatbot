from django.shortcuts import render

# Create your views here.
#from django.shortcuts import render
from django.http import JsonResponse
#from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from chat.models import ChatMessage
from .chatbot import get_bot_response


def chat_page(request):
    return render(request, "chat.html")

@csrf_exempt
def chat_api(request):
    if request.method != "POST":
        return JsonResponse(
            {"error": "Only POST requests are allowed"},
            status=405
        )

    message = request.POST.get("message", "").strip()

    if not message:
        return JsonResponse(
            {"error": "Please enter a message"},
            status=400
        )

    response = get_bot_response(message)
    ChatMessage.objects.create(
        user=request.user if request.user.is_authenticated else None,
        message=message,
        response=response
    )

    return JsonResponse({
        "message": message,
        "response": response
    })