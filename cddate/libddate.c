#include <Python.h>

#include "libddate.h"
#include "ddate.h"

PyObject * cddate_makeday(PyObject *self, PyObject *args)
{
    struct disc_time dd;

    int month, day, year;

    if (!PyArg_ParseTuple(args, "iii", &year, &month, &day))
        return NULL;

    dd = makeday(month, day, year);

    return Py_BuildValue(
        "{s:i, s:i, s:i}",
        "season", dd.season+1,
        "day", dd.day+1,
        "year", dd.year
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

    dt.season = season-1;
    dt.day = day-1,
    dt.yday = yday-1,
    dt.year = year,

	format(out, fmt, dt);

    return Py_BuildValue("s", out);
}
