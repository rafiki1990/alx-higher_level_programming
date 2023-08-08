#include"lists.h"
#include <stdlib.h>

/**
 * insert_node - Inserts a number into a sorted singly linked list.
 * @head: Pointer to the head of the linked list.
 * @number: Number to be inserted.
 *
 * Return: The address of the new node, or NULL if it failed.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *current;

	/* Create a new node */
	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;

	/* If the list is empty or the number < the head, insert at the beginning */
	if (*head == NULL || number < (*head)->n)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}

	/* Traverse the list to find the appropriate position */
	current = *head;
	while (current->next != NULL && current->next->n < number)
		current = current->next;

	/* Insert the new node in the middle or at the end of the list */
	new_node->next = current->next;
	current->next = new_node;

	return (new_node);
}
