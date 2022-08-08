from enum import Enum


class StatusChoices(Enum):
    ERROR = 'error'
    SUCCESS = 'success'
    WAIT = 'wait'
    NOT_STARTED = 'not started'
    WARNING = 'warning'


class AvailableDrivers(Enum):
    CHROME_PATH = 'drivers/chromedriver.exe'
    FIREFOX_PATH = 'drivers/geckodriver.exe'


SEARCH_URL = 'https://www.google.com/search?q={0}&newwindow=1&tbm=lcl&sxsrf=AOaemvJF91rSXoO-Kt8Dcs2gkt9_JXLlCQ%3A1632305149583&ei=_f9KYayPI-KExc8PlcaGqA4&oq={0}&gs_l=psy-ab.3...5515.12119.0.12483.14.14.0.0.0.0.0.0..0.0....0...1c.1.64.psy-ab..14.0.0....0.zLZdDbmH5so#rlfi=hd:;'
PLACE_DETAIL_PAGE_URL = 'https://maps.google.com/?cid={0}'
