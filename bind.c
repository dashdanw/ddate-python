#include "libddate.h"

char ddate_now_docs[] = "Get current time in discordian form.";
char ddate_ddate_docs[] = "Get time in discordian form.";

PyMethodDef ddate_funcs[] = {
	{
		"now",
		(PyCFunction)ddate_now,
		METH_NOARGS,
		ddate_now_docs
	},
	{
		"ddate",
		(PyCFunction)ddate_ddate,
		METH_VARARGS,
		ddate_now_docs
	},
	{
		NULL
	}
};

char ddate_mod_docs[] = "Convert standard dates to discordian dates.";
char ddate_mod_name[] = "ddate";

#if PY_MAJOR_VERSION >= 3

PyModuleDef ddate_mod = {
	PyModuleDef_HEAD_INIT,
	ddate_mod_name,
	ddate_mod_docs,
	-1,
	ddate_funcs,
	NULL,
	NULL,
	NULL,
	NULL
};

PyMODINIT_FUNC PyInit_ddate(void) {
	return PyModule_Create(&ddate_mod);
}

#else

void inithelloworld(void) {
	Py_InitModule3(ddate_mod_name, ddate_funcs, ddate_mod_docs);
}

#endif
