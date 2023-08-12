#include "lists.h"

int is_palindrome(listint_t **head)
{
	listint_t *top;
	int count, i, j;
	bool pal = false;
	int nums[1000];

	if (head == NULL || *head == NULL)
		return (1);
	top = *head;
	count = num_ele(head);
	if (count == 0 || count == 1)
		return (1);
	for (i = 0; i < count; i++)
	{
		nums[i] = top -> n;
		top = top -> next;
	}
	j = count - 1;
	for (i = 0; i < count; i++)
	{
		if (nums[i] == nums[j--])
			pal = true;
		else
		{
			pal = false;
			break;
		}
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
