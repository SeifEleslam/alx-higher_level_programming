#include "lists.h"
#include <stdio.h>

/*
 * is_palindrome - check if list is plaindrome
 * @head: the head of the list
 * Return: 1 | 0
 */
int is_palindrome(listint_t **head)
{
    listint_t *curr;
    int len, vals[1024], i;

    if (*head == NULL)
        return (1);
    curr = *head;
    len = list_len(*head);
    if (len == 1)
        return (1);
    // vals = malloc((len + 1) * sizeof(int *));
    for (i = 0; i < len / 2; i++, curr = curr->next)
        vals[i] = curr->n;
    if (len > 2 * (len / 2))
        curr = curr->next;
    for (i = (len / 2) - 1; i >= 0; i--, curr = curr->next)
    {
        if (vals[i] != curr->n)
        {
            // free(vals);
            return (0);
        }
    }
    // free(vals);
    return (1);
}

/*
 * list_len - check if list is plaindrome
 * @head: the head of the list
 * Return: nt
 */
int list_len(listint_t *head)
{
    int len;

    for (len = 0; head; len++)
        head = head->next;
    return len;
}