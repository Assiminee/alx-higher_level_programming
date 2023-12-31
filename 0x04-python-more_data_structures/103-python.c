#include <stdio.h>
#include <stdlib.h>
#include <Python.h>
#include <string.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

void print_python_list(PyObject *p)
{
	PyListObject *ListObj = (PyListObject *)p;
	Py_ssize_t i = 0;
	const char *element_type;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", PyList_Size(p));
	printf("[*] Allocated = %ld\n", ListObj->allocated);
	while (i < PyList_Size(p))
	{
		element_type = ListObj->ob_item[i]->ob_type->tp_name;
		printf("Element %ld: %s\n", i, element_type);
		if (strcmp(element_type, "bytes") == 0)
			print_python_bytes(ListObj->ob_item[i]);
		i++;
	}
}

void print_python_bytes(PyObject *p)
{
	PyBytesObject *BytesObj;
	Py_ssize_t ObjSize, i;

	printf("[.] bytes object info\n");
	if (!PyBytes_CheckExact(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	BytesObj = (PyBytesObject *)p;
	ObjSize = PyBytes_Size(p);

	printf("  size: %ld\n", ObjSize);
	printf("  trying string: %s\n", BytesObj->ob_sval);
	if (ObjSize >= 10)
		ObjSize = 10;
	else
		ObjSize++;
	printf("  first %ld bytes: ", ObjSize);
	for (i = 0; i < ObjSize; i++)
	{
		printf("%02x", (unsigned char)BytesObj->ob_sval[i]);
		if (i == ObjSize - 1)
			printf("\n");
		else
			printf(" ");
	}
}
