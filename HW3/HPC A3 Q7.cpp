#include<iostream>
#include <vector>
using namespace std;
#define bool int
class node
{
public:
    int data;
    node* left;
    node* right;
};

bool findPathSum(node* Node, int sum)
{
    bool answer = 0;
    int differenceSum = sum - Node->data;
    if (differenceSum == 0 && Node->left == NULL && Node->right == NULL)
        return 1;

    if (Node->left)
        answer = answer || findPathSum(Node->left, differenceSum);
    if (Node->right)
        answer = answer || findPathSum(Node->right, differenceSum);

    return answer;

}

node* createnode(int data)
{
    node* Node = new node();
    Node->data = data;
    Node->left = NULL;
    Node->right = NULL;

    return(Node);
}


int main()
{
    int sum = 0;
    cout << "Input the sum to be found in the tree : " << endl;
    cin >> sum;
    cout << "Given tree is \n \t5\n4\t 8\n11 13\t\t 4\n7 2\t\t1" << endl;
    node* root = createnode(5);
    root->left = createnode(4);
    root->right = createnode(8);
    root->left->left = createnode(11);
    root->right->left = createnode(13);
    root->right->right = createnode(4);
    root->left->left->left = createnode(7);
    root->left->left->right = createnode(2);
    root->right->left->right = createnode(1);
    if (findPathSum(root, sum))
        cout << "There is a root-to-leaf path with sum " << sum;
    else
        cout << "There is NO root-to-leaf path with sum " << sum;

    return 0;
}
