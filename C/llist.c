#include <stdio.h>
#include <stdlib.h>

typedef struct node {
    int value;
    struct node * next;
} node_t;

node_t *HEAD, *TAIL;
node_t headnode, tailnode;

void insert_first( node_t * nodep )
{
    nodep->next = HEAD->next;
    HEAD->next = nodep;
}

void insert_last( node_t * nodep )
{
    /* Look for tail */
    node_t * cur = HEAD;
    while (cur->next != TAIL) {
        cur = cur->next;
    }
    /* We're pointing to tail here. */
    cur->next = nodep;
    nodep->next = TAIL;
}

node_t * remove_node( int value )
{
    node_t * cur =  HEAD;
    node_t * found = NULL;
    while ((cur->next != TAIL) && (cur->next->value != value)) {
        cur = cur->next;
    }
    if (cur->next != TAIL) {
        // found the node: cur->next
        found = cur->next;
        cur->next = found->next;
    }
    return found;
}

void print_out_list()
{
    for (node_t * cur = HEAD->next; cur != TAIL; cur = cur->next) {
        printf("%d ", cur->value);
    }
    printf("\n");
}

void initialize()
{
    printf("Initializing.\n");
    HEAD = &headnode;
    TAIL = &tailnode;
    HEAD->next = TAIL;
    TAIL->next = TAIL;
}

node_t * new_node( int value )
{
    node_t *nodep = (node_t *) malloc(sizeof(node_t));
    nodep->value = value;
    return nodep;
}

int main()
{
    initialize();
    for (int num = 0; num < 10; num++) {
        // insert_first( new_node(num) );
        insert_last( new_node(num) );
    }
    print_out_list();
    printf("============================================================\n");
    for (int num = 9; num >= 0; num--) {
        remove_node(num);
        print_out_list();
    }
    return 0;
}
