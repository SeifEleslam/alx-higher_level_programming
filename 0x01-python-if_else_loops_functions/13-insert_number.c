#include "lists.h"

/**
 * print_listint - prints all elements of a listint_t list
 * @head: pointer to head of list
 * @number: int
 * Return: new node address
 */
listint_t *insert_node(listint_t **head, int number)
{
    listint_t *new_node, *curr;

    if (!head)
        return (NULL);
    new_node = malloc(sizeof(listint_t *));
    if (new_node == NULL)
        return (NULL);
    new_node->n = number;
    if (new_node->n < (*head)->n)
    {
        new_node->next = *head, *head = new_node;
        return (new_node);
    }
    for (curr = *head; curr->next; curr = curr->next)
    {
        if (curr->next->n > new_node->n)
        {
            new_node->next = curr->next, curr->next = new_node;
            return (new_node);
        }
    }
    curr->next = new_node;
    return (new_node);
}