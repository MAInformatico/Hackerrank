#include<bits/stdc++.h>

using namespace std;

class Node {
    public:
        int data;
        Node *left;
        Node *right;
        Node(int d) {
            data = d;
            left = NULL;
            right = NULL;
        }
};

class Solution {
    public:
  		Node* insert(Node* root, int data) {
            if(root == NULL) {
                return new Node(data);
            } else {
                Node* cur;
                if(data <= root->data) {
                    cur = insert(root->left, data);
                    root->left = cur;
                } else {
                    cur = insert(root->right, data);
                    root->right = cur;
               }

               return root;
           }
        }
        
    void topView(Node * root){
        Node *aux = NULL;
        if(root->left){
            aux= root->left->right;
            root->left->right = NULL;
            topView(root->left);
            root->left->right = tmp;
        }
        cout<<root->data<<" ";
        if(root->right){
            aux= root->right->left;
            root->right->left = NULL;
            topView(root->right);
            root->right->left = tmp;
        }
        return;
    }
    
}; //End of Solution

int main() {
  
    Solution myTree;
    Node* root = NULL;
    
    int t;
    int data;

    std::cin >> t;

    while(t-- > 0) {
        std::cin >> data;
        root = myTree.insert(root, data);
    }
  
	myTree.topView(root);
    return 0;
}
    
