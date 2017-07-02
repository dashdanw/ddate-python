#include <Python.h>

#include "libddate.h"
#include "ddate.h"

PyObject * ddate_now(PyObject *self)
{
    const char *ddate_str;
    time_t t = time(NULL);
    ddate_str = ddate(t);
    return Py_BuildValue("s", ddate_str);
}

PyObject * ddate_ddate(PyObject *self, PyObject *args)
{
    const char *ddate_str;
    time_t time;

    if (!PyArg_ParseTuple(args, "l", &time))
        return NULL;

    ddate_str = ddate(time);
    return Py_BuildValue("s", ddate_str);
}
