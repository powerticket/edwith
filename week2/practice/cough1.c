#include <stdio.h>

void cough(int);

int  main(void)
{
    // printf("cough\n");
    // printf("cough\n");
    // printf("cough\n");

    // for (int i = 0; i < 3; i++)
    // {
    //     cough(3);
    // }

    cough(3);


}

void cough(int n)
{
    for (int i = 0; i < n; i++)
    {
        printf("cough\n");
    }
    
}
