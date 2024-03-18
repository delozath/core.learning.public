#include <stdio.h>
//#include <stdlib.h>

#define NCAL 4

typedef struct estudiante{
  int   matricula           ;
  char  nombre[50]          ;
  char  status              ;
  float calificaciones[NCAL];
} estudiante; //estudiante en lugar de scruct estudiante, 

void  pedir_datos(estudiante *registro);
float promedio   (float arreglo[]);
void  nota       (estudiante registro);

void main() {
  estudiante e0;// struct estudiante
  pedir_datos(&e0);
  nota(e0);
}

void pedir_datos(estudiante *registro){
  
  printf("Matricula : ");
  scanf("%d", &(registro->matricula));
  printf("Nombre : ");
  scanf(" %[^\n]", registro->nombre);
  printf("Estatus: ");
  scanf(" %c", &(registro->status));
  getchar();
  printf("Calificaciones: \n");
  
  for(int i=0; i<NCAL; i++){
    printf("  Item[%d]: ", i);
    scanf("%f", &(registro->calificaciones[i]));
  }
}

float promedio(float arreglo[]){
  float m = 0;
  
  for(int i=0; i<NCAL; i++){
    m += arreglo[i];
  }
  
  return m/NCAL;
}

void nota(estudiante registro){
  float cal;
  printf("\n\nRegistro alumno %d:\n"
         "  Nombre: %s\n"
         "  Estatus: %c\n", registro.matricula, registro.nombre, registro.status);
  cal = promedio(registro.calificaciones);
  printf("Calificacion %2.1f\n", cal );
  getchar();
}