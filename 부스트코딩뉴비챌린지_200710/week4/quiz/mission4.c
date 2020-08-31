#include <stdio.h>

int main(void){
    int N = 9, M = 8; // 방의 가로, 세로 길이
    int H[] = {7, 4, 2, 0, 0, 6, 0, 7, 0}; // 상자들이 쌓여있는 높이
    int max_distance = 0;
    for(int i = 0; i < N-1; i++)
    {
        int distance = 0;
        for(int j = i; j < N; j++)
        {
            if(H[i] > H[j]) // i번 째, 상자와 우측 상자들(낙하할 때, 밑에 깔리는 상자들)을 비교하여 높을 경우 낙하 거리 1 증가
            {
                distance++;
            }        
        }
        if(distance > max_distance)
        {
            max_distance = distance;
        }
    }
    printf("%i\n", max_distance); // 가장 큰 낙하거리 출력
    return 0;
}
