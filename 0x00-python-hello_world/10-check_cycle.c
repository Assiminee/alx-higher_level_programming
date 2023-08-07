#include "lists.h"

/**
 * check_cycle - checks if singly linked list has a cycle
 * @list: pointer to listint_t
 *
 * Return: 1 if list has a cycle, 0 if not
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	while (slow != NULL && fast != NULL)
	{
		slow = slow -> next;
		fast = fast -> next -> next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
