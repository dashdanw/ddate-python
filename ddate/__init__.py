from datetime import date as _date
import time as _time
from datetime import timedelta

__version__ = '1.0'


def _cmperror(x, y):
    raise TypeError("can't compare '%s' to '%s'" % (
        type(x).__name__, type(y).__name__))

class ddate:
    MIN_DAY = 1
    MAX_DAY = 73
    MIN_SEASON = 1
    MAX_SEASON = 5
    MIN_YEAR = -32768
    MAX_YEAR = 32768

    ORDINAL_PRE_AD_ONE = 425882

    def __init__(self, year, month, day):

        dd_data = self._makeday(month, day, year)

        self.__season = dd_data['season']
        self.__season_long = dd_data['season_long']
        self.__season_short = dd_data['season_short']

        self.__day = dd_data['day']
        self.__day_long = dd_data['day_long']
        self.__day_short = dd_data['day_short']

        self.__yday = dd_data['yday']
        self.__year = dd_data['year']

        self.__holyday = dd_data['holyday']
        self.__exclamation = dd_data['exclamation']

        self.__xday = dd_data['xday']

        self.__str = self._format()

    def _format(self, fmt=''):
        import cddate
        return cddate.format(fmt, self.__season, self.__day, self.__yday, self.__year)

    @staticmethod
    def _makeday(month, day, year):
        import cddate
        return cddate.makeday(month, day, year)

    @classmethod
    def fromtimestamp(cls, t):
        y, m, d, hh, mm, ss, weekday, jday, dst = _time.localtime(t)
        return cls(y, m, d)

    @classmethod
    def today(cls):
        t = _time.time()
        return cls.fromtimestamp(t)

    @classmethod
    def fromdatetime(cls, datetime):
        return cls(datetime.year, datetime.month, datetime.day)

    #TODO: fromordinal, toordinal
    # def fromordinal(cls, n):
    #     y, m, d = _ord2ymd(n)
    #     return cls(y, m, d)

    def toordinal(self):
        leap_days = int((self.__year + 2) / 4)
        return leap_days + (self.__year * 365) + self.__yday

    def ctime(self):
        "Return ctime() style string."
        weekday = self.toordinal() % 7 or 7
        return "%s %s %2d %02d:%02d:%02d %04d" % (
            self.__day_long,
            self.__season_long,
            self.__day,
            0, 0, 0,
            self.__year)

    def strftime(self):
        "Format using strftime()."
        return self.__str

    def weekday(self):
        return self.__day % 5

    def isoweekday(self):
        return (self.__day % 5) + 1

    def isocalendar(self):
        return (self.__year, self.__season, self.__day)

    def isoformat(self):
        args = self.isocalendar()
        return "{0}-{1}-{2}".format(*args)

    def timetuple(self):
        return (self.__year, self.__season, self.__day)

    #TODO: cleanup
    def replace(self, year=None, season=None, day=None):
        """Return a new date with new values for the specified fields."""
        if year is None:
            year = self.__year
        if season is None:
            season = self.__season
        if day is None:
            day = self.__day
        self._check_date_fields(year, season, day)
        return ddate(year, season, day)

    # type conversions

    def __str__(self):
        return self._format()

    def __repr__(self):
        "Convert to formal string, for repr()."
        return "%s(%d, %d, %d)" % (
            'ddate.' + self.__class__.__name__,
            self.__year,
            self.__season,
            self.__day
        )

    # Comparisons.

    def __eq__(self, other):
        if isinstance(other, self.__class__) or isinstance(other, _date):
            return self.__cmp(other) == 0
        elif hasattr(other, "timetuple"):
            return NotImplemented
        else:
            return False

    def __ne__(self, other):
        if isinstance(other, self.__class__) or isinstance(other, _date):
            return self.__cmp(other) != 0
        elif hasattr(other, "timetuple"):
            return NotImplemented
        else:
            return True

    def __le__(self, other):
        if isinstance(other, self.__class__) or isinstance(other, _date):
            return self.__cmp(other) <= 0
        elif hasattr(other, "timetuple"):
            return NotImplemented
        else:
            _cmperror(self, other)

    def __lt__(self, other):
        if isinstance(other, self.__class__) or isinstance(other, _date):
            return self.__cmp(other) < 0
        elif hasattr(other, "timetuple"):
            return NotImplemented
        else:
            _cmperror(self, other)

    def __ge__(self, other):
        if isinstance(other, self.__class__) or isinstance(other, _date):
            return self.__cmp(other) >= 0
        elif hasattr(other, "timetuple"):
            return NotImplemented
        else:
            _cmperror(self, other)

    def __gt__(self, other):
        if isinstance(other, self.__class__) or isinstance(other, _date):
            return self.__cmp(other) > 0
        elif hasattr(other, "timetuple"):
            return NotImplemented
        else:
            _cmperror(self, other)

    def __cmp(self, other):
        if isinstance(other, _date):
            other = ddate.fromdate(other)

        assert isinstance(other, ddate)

        ord1 = self.toordinal()
        ord2 = other.toordinal()

        return 1 if ord1 > ord2 else 0 if ord1 == ord2 else -1

    def __hash__(self):
        "Hash."
        return hash(self.__getstate())
    
    # Computations
    #TODO: fix this not working
    def __add__(self, other):
        "Add a date to a timedelta."
        if isinstance(other, timedelta):
            raise NotImplementedError
            year = self.__year
            season = self.__season
            day = self.__day + other.days
            self._check_date_fields(year, season, day)
            result = self.__class__(year, self.__season, self.__day)
            return result
        raise TypeError

    __radd__ = __add__

    def __sub__(self, other):
        """Subtract two dates, or a date and a timedelta."""
        if isinstance(other, timedelta):
            return self + timedelta(-other.days)
        if isinstance(other, self.__class__):
            days1 = self.toordinal()
            days2 = other.toordinal()
            return timedelta(days1 - days2)
        return NotImplemented

    @staticmethod
    def _check_date_fields(year, season, day):
        if not ddate.MIN_DAY <= day <= ddate.MAX_DAY:
            msg = 'day must be {}..{}'.format(ddate.MIN_DAY, ddate.MAX_DAY)
            raise ValueError(msg, day)
        if not ddate.MIN_SEASON <= season <= ddate.MAX_SEASON:
            msg = 'season must be {}..{}'.format(ddate.MIN_SEASON, ddate.MAX_SEASON)
            raise ValueError(msg, season)
        if not ddate.MIN_YEAR <= year <= ddate.MAX_YEAR:
            msg = 'season must be {}..{}'.format(ddate.MIN_YEAR, ddate.MAX_YEAR)
            raise ValueError(msg, year)

    # Pickle support.

    __safe_for_unpickling__ = True  # For Python 2.2

    def __getstate(self):
        yhi, ylo = divmod(self.__year, 256)
        return ("%c%c%c%c" % (yhi, ylo, self.__season, self.__day),)

    def __setstate(self, t):
        assert isinstance(t, tuple) and len(t) == 1
        string = t[0]
        assert len(string) == 4
        yhi, ylo, self.__season, self.__day = map(ord, string)
        self.__year = yhi * 256 + ylo

    def __reduce__(self):
        return (self.__class__, self.__getstate())