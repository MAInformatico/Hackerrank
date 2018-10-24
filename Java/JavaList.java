import java.io.*;
import java.util.*;
import java.text.*;

public class Solution {

    public static void main(String[] args) {
        int n1,n2,q=0;
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        List<Integer> lista = new ArrayList<Integer>();
        for(int i=0; i<n;i++){
            lista.add(scan.nextInt());
        }
        q=scan.nextInt();
        String query="";        
        for(int j=0;j<q;j++){
            query=scan.next();
            if(query.equals("Insert")){
                n1=scan.nextInt();
                n2=scan.nextInt();
                lista.add(n1,n2);
            }
            if(query.equals("Delete")){
                n1=scan.nextInt();
                lista.remove(n1);
            }
        }
        scan.close();
        for(Object o : lista) {
            System.out.print(o.toString()+" ");
        }
    }
}
