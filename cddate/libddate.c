#include <Python.h>

#include "libddate.h"
#include "ddate.h"

PyObject * cddate_makeday(PyObject *self, PyObject *args)
{
    struct disc_time dd;

    int month, day, year;

    const char * dl;
    const char * ds;

    const char * sl;
    const char * ss;

    const char * hd;
    const char * ex;

    int xd;

    if (!PyArg_ParseTuple(args, "iii", &year, &month, &day))
        return NULL;

    dd = makeday(month, day, year);

    dl = day_long[dd.day % 5];
    ds = day_short[dd.day % 5];

    sl = season_long[dd.season];
    ss = season_short[dd.season];

    xd = xday_countdown(dd.yday, dd.year);

    srandom(time(NULL));

    if (dd.day == 4 || dd.day == 49)
        hd = holyday[dd.season][dd.day == 49];
    else
        hd = "";

    return Py_BuildValue(
        "{s:i, s:i, s:i, s:i, s:s, s:s, s:s, s:s, s:s, s:s, s:i}",
        "season", dd.season,
        "day", dd.day,
        "yday", dd.yday,
        "year", dd.year,
        "day_long", dl,
        "day_short", ds,
        "season_long", sl,
        "season_short", ss,
        "holyday", hd,
        "exclamation", ex,
        "xday", xd
    );
}

PyObject * cddate_format(PyObject *self, PyObject *args)
{
    const char *fmt;
	char *out = (char*) malloc (23 * 17);
	int season, day, yday ,year;
    struct disc_time dt;

    srandom(time(NULL));

    if (!PyArg_ParseTuple(args, "siiii", &fmt, &season, &day, &yday ,&year))
        return NULL;

	fmt = strlen(fmt) > 0 ? fmt : default_immediate_fmt;

    dt.season = season;
    dt.day = day,
    dt.yday = yday,
    dt.year = year,

	format(out, fmt, dt);

    return Py_BuildValue("s", out);
}

PyObject * cddate_getday(PyObject *self, PyObject *args)
{
    struct disc_time dd;

    int season, day, year;

    const char * dl;
    const char * ds;

    const char * sl;
    const char * ss;

    const char * hd;
    const char * ex;

    int xd;

    if (!PyArg_ParseTuple(args, "iii", &year, &season, &day))
        return NULL;

    dl = day_long[day % 5];
    ds = day_short[day % 5];

    sl = season_long[season];
    ss = season_short[season];



    xd = xday_countdown(yday, year);

    srandom(time(NULL));

    if (dd.day == 4 || dd.day == 49)
        hd = holyday[dd.season][dd.day == 49];
    else
        hd = "";

    return Py_BuildValue(
        "{s:i, s:i, s:i, s:i, s:s, s:s, s:s, s:s, s:s, s:s, s:i}",
        "season", dd.season,
        "day", dd.day,
        "yday", dd.yday,
        "year", dd.year,
        "day_long", dl,
        "day_short", ds,
        "season_long", sl,
        "season_short", ss,
        "holyday", hd,
        "exclamation", ex,
        "xday", xd
    );
}