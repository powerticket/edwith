#include <stdio.h>
int sort(int n, int *arr)
{
    for (int i = n-1; i >= 0; i--)
    {
        for (int j = i; j < n; j++)
        {
            if (*(arr+j) > *(arr+j+1))
            {
                int *temp = arr+j;
                *(arr+j) = *(arr+j+1);
                *(arr+j+1) = *temp;
            }
        }
    }
    return *arr;
}
int main() 
{ 
    int n = 7; 
    int arr[7] = {0, 25, 10, 17, 6, 12, 9}; 
    sort(n, arr);
    return 0; 
}