#include "lists.h"

int is_palindrome(listint_t **head)
{
	listint_t *top, *bot;
	int count, i;
	bool pal = false;

	if (head == NULL || *head == NULL)
		return (1);
	top = *head;
	count = num_ele(head);
	if (count == 0 || count == 1)
		return (1);
	pal = false;

	while (count - 1 > 0)
	{
		bot = *head;
		for (i = 0; i < count - 1; i++)
			bot = bot -> next;
		if (bot -> n == top -> n)
			pal = true;
		else
		{
			pal = false;
			break;
		}
		top = top -> next;
		count--;
	}
	if (pal)
		return (1);
	return (0);
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
