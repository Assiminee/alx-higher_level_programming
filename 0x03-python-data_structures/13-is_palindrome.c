#include "lists.h"

int is_palindrome(listint_t **head)
{
	listint_t *slow, *fast, *prev = NULL, *next;

	if (head == NULL || *head == NULL || (*head) -> next == NULL)
		return (1);
	slow = *head;
	fast = *head;
	while (fast != NULL || fast -> next != NULL)
	{
		next = slow;
		slow -> next = prev;
		prev = slow -> next;
		slow = prev;
		fast = fast -> next -> next;
	}
	fast = *head;
	printf("\n\nslow:\n");
	print_listint(prev);
	printf("\n\nfast:\n");
	print_listint(fast);
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
