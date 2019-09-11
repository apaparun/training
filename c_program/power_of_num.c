#include <stdio.h>
#include<math.h>
int main(void) {
  int num,power;
  scanf("%d%d",&num,&power);
  power=pow(num,power);
  printf("%d",power);
  return 0;
}
