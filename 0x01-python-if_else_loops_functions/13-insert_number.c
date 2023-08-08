#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current = *head;
	listint_t *temp;

	if (head == NULL)
		return (NULL);

	if (*head == NULL || (*head) -> next == NULL)
		return (add_nodeint_end(head, number));
	
	if (number <= current -> n)
		return (add_node_beg(head, number));

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	
	new -> n = number;
	while (current -> next)
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
	return (add_nodeint_end(&current, number));
}

listint_t *add_node_beg(listint_t **head, int number)
{
	listint_t *new;

	if (head == NULL)
		return (NULL);

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new -> n = number;
	new -> next = *head;
	*head = new;
	return (new);
}	
