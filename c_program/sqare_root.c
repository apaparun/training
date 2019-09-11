#include <stdio.h>

int main(void) {
  float num,temp;
  float sqrt;
  scanf("%f",&num);
  sqrt=num/2;
  temp=0;
  while(sqrt!=temp){
    temp=sqrt;
    sqrt=(num/temp+temp)/2;

  }
  printf("%.2f",sqrt);
  return 0;
}
