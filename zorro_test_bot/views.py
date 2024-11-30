from django.template import loader
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django_tgbot.types.update import Update

from .bot import bot
from .models import TOKEN_LEN

import logging
import random
import string


@csrf_exempt
def handle_bot_request(request):
    update = Update(request.body.decode("utf-8"))
    try:
        bot.handle_update(update)
    except Exception as e:
        if settings.DEBUG:
            raise e
        else:
            logging.exception(e)
    return HttpResponse("OK")


def poll_updates(request):
    count = bot.poll_updates_and_handle()
    return HttpResponse(f"Processed {count} update{'' if count == 1 else 's'}.")

def index(request):
    context =  {
        "token" : ''.join(random.choices(string.ascii_uppercase + string.digits, k = TOKEN_LEN)),
    }
    s = loader.render_to_string('index.html', context)
    return HttpResponse(s)
