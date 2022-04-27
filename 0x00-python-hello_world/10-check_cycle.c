#include "lists.h"

/**
 * check_cycle - check list cycle
 * @list: linked list
 * Return: 0 or 1
 */

int check_cycle(listint_t *list)
{
	listint_t *twoJump;
	listint_t *singleJump;

	if (list == NULL)
		return (0);
	singleJump = list;
	twoJump = list->next;

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
