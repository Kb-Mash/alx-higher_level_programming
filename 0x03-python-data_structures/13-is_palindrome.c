#include "lists.h"

/**
 * reverse_listint - reverses a listint_t linked list
 * @head: pointer pointing to the head pointer
 * Return:  pointer to the first node of the reversed list
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *ptr = NULL, *previous = NULL;

	if (head == NULL || *head == NULL)
	{
		return (NULL);
	}

	while (*head != NULL)
	{
		ptr = (*head)->next;
		(*head)->next = previous;
		previous = *head;
		*head = ptr;
	}

	*head = previous;

	return (*head);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the head node
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *current = NULL, *rev = NULL, *mid = NULL;
	size_t i = 0, len = 0;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	current = *head;
	while (current != NULL)
	{
		len++;
		current = current->next;
	}
	current = *head;
	while (i < (len / 2) - 1)
	{
		current = current->next;
		i++;
	}
	if ((len % 2) == 0 && current->n != current->next->n)
		return (0);
	current = current->next->next;
	rev = reverse_listint(&current);
	mid = rev;
	current = *head;
	while (rev != NULL)
	{
		if (current->n != rev->n)
			return (0);
		current = current->next;
		rev = rev->next;
	}
	reverse_listint(&mid);
	return (1);
}
