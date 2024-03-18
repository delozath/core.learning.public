#include <stdio.h>
#include <stdlib.h>
#include "stack_static.h"

#define STACK_LEN (8)

void main(){
  int value;
  stack_int stack = init_stack_int(STACK_LEN);
  
  for(int i=0; i<STACK_LEN+2; i++){
    push_int(&stack, 1+i*i);
    print_stack_int(stack);
    printf("\npresiona enter para continuar\n");
    getchar();
  }
  
  for(int i=0; i<STACK_LEN+2; i++){
    pop_int(&stack, &value);
    printf("Valor estraido de la pila %d\n",value);
    print_stack_int(stack);
    printf("\npresiona enter para continuar\n");
    getchar();
  }
  
}
