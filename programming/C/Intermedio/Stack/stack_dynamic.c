#include <stdio.h>
#include <stdlib.h>
#include "stack_dynamic.h"

stack_int_node* init_stack_int (){
  stack_int_node *stack = (stack_int_node*)malloc(sizeof(stack_int_node));
  
  stack->value = -1;
  stack->next  = NULL;
  return stack;
}

void  push_int_dn(stack_int_node **top, int val){
  stack_int_node *stack_new_node = (stack_int_node*)malloc(sizeof(stack_int_node));
  
  stack_new_node -> value = val;
  stack_new_node -> next  = *top;
  *top                    = stack_new_node;
}

int pop_int_dn(stack_int_node **top, int *val){
  int            success_pop = 1;
  stack_int_node *node;
  node  = *top;
  if (node->next!=NULL){
    *val = node  ->value;
    *top = (*top)->next;
    free(node);
  }
  else{
    printf("Stack overflow\n");
    success_pop = 0;
  }
  return success_pop;
}

void print_stack_int_dn(stack_int_node *top){
  stack_int_node *node;
    node = top;
    printf("\nStack:\n");
    while (node->next != NULL){ 
        printf("\n%3d", node->value);
        node = node->next;
    }
    printf("\nEnd...\n");
}