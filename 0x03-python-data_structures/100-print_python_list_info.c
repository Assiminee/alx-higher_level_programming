#include <Python.h>
#include <stdio.h>
#include <stdlib.h>

void print_python_list_info(PyObject *p)
{
	Py_ssize_t obj_size = PyList_Size(p), i;
	char **types = malloc(obj_size * sizeof(char*));

	printf("[*] Size of the Python List = %ld\n", obj_size);
	for (i = 0; i < obj_size; i++)
	{
		types[i] = malloc(strlen(Py_TYPE(PyList_GetItem(p, i)) -> tp_name) + 1);
		strcpy(types[i], Py_TYPE(PyList_GetItem(p, i)) -> tp_name);
	}	
	printf("[*] Allocated = %d\n", PyList_GET_SIZE(p));
	for (i = 0; i < obj_size; i++)
		printf("Element %ld: %s\n", i, types[i]);
	for (i = 0; i < obj_size; i++)
		free(types[i]);
	free(types);
}
