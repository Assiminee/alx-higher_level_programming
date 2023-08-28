#ifndef CP_H_INCLUDED
#define CP_H_INCLUDED

#include <Python.h>
#include <stdlib.h>
#include <stdio.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

#endif
