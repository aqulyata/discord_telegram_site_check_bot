import time

from DiscordTelegramSiteCheckBot.DbManager import UrlsBdRepository
from DiscordTelegramSiteCheckBot.command.base.Command import Command
from DiscordTelegramSiteCheckBot.command.enums.SiteState import SiteState


class Add(Command):

    def __init__(self, url_repo: UrlsBdRepository, prefix) -> None:
        super().__init__()
        self.url_repo: UrlsBdRepository = url_repo
        self.prefix = prefix

    def execute(self, send_func, args: [str]):
        if len(args) == 1:
            url = args[0]
            if self.url_repo.check_and_recording_url_in_db(url, SiteState.UNDEFINDED.value, time.time()):
                send_func("```Добавлено!```")
            else:
                send_func("```Уже добавлено```")

        elif len(args) == 0:
            send_func('```Вы забыли указать параметр```')
        else:
            send_func('```Извините, вы указали лишний  параметр```')

    def get_name(self):
        return 'add'

    def get_help(self):
        return ("Add url\n" +
                "Usage: `" + self.prefix + self.get_name() + " <url>`")