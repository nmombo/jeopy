// Learning how to extend python with c++ functions
// tutorial from https://docs.python.org/2/extending/extending.html

// Inclue python API
#include <Python.h>
// Include standard headers that python commonly uses
#include <stdio.h>
#include <string.h>
#include <errno.h>
#include <stdlib.h>

// Write function to be called with the python expression spam.system(string)
static PyObject *
spam_system(PyObject *self, PyObject *args)
{
	// Set up variables
	const char *command;
	int sts;

	// Return NULL (the error indicator for functions returning object
	// pointers) if an error is detected in the argument list, relying on the
	// exception set by PyArg_ParseTuples(). Otherwise, the string value of
	// the argument has been copied to the local variable command. This is a
	// pointer asssignment and you are not supposed to modify the string to
	// which it points (so we made it constant).
	if(!PyArg_ParseTuple(args, "s", &command))
		return NULL;
	// Call to the Unix function system(), pssing it the string we just got
	// from PyArg_ParseTuple()
	sts = system(command);
	// Since we need to return the value of sts as a python object, we call
	// Py_BuildBValue(), which is something like the inverse of
	//PyArg_ParseTuple(); it takes a format string and an arbitrary number of
	// C values and returns a new python object. In this case, it will return
	// an integer object.
	return Py_Build_Value("i", sts);
}