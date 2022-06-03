#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * frees - frees data
 * @data: firs intput to free
 * @dataReversed: second intput to free
 */
void frees(int *data, int *dataReversed)
{
	free(data);
	free(dataReversed);
}
/**
 * reverse - reverse a linked list
 *
 * @head: header of the lintked list
 * @listSize: Size of the linked list
 * @data: data to free if malloc fails
 *
 * Return: an array of ints reversed
 */
int *reverse(listint_t **head, int listSize, int *data)
{
	int *dataReversed = 0;

	listint_t *temp;

	temp = *head;

	dataReversed = (int *)calloc(listSize + 40, sizeof(int));
	if (!dataReversed)
	{
		free(data);
		return (NULL);
	}

	while (temp != NULL)
	{
		dataReversed[listSize] = temp->n;
		temp = temp->next;
		listSize--;
	}
	return (dataReversed);
}
/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: linked list
 *
 * Return: 0 if is not, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	int listSize = 0, i = 0;
	int *dataReversed = 0, *data = 0;

	listint_t *temp;

	if (head == NULL)
		return (1);

	temp = *head;
	while (temp != NULL)
	{
		temp = temp->next;
		listSize++;
	}
	data = (int *)calloc(listSize + 1, sizeof(int));
	if (!data)
		return (1);
	listSize--;
	temp = *head;
	while (temp != NULL)
	{
		data[i] = temp->n;
		temp = temp->next;
		i++;
	}
	dataReversed = reverse(head, listSize, data);
	data[i] = '\0', dataReversed[i] = '\0', i = 0;
	while (data[i] == dataReversed[i])
	{
		if (!data[i] || !dataReversed[i])
		{
			frees(data, dataReversed);
			return (1);
		}
		i++;
	}
	frees(data, dataReversed);
	return (0);
}
