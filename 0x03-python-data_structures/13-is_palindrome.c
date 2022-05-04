#include "lists.h"

/**
 * is_palindrome - check if a list is palindrome
 * @head: head of the list
 * Return: 0 if is not palindrome or 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	int list_arr[50];
	int i = 0, j = 0;

	while(*head != NULL)
	{
		list_arr[i] = (*head)->n;
		i++;
		(*head) = (*head)->next;
	}

	for(j = 0; list_arr[j] != NULL; j++)
	{
		if list_arr[j] != list_arr[0 - j - 1]
		{
			return(0);
		}
	}
	return(1);


}
