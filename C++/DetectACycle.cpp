bool has_cycle(Node* head) {
    if (head==NULL)
        return false;    
    
    Node *aux = head;
    Node *auxNext = head->next;
    while(aux!=auxNext){
        if (auxNext==NULL || auxNext->next==NULL)
            return false;
        
        aux=aux->next;
        auxNext=auxNext->next->next;
    }
    return true;
}
