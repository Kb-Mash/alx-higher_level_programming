#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - Prints basic info about Python lists.
 * @p: A PyObject list.
 */
void print_python_list_info(PyObject *p)
{
	int i = 0;

	printf("[*] Size of the Python List = %ld\n", Py_SIZE(p));
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	while (i < Py_SIZE(p))
	{
		printf("Element %d: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
		i++;
	}
}
