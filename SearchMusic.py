"""
                          _
                         (_)
 _ __ ___   ___ _ __ ___  _ _ __ __  _____  ___
| '_ ` _ \ / _ \ '_ ` _ \| | '_ \\ \/ / _ \/ __|
| | | | | |  __/ | | | | | | | | |>  < (_) \__ \
|_| |_| |_|\___|_| |_| |_|_|_| |_/_/\_\___/|___/
"""

from .. import loader, utils

@loader.tds
class SearchMusic(loader.Module):
    """
    Модуль для поиска муызки
    """
    strings = {"name": "Search Music"}

    async def smcmd(self, message):
        """Используй: .sm {название песни}, чтобы найти музыку по названию."""
        args = utils.get_args_raw(message)
        reply = await message.get_reply_message()
        if not args:
            return await message.edit("<b>нет аргументов.</b>")
        try:
            await message.delete()
            music = await message.client.inline_query('TgSoundBot', args)
            await message.client.send_file(message.to_id, music[0].result.document,reply_to=reply.id if reply else None)
        except:
            return await message.client.send_message(message.chat_id,f"<b>Музыка с названием <code>{args}</code> не найдена.</b>\nпопробуй указать автора")
