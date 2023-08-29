#include "cp.h"

/**
 * print_python_list - prints python list infomation
 * @p: PyObject
 *
 * Return: void
 */
void print_python_list(PyObject *p)
{
	PyListObject *list_obj;
	Py_ssize_t allocated;
	Py_ssize_t num_ele, i;
	const char *type;

	setbuf(stdout, NULL);

	printf("[*] Python list info\n");

	if (!PyList_CheckExact(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	list_obj = (PyListObject *)p;

	allocated = list_obj->allocated;

	num_ele = ((PyVarObject*)p)->ob_size;

	printf("[*] Size of the Python List = %ld\n", num_ele);
	printf("[*] Allocated = %ld\n", allocated);

	for (i = 0; i < num_ele; i++)
	{
		type = list_obj->ob_item[i]->ob_type->tp_name;
		printf("Element %ld: %s\n", i, type);
		if (strcmp(type, "bytes") == 0)
			print_python_bytes(list_obj->ob_item[i]);
		else if (strcmp(type, "float") == 0)
			print_python_float(list_obj->ob_item[i]);
	}
}

/**
 * print_python_bytes - prints python bytes information
 * @p: PyObject
 *
 * Return: void
 */
void print_python_bytes(PyObject *p)
{
	PyBytesObject *bytes_obj;
	Py_ssize_t i, obj_size;

	setbuf(stdout, NULL);

	printf("[.] bytes object info\n");
	if (!PyBytes_CheckExact(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	bytes_obj = (PyBytesObject *)p;
	obj_size = ((PyVarObject *)p)->ob_size;

	printf("  size: %lu\n", obj_size);
	printf("  trying string: %s\n", bytes_obj->ob_sval);

	if (obj_size >= 10)
		obj_size = 10;
	else
		obj_size++;
	printf("  first %ld bytes: ", obj_size);
	for (i = 0; i < obj_size; i++)
	{
		printf("%02x", (unsigned char)bytes_obj->ob_sval[i]);
		if (i == obj_size - 1)
			printf("\n");
		else
			printf(" ");
	}
}

/**
 * print_python_float - prints python float information
 * @p: PyObject
 *
 * Return: void
 */
void print_python_float(PyObject *p)
{
	double val = ((PyFloatObject *)p)->ob_fval;
	char *str_rep;

	setbuf(stdout, NULL);
	printf("[.] float object info\n");
	if (!PyFloat_CheckExact(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	str_rep = PyOS_double_to_string(val, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", str_rep);
}

