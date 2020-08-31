// 문제 3

 

// 모바일 프로그래밍을 배우고 프로그래머로 취업을 하려고 하고있습니다.

// 신장개업을 하는 식당의 어플리케이션을 개발해 달라는 업무가 들어왔습니다.

 

// 이 식당은 손님들의 편의를 위해 모바일앱을 통한 쿠폰이나 서비스를 제공하고자 합니다.

// 프로모션을 위해 오늘의 메뉴를 할인해서 판매하고 있습니다.

 

// 의뢰자는 음식점의 앱에 들어와서 요일을 입력하면 해당 요일의 메뉴를 출력해 달라고 요청을 했습니다.

// 요일을 입력했을 때 해당 요일의 메뉴를 출력해 주는 프로그램을 개발 해서 고객의 요구사항을 잘 구현해 주세요!

 

// 각 요일별 메뉴는 다음과 같습니다.

 

// 월요일 : 청국장

// 화요일 : 비빔밥

// 수요일 : 된장찌개

// 목요일 : 칼국수

// 금요일 : 냉면

// 토요일 : 소불고기

// 일요일 : 오삼불고기

 

// 출력 예시)

// 요일을 입력하세요: 화요일                                                                                               
// 화요일: 비빔밥
// 요일을 입력하세요: 화요일                                                                                              

// 화요일: 비빔밥

#include <stdio.h>
#include <cs50.h>
#include <string.h>


int main(void){    
    string day_input = get_string("요일을 입력하세요: ");
    if (strcmp(day_input, "월요일") == 0)
    {
        printf("청국장\n");

    }
    else if (strcmp(day_input, "화요일") == 0)
    {
        printf("비빔밥\n");
    }
    else if (strcmp(day_input, "수요일") == 0)
    {
        printf("된장찌개\n");
    }
    else if (strcmp(day_input, "목요일") == 0)
    {
        printf("칼국수\n");
    }
    else if (strcmp(day_input, "금요일") == 0)
    {
        printf("냉면\n");
    }
    else if (strcmp(day_input, "토요일") == 0)
    {
        printf("소불고기\n");
    }
    else if (strcmp(day_input, "일요일") == 0)
    {
        printf("오삼불고기\n");
    }
    
}