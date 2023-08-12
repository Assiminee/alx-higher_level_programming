#include <Python.h>
#include <stdio.h>
#include <stdlib.h>

void print_python_list_info(PyObject *p)
{
	Py_ssize_t obj_size = PyList_Size(p), i;

	printf("[*] Size of the Python List = %ld\n", obj_size);
	printf("[*] Allocated = %ld\n", p -> allocated);
	for (i = 0; i < obj_size; i++)
		printf("Element %ld: %s\n", i, Py_TYPE(PyList_GetItem(p, i)) -> tp_name);
}
