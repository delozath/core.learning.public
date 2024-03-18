#include <stdio.h>

void main(){
  int x, *px;
  px = &x;
  //
  printf("\n\n Bloque 1\n");
  printf("x <- ");
  scanf("%d", &x);
  //
  printf("x = %d, dir(x) = 0x%lx\n\n", x, (long int) px);
  getchar();
}

