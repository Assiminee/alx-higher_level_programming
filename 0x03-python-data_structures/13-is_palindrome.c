#include "lists.h"

int is_palindrome(listint_t **head)
{
	listint_t *slow, *fast, *rev_list;

	if (head == NULL || *head == NULL || (*head) -> next == NULL)
		return (1);
	slow = *head;
	fast = *head;
	while (fast != NULL && fast -> next != NULL)
	{
		slow = slow -> next;
		fast = fast -> next -> next;
	}
	fast = *head;
	slow = reverse_list(slow);
	rev_list = slow;
	while (rev_list != NULL)
	{
		if (rev_list -> n != fast -> n)
		{
			slow = reverse_list(slow);
			return (0);
		}
		fast = fast -> next;
		rev_list = rev_list -> next;
	}
	slow = reverse_list(slow);
	return (1);
}

listint_t *reverse_list(listint_t *mid)
{
	listint_t *prev = NULL, *next;

	while (mid != NULL)
	{
		next = mid -> next;
		mid -> next = prev;
		prev = mid;
		mid = next;
	}
	return (prev);
}
