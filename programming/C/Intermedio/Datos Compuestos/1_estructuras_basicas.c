#include <stdio.h>
//#include <stdlib.h>

struct persona{
  int   id     ;
  char  inicial;
  int   edad;
  float estatura;
};

void pedir_datos   (char *inicial, int *edad, float *estatura);
void imprimir_datos(struct persona datos);

void main() {
  char    inicial;
  int     edad;
  float   estatura;
  
  //Registro Persona 1
  printf("\n\nRegistro de persona 1->\n");
  struct persona reg1;
  pedir_datos(&inicial, &edad, &estatura);
  reg1.id       = 1;
  reg1.inicial  = inicial;
  reg1.edad     = edad;
  reg1.estatura = estatura;
  imprimir_datos(reg1);
  
  
  //Registro Persona 2
  printf("\n\nRegistro de persona 2->\n");
  pedir_datos(&inicial, &edad, &estatura);
  struct persona reg2 = { 2        ,
                          inicial  ,
                          edad     ,
                          estatura  };
  imprimir_datos(reg2);
  
  
  //Registro Persona 3
  printf("\n\nRegistro de persona 3->\n");
  pedir_datos(&inicial, &edad, &estatura);
  struct persona reg3 = { .edad     = edad    ,
                          .inicial  = inicial ,
                          .estatura = estatura,
                          .id       = 3  };
  imprimir_datos(reg3);
  
}



void pedir_datos(char *inicial, int *edad, float *estatura){
  printf("Inicial (minusc) : ");
  scanf("\n%c", inicial);
  printf("Edad     (anios) : ");
  scanf("%d", edad);
  printf("Estatura (metros): ");
  scanf("%f", estatura);
}

void imprimir_datos(struct persona datos){
  printf("\n\nDatos almacenados Persona %d:\n"
         "  Inicial  (minusc): %c\n"
         "  Edad     (anios) : %d\n"
         "  Estatura (metros): %f\n", datos.id, datos.inicial, datos.edad, datos.estatura);
  getchar();
}