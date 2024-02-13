#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly-linked list.
 * @head: A pointer the head of the linked list.
 * @number: The number to insert.
 * Return: pointer to new node else NULL.
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = malloc(sizeof(listint_t)), *__head = *head;
	listint_t *prev = __head;

	if (!new)
		return (NULL);
	new->n = number;

	if (!__head)
	{
		new->next = __head, *head = new;
		return (new);
	}
	while (__head->next)
	{
		if (__head->n < number)
			prev = __head, __head = __head->next;
		else
			break;
	}
	new->next = (__head->next) ? __head : NULL;
	if (prev == __head)
		*head = new;
	else
	{
		if (__head->next)
			prev->next = new;
		 else
			__head->next = new;
	}
	return (new);
}
