#include <stdio.h>
#include <string.h>

#define NCAL 4

typedef struct estudiante{
  int   matricula           ;
  char  nombre[50]          ;
  char  status              ;
  float calificaciones[NCAL];
} estudiante;

void  pedir_datos (estudiante *registro);
float promedio    (float arreglo[]);
void  calcula_nota(float cal, char nota[]);
void  asigna_nota (estudiante registro);

void main() {
  estudiante e0;
  pedir_datos(&e0);
  asigna_nota(e0);
}

void pedir_datos(estudiante *registro){
  printf("Matricula : ");
  scanf("%d", &(registro->matricula));
  printf("Nombre : ");
  scanf("%s", registro->nombre);
  printf("Estatus: ");
  scanf(" %c", &(registro->status));
  printf("Calificaciones: \n");
  
  for(int i=0; i<NCAL; i++){
    printf("  Item[%d]: ", i);
    scanf("%f", &(registro->calificaciones)[i]);
  }
}

float promedio(float arreglo[]){
  float m = 0;
  
  for(int i=0; i<NCAL; i++){
    m += arreglo[i];
  }
  
  return m/NCAL;
}

void calcula_nota(float cal, char nota[]){
  if ( (cal>=6) && (cal<7.6) )
    strcpy(nota," S");
  else if ( (cal>=7.6) && (cal<9) )
    strcpy(nota," B");
  else if (cal>=9)
    strcpy(nota,"MB");
}

void asigna_nota(estudiante registro){
  float cal;
  char  nota[2] = "NA";
  //char  notas[4][2] = {"NA", " S", " B", "MB"};
  printf("\n\nRegistro alumno %d:\n"
         "  Nombre: %s\n"
         "  Estatus: %c\n", registro.matricula, registro.nombre, registro.status);
  cal  = promedio(registro.calificaciones);
  calcula_nota(cal, nota);
  printf("  Calificacion %2.1f, Nota: %s\n\n", cal, nota);
  
  getchar();
}