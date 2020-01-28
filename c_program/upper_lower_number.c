#include<stdio.h>
int main(){
  char ch;
  scanf("%c",&ch);
  if(ch>=65 && ch<=90){
    printf("Upper");
  }
  else if(ch>=97 && ch<=122){
    printf("lower");
  }
  else if(ch>=48 && ch<=57){
    printf("Number");
  }
  else{
    printf("symbol");
  }
  return 0;

}
