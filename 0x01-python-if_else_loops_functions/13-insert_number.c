#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current = *head;
	listint_t *temp;

	if (head == NULL || *head == NULL)
		return (NULL);

	if ((*head) -> next == NULL)
		return (add_nodeint_end(head, number));
	
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	
	new -> n = number;
	while (current)
	{
		if (number <= (current -> next) -> n)
		{
			temp = current -> next;
			current -> next = new;
			new -> next = temp;
			return (new);
		}
		current = current -> next;
	}
	return (NULL);
}
