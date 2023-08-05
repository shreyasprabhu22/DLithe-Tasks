#include <stdio.h>
#include <stdlib.h>

#define SIZE 100000

int stack1[SIZE], stack2[SIZE];
int top1 = -1, top2 = -1;

void enqueue(int value) {
    stack1[++top1] = value;
}

void dequeue() {
    if (top2 == -1) {
        while (top1 >= 0) {
            stack2[++top2] = stack1[top1--];
        }
    }
    if (top2 >= 0) {
        top2--;
    }
}

int front() {
    if (top2 == -1) {
        while (top1 >= 0) {
            stack2[++top2] = stack1[top1--];
        }
    }
    return stack2[top2];
}

int main() {
    int q, type, value;
    scanf("%d", &q);

    for (int i = 0; i < q; i++) {
        scanf("%d", &type);
        
        if (type == 1) {
            scanf("%d", &value);
            enqueue(value);
        } else if (type == 2) {
            dequeue();
        } else if (type == 3) {
            int front_value = front();
            printf("%d\n", front_value);
        }
    }

    return 0;
}
