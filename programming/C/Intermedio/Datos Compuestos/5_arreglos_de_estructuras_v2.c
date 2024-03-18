#include <stdio.h>
#include <stdlib.h>

typedef struct complex{
  float re;
  float im;
} complex;

typedef struct complex_list{
  complex *list;
  int     len;
} complex_list;

complex_list captura_datos(int len);
void         imprime_lista_complex(complex_list C);
complex      sum_complex(complex_list C);

void main(){
  int len=0;
  complex_list C;
  complex     sum;
  printf("Ingresa el numero de complejos a agregar:  ");
  scanf("%d",&len);
  
  C = captura_datos(len);
  imprime_lista_complex(C);
  sum = sum_complex(C);
  printf("\n  Suma: %5.2f%+5.2fi\n",sum.re,sum.im);
}

complex_list captura_datos(int len){
  complex_list C;
  complex      *c_list   = NULL;
  
  if (len>0){
    c_list = (complex*)malloc(len*sizeof(complex));
    printf("\nIngresa lista de numeros complejos en formato a,b:\n");
    for(int i=0; i<len; i++){
      printf("  x[%d]: ",i );
      scanf("%f,%f",&c_list[i].re, &c_list[i].im);
    }
  }
  C.list = c_list;
  C.len  = len;
  return C;
}

void imprime_lista_complex(complex_list C){
  printf("\nLista de %d numeros complejos:\n",C.len);
  for(int i=0; i<C.len; i++){
    printf("  x[%d]: %5.2f%+5.2fi\n",i,C.list[i].re, C.list[i].im);
  }
}

complex sum_complex(complex_list C){
  float re, im = 0;
  
  for(int i=0; i<C.len; i++){
    re += C.list[i].re;
    im += C.list[i].im;
  }
  
  complex sum = {.re=re, .im=im};
  return sum;
}