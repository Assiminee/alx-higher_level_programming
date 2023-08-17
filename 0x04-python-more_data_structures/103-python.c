#include "stdio.h"
#include "stdlib.h"
#include "Python.h"

void print_python_list(PyObject *p)
{
	PyListObject *iter = (PyListObject *)p -> ob_item;
	int i = 0;

	printf("[*] Python list info\n");
	while (iter != NULL)
	{
		printf("%d\n", i);
		iter++;
	}

}
