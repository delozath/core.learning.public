#include <stdio.h>

void fill_array(int x[], int N);
void display_array(int x[], int N);

void main(){
  int N, *px;
  //
  printf("\n\n Bloque 1\n");
  printf("N <- ");
  scanf("%d", &N);
  //
  int x[N];
  fill_array(x, N);
  display_array(x, N);
  //printf("x = %d, dir(x) = 0x%lx\n\n", x, (long int) px);
  getchar();
}
//
void fill_array(int x[], int N){
  for(int i=0; i<N; i++){
    printf("x[%d] = ", i);
    scanf("%d", &x[i]);
  }
}

void display_array(int x[], int N){
  printf("x = [");
  for(int i=0; i<N-1; i++)
    //printf("%d, ", x[i]);
    printf("%lx, ", (long int)&x[i]);
    //
    //printf("%d]\n", x[N-1]);
    printf("%lx]\n", (long int)&x[N-1]);
}