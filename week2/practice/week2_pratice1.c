#include <stdio.h>


int main()
{
    char answer;
    printf("What's your name?\n");
    scanf("%c", &answer);
    printf("My name is %c.\n", answer);
    return 0;
}