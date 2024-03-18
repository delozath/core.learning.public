#ifndef STACK_DYNAMIC_H
#define STACK_DYNAMIC_H

typedef struct stack_int_node{
  int                   value;
  struct stack_int_node *next;
} stack_int_node;

stack_int_node* init_stack_int   ();
void            push_int_dn       (stack_int_node **top, int  val);
int             pop_int_dn        (stack_int_node **top, int *val);
void            print_stack_int_dn(stack_int_node  *top);

#endif