#include <stdio.h>
#include <stdlib.h>
#include "arreglo.h"

void llena_arreglo_int(int arreglo[], int len){
  int ent;
  
  for(int i=0; i<len; i++){
    printf("\nIngresa A[%d]: ",i);
    scanf("%d",&ent);
    arreglo[i] = ent;   
  }
}

void imprime_arreglo_int(int arreglo[], int len){
  printf("\n\nArreglo: [");
  for(int i=0; i<len-1; i++){
    printf("%d, ",arreglo[i]);
  }
  printf("%d]\n\n",arreglo[len-1]);
}

float promedio_int(int arreglo[], int len){
  float m = 0;
  for(int i=0; i<len; i++)
    m += arreglo[i];
  
  return m/len;
}