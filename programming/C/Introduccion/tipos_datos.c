#include <stdio.h>

void main(){
  int   entero     = 0;
  float real       = 0.0;
  char  letra      = '0';
  char  cadena[10] = "letras";
  
  printf("Ingresa un numero entero:\n");
  scanf("%d",&entero);
  
  printf("\nIngresa un numero real:\n");
  scanf("%f",&real);
  
  printf("\nIngresa una letra:\n");
  scanf(" %c",&letra);
  
  printf("\nIngresa una cadena de caracteres sin espacios:\n");
  scanf(" %s",cadena);
  
  printf("\n\nDatos leidos -> \n"\
         "  Entero:   %d\n"\
         "  Float:    %f\n"\
         "  Caracter: %c, cast: %d\n"\
         "  String:   %s\n" ,entero, real, letra, (int)letra, cadena);
  getchar();
  
}