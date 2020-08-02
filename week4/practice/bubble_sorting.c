#include <stdio.h>


int main(void)
{
    int input_num[5] = {9, 4, 2, 3, 7};
    int temp = 0;
    for (int i = 0, n = 5; i < n; i++)
    {
        for (int j = 0; j < n - 1 - i; j++)
        {
            if (input_num[j] > input_num[j+1])
            {
                temp = input_num[j];
                input_num[j] = input_num[j+1];
                input_num[j+1] = temp;
            }
        }
    }
    for (int i = 0, n = 5; i < n; i++)
    {
        printf("%i\n", input_num[i]);
    }
    return 0;
}
