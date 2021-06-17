#include <stdio.h>
int main(void) {
    char ch[1];
    while(1){
        printf("enter char:");
        scanf("%s",ch);
        printf("%s\n",ch[0]);
    }    
	return 0;
}
