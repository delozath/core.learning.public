#include <stdio.h>
#include <stdlib.h>

typedef struct stack_int_node{
  int                   value;
  struct stack_int_node *next;
} stack_int_node;

stack_int_node* init_stack_int   ();
void            push_int_dn       (stack_int_node **top, int val);
int             pop_int_dn        (stack_int_node **top);
void            print_stack_int_dn(stack_int_node  *top);

void main(){
  int value;
  stack_int_node *stack = init_stack_int();
  
  push_int_dn(&stack, 6);
  push_int_dn(&stack,-5);
  push_int_dn(&stack, 0);
  push_int_dn(&stack,-1);
  
  print_stack_int_dn(stack);
  
  pop_int_dn(&stack);
  print_stack_int_dn(stack);
  
  pop_int_dn(&stack);
  pop_int_dn(&stack);
  print_stack_int_dn(stack);
  
  pop_int_dn(&stack);
  print_stack_int_dn(stack);
  
  pop_int_dn(&stack);
  print_stack_int_dn(stack);
}

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

int pop_int_dn(stack_int_node **top){
  int            value;
  stack_int_node *node;
  node  = *top;
  if (node->next!=NULL){
    value = node  ->value;
    *top  = (*top)->next;
    free(node);
  }
  else{
    printf("Stack overflow\n");
  }
  return value;
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