#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: pointer to the head of the list
 * Return: 0 if there is no cycle, 1 if there is a cycle
*/
int check_cycle(listint_t *list)
{
	listint_t *temp = list;

	if (!list)
		return (0);
	while (temp)
	{
		if (temp->next == list)
			return (1);
		temp = temp->next;
	}
	return (0);
}
