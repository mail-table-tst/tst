import os

from django.conf import settings
from django.contrib.auth.models import User
from django_tgbot.decorators import processor
from django_tgbot.state_manager import message_types, update_types, state_types
from django_tgbot.types.update import Update
from .bot import state_manager
from .models import TelegramState, UserTelegram
from .bot import TelegramBot

@processor(state_manager,
           update_types=update_types.Message,
           message_types=message_types.Text,
           from_states=state_types.All)
def tst(bot: TelegramBot, update: Update, state: TelegramState):
    t = update.message.text[7:]
    o = UserTelegram(name = update.get_user().get_first_name(), token = t)
    o.save()

    try:
        user = User.objects.get(username = update.get_user().get_first_name())
        user.set_password(t)
        user.save()
    except:
        user = User.objects.create_user(update.get_user().get_first_name(), "", t, is_staff = True)
        user.save()

    host = settings.HOST_NAME

    s = """
      Login to <a href="%s/admin/">site</a>
      <b>user</b>: <i>%s</i>
      <b>password</b>: <i>%s</i>
      """ % (host, update.get_user().get_first_name(), t)

    bot.sendMessage(update.get_chat().get_id(),
      s,
      parse_mode = "HTML"
    )
