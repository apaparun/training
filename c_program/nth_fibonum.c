#include <stdio.h>

int main(void) {
  int n1=0,n2=1,n3=0,n,i;
  scanf("%d",&n);
  for(i=2;i<n;i++){
    n3=n1+n2;
    n1=n2;
    n2=n3;
    
  }
  if(n==1){
      printf("%d",n1);
    }
  else if(n==2){
    printf("%d",n2);

  }
  else{
    printf("%d",n3);
  }

    
  return 0;
}
