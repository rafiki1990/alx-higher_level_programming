#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to the head of the list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	/* Initialize two pointers: slow and fast */
	listint_t *slow, *fast;

	/* If the list is empty or has only one node, there can't be a cycle */
	if (list == NULL || list->next == NULL)
		return (0);

	/* Initialize slow & fast pointers to 1st and 2nd nodes, respectively */
	slow = list;
	fast = list->next;

	/* Iterate until the fast pointer reaches the end of the list */
	while (fast != NULL && fast->next != NULL)
	{
		/* If there is a cycle, the slow and fast pointers will eventually meet */
		if (slow == fast)
			return (1);

		/* Move the slow pointer one step at a time */
		slow = slow->next;

		/* Move the fast pointer two steps at a time */
		fast = fast->next->next;
	}

	/* If the loop completes without finding a cycle, return 0 */
	return (0);
}
