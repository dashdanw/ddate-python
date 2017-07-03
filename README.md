# ddate-python
C bindings for native util-linux ddate.

Behavior of the class ddate.ddate emulates that of datetime.date.

Direct C bindings to format() can be found in the sub-package cddate.

## Usage
### Typical:
    In [1]: import ddate

    In [2]: dd = ddate.ddate.today()

    In [3]: dd
    Out[3]: ddate.ddate(3183, 2, 37)

    In [4]: str(dd)
    Out[4]: 'Today is Prickle-Prickle, the 38th day of Confusion in the YOLD 3183'

    In [5]: dd.ctime()
    Out[5]: 'Pungenday Confusion 37 00:00:00 3183'

    In [6]: dd.timetuple()
    Out[6]: (3183, 2, 37)

### Format Strings
This is based on the format rules in the ddate manpage (https://linux.die.net/man/1/ddate) similar to those found in time.strftime().
    In [1]: import ddate

    In [2]: dd = ddate.ddate.today()

    In [3]: dd.format.__doc__

    :param fmt: follows the string formatting rules detailed in the ddate manpage https://linux.die.net/man/1/ddate
    :type fmt: str
    :return: the string produced by the original fmt input
    :rtype: str

    In [4]: fmt_str = dd.format('Today is %{%A, the %e of %B%}, %Y. %N%nCelebrate %H')

    In [5]: print(fmt_str)
    Today is Prickle-Prickle, the 38th of Confusion, 3183.

### Comparison and Arithmetic Operators
    In [1]: import ddate

    In [2]: dd = ddate.ddate.today()

    In [3]: # linux epoch time:

    In [4]: dd2 = ddate.ddate.fromtimestamp(0)

    In [5]: dd > dd2
    Out[5]: True

    In [6]: dd < dd2
    Out[6]: False

    In [7]: dd - dd2
    Out[7]: datetime.timedelta(17350)

## Unimplemented
1. Implement timedelta addition/subtraction
1. Implement ddate.fromordinal()
1. Fix ddate.replace()
1. Build converstion from ddate.ddate to datetime.date