#include "stdio.h"
#include "stdlib.h"
#include "Python.h"

void print_python_list(PyObject *p)
{
	PyListObject *ListObj = (PyListObject *)p;
	Py_ssize_t i = 0;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", PyList_Size(p));
	printf("[*] Allocated = %ld\n", ListObj->allocated);
	while (i < 2)
	{
		printf("Element %ld: %s\n", i, ListObj->ob_item[i]->ob_type->tp_name);
		i++;
	}
}
