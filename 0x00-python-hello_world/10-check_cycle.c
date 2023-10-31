#include "lists.h"
/**
 * check_cycle - prints all elements of a listint_t list
 * @listint_t: pointer to head of list
 * Return: int 
 */

int check_cycle(listint_t *list)
{
	unsigned int i, l;
	listint_t *curr, *suspect;

	for (i = 0, curr = list; curr->next; curr = curr->next, i++)
		for (l = 0, suspect = list; l < i; suspect = suspect->next, l++)
			if (suspect == curr)
				return (1);
	return (0);
}
