#include <stdio.h>

int main(void) {
  int sum=0,num;
  scanf("%d",&num);
  while(num !=0){
    sum=sum+ (num%10);
    num=num/10;
  }
  printf("%d",sum);
  return 0;
}
