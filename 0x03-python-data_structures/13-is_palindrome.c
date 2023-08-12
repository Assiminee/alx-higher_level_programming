#include "lists.h"

int is_palindrome(listint_t **head)
{
	listint_t *top, *bot;
	int count, i;

	if (head == NULL || *head == NULL || (*head) -> next == NULL)
		return (1);
	top = *head;
	count = num_ele(head);
	while (count - 1 > 0)
	{
		bot = *head;
		for (i = 0; i < count - 1; i++)
			bot = bot -> next;
		if (bot -> n != top -> n)
			return (0);
		top = top -> next;
		count--;
	}
	return (1);
}

int num_ele(listint_t **head)
{
	listint_t *ptr;
	int count = 0;

	if (*head == NULL || head == NULL)
		return (0);
	ptr = *head;

	while (ptr != NULL)
	{
		count++;
		ptr = ptr -> next;
	}
	return (count);
}
