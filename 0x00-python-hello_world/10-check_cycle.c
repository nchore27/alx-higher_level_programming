#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle
 * @list: linked list
 * Return: 0 if cycle, 1 if no cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *last, *first;

	last = list;
	first = list;

	while (last && first)
	{
		if (first->next == NULL)
			return (0);
		last = last->next;
		first = first->next->next;
		if (last == first)
			return (1);
	}
	return (0);
}
