#include "/usr/include/python3.4/Python.h"
#include "/usr/include/python3.4/bytesobject.h"
#include <object.h>
#include <listobject.h>
#include <stdio.h>

/**
 * print_hexn - prints hex integer
 * @str: string
 * @n: int
 */

void print_hexn(const char *str, int n)
{
	int i = 0;

	for (; i < n - 1; i++)
		printf("%02x ", (unsigned char) str[i]);

	printf("%02x", str[i]);
}

/**
 * print_python_bytes - prints python bytes
 * @p: PyObject
 */

void print_python_bytes(PyObject *p)
{
	PyBytesObject *clone = (PyBytesObject *) p;
	int calc_bytes, clone_size = 0;

	printf("[.] bytes object info\n");
	if (PyBytes_Check(clone))
	{
		clone_size = PyBytes_Size(p);
		calc_bytes = clone_size + 1;

		if (calc_bytes >= 10)
			calc_bytes = 10;

		printf("  size: %d\n", clone_size);
		printf("  trying string: %s\n", clone->ob_sval);
		printf("  first %d bytes: ", calc_bytes);
		print_hexn(clone->ob_sval, calc_bytes);
		printf("\n");
	}
	else
	{
		printf("  [ERROR] Invalid Bytes Object\n");
	}
}

/**
 * print_python_list - prints info about python lists
 * @p: pointer, pyobject
 */
void print_python_list(PyObject *p)
{
	PyListObject *list;
	PyObject *item;
	Py_ssize_t index;

	list = (PylistListObject *) p;

	printf("[*] Python list info\n")
	printf("[*] Size of the Python List = %d\n", (int) Py_SIZE(list));
	printf("[*] Allocated = %d\n", (int) list->allocated);

	for (index = 0; index < Py_SIZE(list); index++)
	{
		item = PyList_GetItem(p, index);
		if (item != NULL)
			printf("Element %d: %s\n", (int) index, item->ob_type->tp_name);
	}
}
