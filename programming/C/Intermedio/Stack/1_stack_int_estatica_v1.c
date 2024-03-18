#include <stdio.h>
#include <stdlib.h>

#define STACK_LEN (8)

typedef struct stack_int{
  int top;
  int max;
  int *data;
} stack_int;

stack_int init_stack_int (int max);
int       pop_int        (stack_int *stack, int *val);
int       push_int       (stack_int *stack, int  val);
void      print_stack_int(stack_int  stack);

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

stack_int init_stack_int (int max){
  int *data;
  stack_int stack = {.max = max, .top = -1};
  data            = (int*)malloc(stack.max*sizeof(int));
  stack.data      = data;
  
  return stack;
}

int push_int(stack_int *stack, int val){
  int push_success = -1;
  
  if (stack->top < stack->max-1){
    stack->top++;
    stack->data[stack->top] = val;
    push_success = 1;
  }
  else{
    printf("\nError push: stack overflow\n");
  }
  
  return push_success;
}

int pop_int(stack_int *stack, int *val){
  int pop_success = -1;
  
  if (stack->top > -1){
    *val = stack->data[stack->top];
    stack->data[stack->top] = 0;
    stack->top--;
    pop_success = 1;
  }
  else{
    printf("\nError pop: stack empty\n");
  }
  
  return pop_success;
}

void print_stack_int(stack_int stack){
  int i = 0;
  
  printf("\n\nStack\n");
  for(i=stack.max-1; i>-1; i--){
    printf("Stack[%2d]: %4d\n", i, stack.data[i]);
  }
  printf("top(%d)/max(%d)\n",stack.top,stack.max-1);
}