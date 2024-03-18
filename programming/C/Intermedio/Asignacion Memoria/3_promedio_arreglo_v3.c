#include <stdio.h>
#include <stdlib.h>
#include "arreglo.h"

void main(){
  int entero     = 0;
  int is_number  = 1;
  int *a_enteros;
  
  while(is_number){
    printf("\n\n==============================================\n"\
           "Ingresa el tamano del arreglo\no cualquier letra para terminar el programa:\t");
    is_number = scanf("%d",&entero);
    if ( (is_number>0) && (entero>0) ){
      a_enteros = (int*)malloc(entero * sizeof(int));
      llena_arreglo_int  (a_enteros,entero);
      imprime_arreglo_int(a_enteros,entero);
      printf("El promedio del arreglo es: %f\n\n", promedio_int(a_enteros,entero));
      free(a_enteros);
    }
  }
}