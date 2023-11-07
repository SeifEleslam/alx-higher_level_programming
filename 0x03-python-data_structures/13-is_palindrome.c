#include "lists.h"

/*
 * is_palindrome - check if list is plaindrome
 * @head: the head of the list
 * Return: 1 | 0
 */
int is_palindrome(listint_t **head)
{
    listint_t *curr, *new, *tmp;
    int len, i;

    new = NULL;
    if (*head == NULL)
        return (1);
    curr = *head;
    len = list_len(*head);
    if (!curr->next)
        return (1);
    for (i = 0; i < len / 2; i++, curr = curr->next)
        add_nodeint_start(&new, curr->n);
    if (len > 2 * (len / 2))
        curr = curr->next;
    tmp = new;
    for (i = (len / 2) - 1; i >= 0; i--, curr = curr->next, tmp = tmp->next)
    {
        if (tmp->n != curr->n)
        {
            free_listint(new);
            return (0);
        }
    }
    free_listint(new);
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
<<<<<<< HEAD

/*
 * add_nodeint_start - check if list is plaindrome
 * @head: the head of the list
 * @n: int
 * Return: nt
 */
listint_t *add_nodeint_start(listint_t **head, int n)
{
    listint_t *new;
    new = malloc(sizeof(listint_t));
    new->next = *head;
    new->n = n;
    *head = new;
    return (new);
}
=======
>>>>>>> b370010951ac6adb175420db24c92695ef0e9b5d
