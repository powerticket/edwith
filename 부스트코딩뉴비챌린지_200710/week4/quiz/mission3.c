#include <stdio.h>

int main(void)
{
    int N = 4;
    int people[4] = {1, 2, 5, 10};
    int fast1 = 0;
    int fast2 = 1;
    int slow1 = N-1;
    int slow2 = N-2;
    int time_spend = 0;
    int go[100] = {0, };
    int back[100] = {0,};
    int i = 0;
    int j = 0;
    int l = N-2;

    while(1)
    {
        time_spend += people[fast2];
        go[i] = people[fast1];
        i++;
        go[i] = people[fast2];
        i++;
        time_spend += people[fast1];
        back[j] = people[fast1];
        j++;
        time_spend += people[slow1];
        go[i] = people[slow2];
        i++;
        go[i] = people[slow1];
        i++;
        time_spend += people[fast2];
        back[j] = people[fast2];
        j++;
        slow1 -= 2;
        slow2 -= 2;
        if(slow1 == fast2)
        {
            time_spend += people[fast2];
            go[i] = people[fast1];
            i++;
            go[i] = people[fast2];
            i++;
            break;
        }else if(slow2 == fast2)
        {
            time_spend += people[slow1];
            go[i] = people[slow2];
            i++;
            go[i] = people[slow1];
            time_spend += people[fast1];
            back[j] = people[fast1];
            j++;
            time_spend += people[fast2];
            go[i] = people[fast1];
            i++;
            go[i] = people[fast2];
            i++;
            l++;
            break;
        }
    }
    printf("%i\n", time_spend);
    for(int k = 0; k < l; k++)
    {
        printf("%i %i\n", go[2*k], go[2*k+1]);
        printf("%i\n", back[k]);
    }
    printf("%i %i\n", go[2*l], go[2*l+1]);
    return 0;
}
