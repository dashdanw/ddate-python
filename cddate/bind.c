#include "libddate.h"

char cddate_makeday_docs[] = "Convert gregorian day, month year to discordian date";
char cddate_format_docs[] = "Get convert month, day, year ints to formatted discordian date string.";

PyMethodDef cddate_funcs[] = {
	{
        "makeday",
        (PyCFunction)cddate_makeday,
        METH_VARARGS,
        cddate_makeday_docs
    },
    {
        "format",
        (PyCFunction)cddate_format,
        METH_VARARGS,
        cddate_format_docs
    },
	{
		NULL
	}
};

char cddate_mod_docs[] = "Convert standard dates to discordian dates.";
char cddate_mod_name[] = "cddate";

#if PY_MAJOR_VERSION >= 3

PyModuleDef cddate_mod = {
	PyModuleDef_HEAD_INIT,
	cddate_mod_name,
	cddate_mod_docs,
	-1,
	cddate_funcs,
	NULL,
	NULL,
	NULL,
	NULL
};

PyMODINIT_FUNC PyInit_cddate(void) {
	return PyModule_Create(&cddate_mod);
}

#else

void initcddate(void) {
	Py_InitModule3(cddate_mod_name, cddate_funcs, cddate_mod_docs);
}

#endif
