_DY400 = 146100
_DY100 = 36525
_DY4 = 1461


def _cmperror(x, y):
    raise TypeError("can't compare '%s' to '%s'" % (
        type(x).__name__, type(y).__name__))


def _ydy2ord(yday, year):
    y = year - 1
    Y400, y = divmod(y, 400)
    Y100, y = divmod(y, 100)
    Y4, Y1 = divmod(y, 4)
    days_before_year = Y400*_DY400 + Y100 * _DY100 + Y4 * _DY4 + Y1 * 365
    return days_before_year + yday


def _ord2ymd(n):
    n -= 1

    n400, n = divmod(n, _DY400)
    n100, n = divmod(n, _DY100)
    n4, n = divmod(n, _DY4)
    n1, n = divmod(n, 365)

    year = n400 * 400 + n100 * 100 + n4 * 4 + n1

    is_leap = n1 == 1
    past_leap = n1 > 1

    # case for leap day
    if is_leap and n == 73:
        month = 0
        day = 73
    # last day of every year post-leap-year
    elif past_leap and n == 0:
        year -= 1
        month = 4
        day = 72
    # every day after leap day
    elif (is_leap and n > 73) or past_leap:
        month, day = divmod(n-1, 73)
    #else compute normally
    else:
        month, day = divmod(n, 73)

    day += 1
    month += 1
    year += 1

    return year, month, day


def _get_yday(year, season, day):
    is_leapyear = _is_leapyear(year)
    days_before_season = (season - 1) * 73
    leap_day = 1 if is_leapyear and season != 1 else 0
    return day + days_before_season + leap_day


def _is_leapyear(year):
    offset_year = year + 2
    return (offset_year % 4) == 0
