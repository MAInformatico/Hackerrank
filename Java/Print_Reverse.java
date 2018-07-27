void ReversePrint(Node head) {
if(head == null) return;

    ReversePrint(head.next);
    System.out.println(head.data);
}
