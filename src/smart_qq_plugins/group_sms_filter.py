import jieba
from smart_qq_bot.logger import logger
from smart_qq_bot.signals import on_group_message, on_bot_inited
from config.group_filter_config import group_filter_config
from models import sess, Message

@on_bot_inited("PluginManager")
def filter_init(bot):
    logger.info('[Group-Sms-Filter] plugin init')

@on_group_message(name="test")
def on_group_sms(msg, bot):
    import ipdb; ipdb.set_trace()  # XXX BREAKPOINT
    message = Message(sender_name=msg.src_sender_name, sender_id=None, group_name=None, group_id=None, content=msg.content)
    sess.add(message)
    logger.info('[New Group Message] name: %s, card: %s, content: %s' % (msg.src_sender_name, msg.src_sender_card, msg.content))
