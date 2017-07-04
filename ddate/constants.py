import random

class CONSTANTS_META(type):
    def __getattr__(self, name):
        return dict(self._CONSTANTS)[name]

    def __getitem__(self, value):
        if isinstance(value, int):
            return self._CONSTANTS[value-1]
        else:
            return dict(self._CONSTANTS)[value]

    def __setattr__(self, key, value):
        raise AttributeError("Cannot edit day constants!")

    def __setitem__(self, key, value):
        raise KeyError("Cannot edit day constants!")



class DAYS(object):
    _CONSTANTS = (
        ("SM", "Sweetmorn"),
        ("BT", "Boomtime"),
        ("PD", "Pungenday"),
        ("PP", "Prickle-Prickle"),
        ("SO", "Setting Orange")
    )
    __metaclass__ = CONSTANTS_META


class SEASONS(object):
    _CONSTANTS = (
        ("Chs", "Chaos"),
        ("Dsc", "Discord"),
        ("Cfn", "Confusion"),
        ("Bcy", "Bureaucracy"),
        ("Afm", "The Aftermath"),
    )
    __metaclass__ = CONSTANTS_META


class HOLYDAYS(object):
    _CONSTANTS = (
        ("Mungday", "Chaoflux"),
        ("Mojoday", "Discoflux"),
        ("Syaday", "Confuflux"),
        ("Zaraday", "Bureflux"),
        ("Maladay", "Afflux")
    )
    __metaclass__ = CONSTANTS_META

class EXCLAMATION(object):
    _CONSTANTS = (
        "Hail Eris!",
        "All Hail Discordia!",
        "Kallisti!",
        "Fnord.",
        "Or not.",
        "Wibble.",
        "Pzat!",
        "P'tang!",
        "Frink!"
    )
    @staticmethod
    def random():
        random.choice(EXCLAMATION._CONSTANTS)


    #
#
# _DAY_CONSTANTS_DICT = {
#     1: {
#         'short': 'BT',
#         'long': 'Boomtime'
#     },
#     2: {
#         'short': 'BT',
#         'long': 'Boomtime'
#     },
#     3: {
#         'short': 'BT',
#         'long': 'Boomtime'
#     },
#     4: {
#         'short': 'BT',
#         'long': 'Boomtime'
#     },
#     5: {
#         'short': 'BT',
#         'long': 'Boomtime'
#     }
# }
#
#
# _SEASON_CONSTANTS_DICT = {
#     1: {
#         'short': 'Chs',
#         'long': 'Chaos',
#         'holydays': {
#             5: "Mungday",
#             50: "Chaoflux"
#         }
#     },
#     2: {
#         'short': 'Dsc',
#         'long': 'Discord',
#         'holydays': {
#             5: "Mojoday",
#             50: "Discoflux"
#         }
#     },
#     3: {
#         'short': 'Cfn',
#         'long': 'Confusion',
#         'holydays': {
#             5: "Syaday",
#             50: "Confuflux"
#         }
#     },
#     4: {
#         'short': 'Bcy',
#         'long': 'Bureaucracy',
#         'holydays': {
#             5: "Zaraday",
#             50: "Bureflux"
#         }
#
#     },
#     5: {
#         'short': 'Afm',
#         'long': 'The Aftermath',
#         'holydays': {
#             5: "Maladay",
#             50: "Afflux"
#         }
#     }
# }