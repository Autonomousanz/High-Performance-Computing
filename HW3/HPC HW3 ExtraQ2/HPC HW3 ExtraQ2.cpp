// HPC HW3 ExtraQ2.cpp : This file contains the 'main' function. Program execution begins and ends there.
//
// C++ program to merge k sorted
// arrays of size n each
#include <iostream>
using namespace std;

// A Linked List node
struct Node {
    int data;
    Node* next;
};

/* Function to print nodes in
   a given linked list */
void printList(Node* node)
{
    while (node != NULL) {
        printf("%d ", node->data);
        node = node->next;
    }
}

// The main function that
// takes an array of lists
// arr[0..last] and generates
// the sorted output
Node* mergeKLists(Node* arr[], int last)
{

    // Traverse form second list to last
    for (int i = 1; i <= last; i++) {
        while (true) {
            // head of both the lists,
            // 0 and ith list.
            Node* head_0 = arr[0], * head_i = arr[i];

            // Break if list ended
            if (head_i == NULL)
                break;

            // Smaller than first element
            if (head_0->data >= head_i->data) {
                arr[i] = head_i->next;
                head_i->next = head_0;
                arr[0] = head_i;
            }
            else
                // Traverse the first list
                while (head_0->next != NULL) {
                    // Smaller than next element
                    if (head_0->next->data >= head_i->data) {
                        arr[i] = head_i->next;
                        head_i->next = head_0->next;
                        head_0->next = head_i;
                        break;
                    }
                    // go to next node
                    head_0 = head_0->next;

                    // if last node
                    if (head_0->next == NULL) {
                        arr[i] = head_i->next;
                        head_i->next = NULL;
                        head_0->next = head_i;
                        head_0->next->next = NULL;
                        break;
                    }
                }
        }
    }

    return arr[0];
}

// Utility function to create a new node.
Node* newNode(int data)
{
    struct Node* temp = new Node;
    temp->data = data;
    temp->next = NULL;
    return temp;
}

// Driver program to test
// above functions
int main()
{
    int a[12];
    cout<<"enter 12 numbers for 3 linked lists" << endl;
    for (int i = 0; i < 12; i++) {
        cin >> a[i];
    }
   
    // Number of linked lists
    int k = 3;

    // Number of elements in each list
    int n = 4;

    // an array of pointers storing the
    // head nodes of the linked lists
    Node* arr[3];

    arr[0] = newNode(a[0]);
    arr[0]->next = newNode(a[1]);
    arr[0]->next->next = newNode(a[2]);
    arr[0]->next->next->next = newNode(a[3]);

    arr[1] = newNode(a[4]);
    arr[1]->next = newNode(a[5]);
    arr[1]->next->next = newNode(a[6]);
    arr[1]->next->next->next = newNode(a[7]);

    arr[2] = newNode(a[8]);
    arr[2]->next = newNode(a[9]);
    arr[2]->next->next = newNode(a[10]);
    arr[2]->next->next->next = newNode(a[11]);

    // Merge all lists
    Node* head = mergeKLists(arr, k-1);

    printList(head);

    return 0;
}