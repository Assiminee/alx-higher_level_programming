#include "lists.h"

int is_palindrome(listint_t **head)
{
	listint_t *slow, *fast;

	if (head == NULL || *head == NULL || (*head) -> next == NULL)
		return (1);
	fast = *head;
	slow = *head;
	while (fast != NULL && fast -> next != NULL)
	{
		fast = fast -> next -> next;
		slow = slow -> next;
	}
	if (fast != NULL && fast -> next == NULL)
		slow = slow -> next;
	slow = rev_list(&slow);
	fast = *head;
	while (slow -> next != NULL)
	{
		if (slow -> n != fast -> n)
			return (0);
		slow = slow -> next;
		fast = fast -> next;
	}
	return (1);
}

listint_t *rev_list(listint_t **mid)
{
	listint_t *prev = NULL, *cur = *mid, *next;

	while (cur != NULL)
	{
		next = cur -> next;
		cur -> next = prev;
		prev = cur;
		cur = next;
	}
	return (prev);
}
