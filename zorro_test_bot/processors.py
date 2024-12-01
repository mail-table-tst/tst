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
        user = User.objects.create_user(update.get_user().get_first_name(), "", t)
    except:
        pass

    bot.sendMessage(update.get_chat().get_id(), 'Token (' + t + ') for user: ' + update.get_user().get_first_name())
