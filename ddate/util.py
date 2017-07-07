_DY400 = 146097
_DY100 = 36524
_DYY4 = 1461


def _cmperror(x, y):
    raise TypeError("can't compare '%s' to '%s'" % (
        type(x).__name__, type(y).__name__))


def _ydy2ord(yday, year):
    y = year - 1
    offset_y = y + 2
    days_before_year = y * 365 + offset_y // 4 - offset_y // 100 + offset_y // 400
    return days_before_year + yday


def _ord2ymd(n):
    n -= 1

    n400, n = divmod(n, _DY400)

    year = n400 * 400 + 1

    n100, n = divmod(n, _DY100)
    n4, n = divmod(n, _DYY4)

    n1, n = divmod(n, 365)

    year += n100 * 100 + n4 * 4 + n1

    if n1 == 4 or n100 == 4:
        assert n == 0
        return year - 1, 5, 73

    is_leap = _is_leapyear(year)

    if is_leap:
        leaped = n-74

        if leaped < 1:
            return year, 1, n+1

        month, day = divmod(leaped, 73)
        month += 2

    else:
        month, day = divmod(n, 73)
        month += 1

    day += 1

    return year, month, day


def _get_yday(year, season, day):
    is_leapyear = _is_leapyear(year)
    days_before_season = (season - 1) * 73
    leap_day = 1 if is_leapyear and season != 1 else 0
    return day + days_before_season + leap_day


def _is_leapyear(year):
    offset_year = year + 2
    return (offset_year % 4) == 0