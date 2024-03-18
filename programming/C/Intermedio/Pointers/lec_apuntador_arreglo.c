#include <stdio.h>

#define MAX (3)

void captura_arreglo_int(int arreglo[]);
void imprime_arreglo_int(int arreglo[]);

void captura_arreglo_int_v2  (int arreglo[]);
void imprime_arreglo_int_pint(int arreglo[]);

void captura_arreglo_float_v3  (double arreglo[]);
void imprime_arreglo_float_pint(double arreglo[]);

void main(){
  int   x[MAX];
  double y[MAX];

  printf("\n\n=========="
          " Version 1\n");
  captura_arreglo_int(x);
  imprime_arreglo_int(x);
  getchar();getchar();
  
  printf("\n\n=========="
          " Version 2\n");
  captura_arreglo_int_v2(x);
  imprime_arreglo_int   (x);
  getchar();getchar();
  
  imprime_arreglo_int_pint(x);
  
  printf("\n\n=========="
          " Version 3 floats\n");
  captura_arreglo_float_v3  (y);
  imprime_arreglo_float_pint(y);
}


void imprime_arreglo_int(int arreglo[]){
  printf("\n\nArreglo X\n");
  for(int i=0; i<MAX; i++){
    printf("X[%2d]: %3d\n",i,arreglo[i]);
  }  
}

void captura_arreglo_int(int arreglo[]){
  for(int i=0; i<MAX; i++){
    printf("X[%2d]: ", i);
    scanf("%d", &arreglo[i]);
  }
}


void captura_arreglo_int_v2(int arreglo[]){
  for(int i=0; i<MAX; i++){
    printf("X[%2d]: ", i);
    scanf("%d", (arreglo + i));
  }
}

void imprime_arreglo_int_pint(int arreglo[]){
  printf("\n\nArreglo X\n");
  for(int i=0; i<MAX; i++){
    printf("X[%2d]: 0x%lx,  0x%lx -> %d\n", i, (long int)(arreglo+i), (long int)(&arreglo[i]), arreglo[i]);
  }  
}



void captura_arreglo_float_v3(double arreglo[]){
  for(int i=0; i<MAX; i++){
    printf("X[%2d]: ", i);
    scanf("%lf", (arreglo + i));
  }
}

void imprime_arreglo_float_pint(double arreglo[]){
  printf("\n\nArreglo X\n");
  for(int i=0; i<MAX; i++){
    printf("X[%d]: 0x%lx,  0x%lx -> %2.3lf\n", i, (long int)(arreglo+i), (long int)(&arreglo[i]), arreglo[i]);
  }  
}