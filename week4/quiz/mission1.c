#include <stdio.h>
#include <string.h>


int main(void)
{
    char input1[5] = "11132";
    char input2[5] = "21135";
    int correct[5] = {0, 0, 0, 0, 0};

    for (int i = 0; i < 5; i++)
    {
        for (int j = 0; j < 5; j++)
        {
            if (input1[i] == input2[j])
            {
                correct[i] = 1;
                input2[j] = 'a';
            }
        }
    }

    for (int i = 0; i < 5; i++)
    {
        if (correct[i] == 0)
        {
            printf("False\n");
            return 1;
        }
    }
    
    printf("True\n");
    return 0;
}