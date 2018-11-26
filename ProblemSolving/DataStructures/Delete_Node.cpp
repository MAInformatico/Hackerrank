Node* Delete(Node *head, int position)
{
    if (position == 0)
    {
        auto next = head->next;
        delete head;
        return next;
    }
    
    head->next = Delete(head->next, position - 1);
    return head;
}
