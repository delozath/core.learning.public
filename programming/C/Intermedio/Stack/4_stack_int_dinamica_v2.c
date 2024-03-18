#include <stdio.h>
#include <stdlib.h>
#include "stack_dynamic.h"

void main(){
  int value, i, stop;
  stack_int_node *stack = init_stack_int();
  
  pop_int_dn(&stack, &value);
  print_stack_int_dn(stack);
  
  for (i=0; i<5; i++){
    printf("\n\nIteracion %2d:\n", i);
    push_int_dn(&stack, i*i-3);
    print_stack_int_dn(stack);
  }
  
  i    = 0;
  stop = pop_int_dn(&stack, &value);
  while(stop){
    printf("\n\nIteracion %2d:\n", i);
    print_stack_int_dn(stack);
    printf("Pop value: %d\n", value);
    stop = pop_int_dn(&stack, &value);
    i++;
  }    
}