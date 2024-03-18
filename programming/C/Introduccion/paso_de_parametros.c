#include <stdio.h>

void param_valor_1(int x);
void param_valor_2(int x);
void param_valor_3(int x);

void param_ref_1(int *x);
void param_ref_2(int *y);
void param_ref_3(int *z);

void main(){
  int var;
  printf("var <- ");
  scanf("%d", &var);
  
  
  printf("\n\nBloque 1\n");
  printf(" init var: $(%ld) -> %3d\n\n", (long int)&var, var);
  param_valor_1(var);
  printf("\n fin var:  $(%ld) -> %3d\n", (long int)&var, var);
  getchar();getchar();
  
  printf("\n\nBloque 2\n");
  printf(" init var: $(%ld) -> %3d\n\n", (long int)&var, var);
  param_ref_1(&var);
  printf("\n fin var:  $(%ld) -> %3d\n", (long int)&var, var);
  
}

void param_valor_1(int x){
  printf("   param_valor_1\n");
  printf("\t   $(%ld) -> %3d\n", (long int)&x, x);
  param_valor_2(x);
}

void param_valor_2(int x){ //scope
  printf("   param_valor_2\n");
  printf("\t   $(%ld) -> %3d\n", (long int)&x, x);
  x = 200;
  param_valor_3(x);
}

void param_valor_3(int x){
  printf("   param_valor_3\n");
  printf("\t   $(%ld) -> %3d\n", (long int)&x, x);
}



void param_ref_1(int *x){
  printf("   param_ref_1\n");
  printf("\t   $(%ld) -> %3d\n", (long int)x, *x);
  param_ref_2(x);
}

void param_ref_2(int *y){
  int *x;
  x = y;
  printf("   param_ref_2\n");
  printf("\t   $(%ld) -> %3d\n", (long int)y, *y);
  printf("\t   $(%ld) -> %3d\n", (long int)x, *x);
  *x = 1024;
  param_ref_3(x);
}

void param_ref_3(int *z){
  printf("   param_ref_3\n");
  printf("\t   $(%ld) -> %3d\n", (long int)z, *z);
}
