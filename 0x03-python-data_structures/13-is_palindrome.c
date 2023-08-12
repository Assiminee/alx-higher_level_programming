#include "lists.h"

int is_palindrome(listint_t **head)
{
	listint_t *top = *head;
	listint_t *bot;
	listint_t *mid = *head;
	int count = num_ele(head);
	int half = count/2, cycle = count/2;
	int i;
	bool pal = false;

	if (count % 2 == 0)
		half--;
	for (i = 0; i < half; i++)
	       mid = mid -> next;
	while (cycle > 0)
	{
		bot = mid;
		for (i = 0; i < cycle; i++)
			bot = bot -> next;
		if (bot -> n == top -> n)
			pal = true;
		else
		{
			pal = false;
			break;
		}
		top = top -> next;
		cycle--;
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
