#include "lists.h"

size_t print_dlistint(const dlistint_t *h)
{
	const dlistint_t *curr;
	size_t count = 0;

	if (h == NULL)
		return (0);
	curr = h;
	while (curr != NULL)
	{
		printf("%d\n", curr->n);
		count++;
		curr = curr->next;
	}
	return count;
}
