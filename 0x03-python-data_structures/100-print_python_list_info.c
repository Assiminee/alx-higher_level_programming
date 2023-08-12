#include <Python.h>
#include <stdio.h>
#include <stdlib.h>

void print_python_list_info(PyObject *p)
{
	Py_ssize_t obj_size, allocated = 0, i;

	if (PyList_CheckExact(p))
	{
		obj_size = PyList_Size(p);
		printf("[*] Size of the Python List = %ld", obj_size);
		for (i = 0; i < obj_size; i++)
			allocated += sizeof(PyList_GetItem(p, i));
		printf("[*] Allocated = %ld", allocated);
		for (i = 0; i < obj_size; i++)
			printf("Element %ld: %s\n", i, Py_TYPE(PyList_GetItem(p, i)) -> tp_name);
	}
}
