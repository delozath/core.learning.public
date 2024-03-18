#include <stdio.h>
#include <stdlib.h>

void  llena_arreglo_int  (int arreglo[], int len);
void  imprime_arreglo_int(int arreglo[], int len);
float promedio           (int arreglo[], int len);

void main(){
  int entero     = 0;
  int is_number  = 1; // 000->Falso, 001, 010, 011, 100, 101, 110, 111 ->  True 
  int *a_enteros;
  
  while(is_number){
    printf("\n\n==============================================\n"\
           "Ingresa el tamano del arreglo\no cualquier letra para terminar el programa:\t");
    is_number = scanf("%d",&entero);
    if ( (is_number>0) && (entero>0) ){
      a_enteros = (int*)malloc(entero * sizeof(int));
      llena_arreglo_int  (a_enteros,entero);
      imprime_arreglo_int(a_enteros,entero);
      printf("El promedio del arreglo es: %f\n\n", promedio(a_enteros,entero));
      free(a_enteros);
    }
  }
}



void llena_arreglo_int(int arreglo[], int len){
  //int ent;
  
  for(int i=0; i<len; i++){
    printf("\nIngresa A[%d]: ",i);
    //scanf("%d",&ent);
    //arreglo[i] = ent;
    scanf("%d",&arreglo[i]);
  }
}

void imprime_arreglo_int(int arreglo[], int len){
  printf("\n\nArreglo: [");
  for(int i=0; i<len-1; i++){
    printf("%d, ",arreglo[i]);
  }
  printf("%d]\n\n",arreglo[len-1]);
}

float promedio(int arreglo[], int len){
  float m = 0;
  for(int i=0; i<len; i++)
    m += arreglo[i];
  
  return m/len;
}