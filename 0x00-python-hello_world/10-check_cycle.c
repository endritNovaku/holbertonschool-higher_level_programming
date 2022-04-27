#include "lists.h"

/**
 * check_cycle - check list cycle
 * @list: linked list
 * Return: 0 or 1
 */

int check_cycle(listint_t *list)
{
	if (list == NULL)
		return (0);

	listint_t *twoJump = list->next;
	listint_t *singleJump = list;

	while (twoJump != NULL && twoJump->next != NULL && singleJump != NULL)
	{
		if (twoJump == singleJump)
		{
			return (1);
		}
		twoJump = twoJump->next->next;
		singleJump = singleJump->next;
	}
	return (0);
}
