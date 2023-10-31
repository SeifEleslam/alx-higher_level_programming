#include "lists.h"
/**
 * check_cycle - prints all elements of a listint_t list
 * @list: pointer to head of list
 * Return: int
 */

int check_cycle(listint_t *list)
{
	unsigned int i, l;
	listint_t *suspect;

	
	for (i = 0; list && list->next; list = list->next, i++)
	{
		for (l = 0, suspect = list->next; l < i && suspect->next; suspect = suspect->next, l++)
			if (suspect == list)
				return (1);
		i += l - 1, list = suspect;
	}
	return (0);
}
