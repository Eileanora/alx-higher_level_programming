#include "lists.h"
/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to head of list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
*/
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head;
	int arr[10000], i = 0;

	if (!head)
		return (1);
	while (fast && fast->next)
	{
		arr[i] = slow->n;
		slow = slow->next;
		fast = fast->next->next;
		i++;
	}
	if (fast)
		slow = slow->next;
	while (slow)
	{
		if (arr[i - 1] != slow->n)
			return (0);
		slow = slow->next;
		i--;
	}
	return (1);
}
