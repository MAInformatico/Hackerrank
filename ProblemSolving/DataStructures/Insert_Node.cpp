Node* Insert(Node *head,int data){
    
    Node *temp=new Node();
    temp->data = data;
    temp->next = NULL;

    if(head == NULL) head = temp;
    
    else{
        Node *p;
        p = head;
        while(p->next != NULL)
            p = p->next;
            p->next = temp;
    }
    return(head);
}
