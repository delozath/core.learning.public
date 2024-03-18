#include <stdio.h>
#include <stdlib.h>

typedef struct complex{
  float re;
  float im;
} complex;

complex *captura_datos(int len);
void imprime_lista_complex(complex *C, int len);

void main(){
  int len=0;
  complex *C;
  printf("Ingresa el numero de complejos a agregar:  ");
  scanf("%d",&len);
  
  C = captura_datos(len);
  imprime_lista_complex(C,len);

}

complex *captura_datos(int len){
  complex *C = NULL;
  if (len>0){
    C = (complex*)malloc(len*sizeof(complex));
    printf("\nIngresa lista de numeros complejos en formato a,b:\n");
    for(int i=0; i<len; i++){
      printf("  x[%d]: ",i );
      scanf("%f,%f",&C[i].re, &C[i].im);
    }
  }
  return C;
}

void imprime_lista_complex(complex *C, int len){
  printf("\nLista de %d numeros complejos:\n",len);
  for(int i=0; i<len; i++){
    printf("  x[%d]: %5.2f%+5.2fi\n",i,C[i].re, C[i].im);
  }
}