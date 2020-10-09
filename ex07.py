#https://66lemon66.blogspot.com/2020/03/zerojudge-c295-apcs-2016-1029-2-c.html

#include <stdio.h>
#include <stdlib.h>

int group_max[30];

int main(void) {
    //init
    for(int i=0;i<30;i++) {
        group_max[i]=0;
    }
    //readin
    int n, m;
    scanf("%d %d", &n, &m);
    for(int i=0;i<n;i++) {
        for(int j=0;j<m;j++) {
            int input;
            scanf("%d", &input);
            if(input>group_max[i]) {
                group_max[i]=input;
            }
        }
    }
    //max_sum
    int sum=0;
    for(int i=0;i<n;i++) {
        sum+=group_max[i];
    }
    printf("%d\n", sum);
    //factors
    int in=0;
    for(int i=0;i<n;i++) {
        if(sum%group_max[i]==0) {
            in=1;
            printf("%d ", group_max[i]);
        }
    }
    //if empty
    if(!in) {
        printf("-1");
    }

    return 0;
}
