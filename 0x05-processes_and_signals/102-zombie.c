#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>

/**
 * main - a function that starts the program
 *
 * Return: int
 */
int main(void)
{
	int i;
	pid_t zombie;

	for (i = 0; i < 5; i++)
	{
		zombie = fork();
		if (!zombie)
			return (0);
		printf("Zombie process created, PID: %u\n", zombie);
	}
	while (1)
		sleep(1);

	return (0);
}
