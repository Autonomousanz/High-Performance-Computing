//question2
#include <iostream>
using namespace std;
struct Node {
	int data;
	struct Node* left;
	struct Node* right;
	Node(int value) {
		data = value;
		left = NULL;
		right = NULL;

	}
};
// Class-method definition
// Compute the "maxDepth" of a tree 
int maxDepth(Node* node){

    if (node == NULL)
        return 0;
    else
    {
        /* compute the depth of each subtree */
        int lDepth = maxDepth(node->left);
        int rDepth = maxDepth(node->right);

        /* use the larger one */
        if (lDepth > rDepth)
            return(lDepth + 1);
        else return(rDepth + 1);
    }
}

int main()
{
	struct Node* root = new Node(3);
	root->left = new Node(9);
	root->right = new Node(20);
	root->right->left = new Node(15);
	//root->right->right = new Node(7);
	cout << "Height of tree is " << maxDepth(root);
	return 0;
}