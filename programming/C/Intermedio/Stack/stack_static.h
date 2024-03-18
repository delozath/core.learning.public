#ifndef STACK_STATIC_H
#define STACK_STATIC_H

typedef struct stack_int{
  int top;
  int max;
  int *data;
} stack_int;

stack_int init_stack_int (int max);
int       pop_int        (stack_int *stack, int *val);
int       push_int       (stack_int *stack, int  val);
void      print_stack_int(stack_int  stack);

#endif