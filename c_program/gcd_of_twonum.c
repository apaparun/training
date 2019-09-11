#include <stdio.h>

int main(void) {
  int n1,n2;
  scanf("%d%d",&n1,&n2);
  n1=(n1>0) ? n1 : -n1;//to change negative num to positive
  n2=(n2>0) ? n2 : -n2;
  while(n1!=n2){
    if(n1>n2){
      n1-=n2;

    }
    else{
      n2-=n1;
    }
  }
  printf("%d",n1);
  return 0;
}
