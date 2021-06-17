#include <stdio.h>
int main(void) {
        printf("+--------------------------+\n");
        printf("+   Wish List Forecaster   |\n");
        printf("+--------------------------+\n\n");

	float income;
    while(1){
        printf("Enter your monthly NET income: $");
        scanf("%f",&income);
        if(income<500){
            printf("ERROR: You must have a consistent monthly income of at least $500.00\n\n");
        }
        else if(income > 400000){
            printf("ERROR: Liar! I'll believe you if you enter a value no more than $400000.00\n\n");
        }
        else{
            break;
        }
    }
    printf("\n");
    int forecast;
    while(1){
        printf("How many wish list items do you want to forecast?:");
        scanf("%d",&forecast);
        if(forecast<1 || forecast >10){
            printf("ERROR: List is restricted to between 1 and 10 items.\n\n");
        }
        else{
            break;
        }
    }    
    printf("\n");
    float costs[forecast+1];
    int options[forecast+1];
    char financings[forecast+1];
    float total = 0.0;
    for(int i=1;i<=forecast;i++){
        printf("Item-%d Details:",i);
        while(1){
            printf("\n\tItem cost: $");
            scanf("%f",&costs[i]);
            if(costs[i]<100.00){
                printf("\t\tERROR: Cost must be at least $100.00");
            }        
            else{
                break;
            }
        }
        total += costs[i];
        

        while(1){
            printf("\tHow important is it to you? [1=must have, 2=important, 3=want]:");
            scanf("%d",&options[i]);
            if(options[i] < 1 || options[i] >3){
                printf("\t\tERROR: Value must be between 1 and 3\n");
            }
            else{
                break;
            }
        }
        char ch[1];
        while(1){
            printf("\tDoes this item have financing options? [y/n]: ");
            scanf("%s",ch);
            if(ch[0] == 'n' || ch[0] == 'y'){
                break;
            }
            else{
                printf("\t\tERROR: Must be a lowercase 'y' or 'n'\n");
            }
        }
        financings[i] = ch[0];
        printf("\n");
    }
    
    printf("Item Priority Financed       Cost\n");
    printf("---- -------- -------- -----------\n");
    for(int i=1;i<=forecast;i++){
        printf("%3d  %5d      %5c    %11.2lf\n",i,options[i],financings[i],costs[i]);
    }
    printf("---- -------- -------- -----------\n");
    printf("                       $%11.2lf\n\n", total);
    
	return 0;
}
