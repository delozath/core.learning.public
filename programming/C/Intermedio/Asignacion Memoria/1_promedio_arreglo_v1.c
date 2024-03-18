#include <stdio.h>

void  llena_arreglo_int  (int arreglo[], int len);
void  imprime_arreglo_int(int arreglo[], int len);
float promedio           (int arreglo[], int len);

void main(){
  int   entero;
  
  printf("Ingresa el tamano del arreglo:  ");
  scanf("%d",&entero);
  
  int a_enteros[entero];
  
  llena_arreglo_int  (a_enteros,entero);
  imprime_arreglo_int(a_enteros,entero);
  printf("El promedio del arreglo es: %f\n", promedio(a_enteros,entero));
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
  printf("%d]\n",arreglo[len-1]);
}

float promedio(int arreglo[], int len){
  float m = 0;
  for(int i=0; i<len; i++)
    m += arreglo[i];
  
  return m/len;
}