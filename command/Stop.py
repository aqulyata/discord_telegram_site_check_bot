from service.Checker import Checker
from service.DbManager import UrlsBdRepository
from command.base.Command import Command


class Stop(Command):
    def __init__(self, url_repo: UrlsBdRepository, checker: Checker, prefix: str) -> None:
        super().__init__()
        self.checker = checker
        self.url_repo: UrlsBdRepository = url_repo
        self.prefix = prefix

    def execute(self, send_func, split_msg):
        self.url_repo.changing_state(False)
        print('stopped')
        send_func('```Вы остановили процесс проверки!```')

    def get_name(self):
        return 'stop'

    def get_help(self):
        return ("Stop process of checking\n" +
                "Usage: `" + self.prefix + self.get_name() + "`")
