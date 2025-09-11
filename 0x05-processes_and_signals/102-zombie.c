#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>

/**
 * infinite_while - a loop that runs till eternity
 *
 * Return: 0 for success
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - program that creates 5 zombie processes
 *
 * Return: 0 for success
 */
int main(void)
{
	int ch_pid = 0;
	pid_t pid;

	while (ch_pid < 5)
	{
		pid = fork();
		if (!pid)
			break;
		printf("Zombie process created, PID: ZOMBIE_PID %i\n", (int)pid);
		ch_pid++;
	}
	if (pid != 0)
		infinite_while();
	return (0);
}
