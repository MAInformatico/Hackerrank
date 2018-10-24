import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {

        int d,n1,n2,q=0;
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        ArrayList[] list = new ArrayList[n];
        for(int i=0; i<n;i++){
            d=scan.nextInt();
            list[i]= new ArrayList<Integer>();
            for(int j=0;j<d;j++)  
                list[i].add(scan.nextInt()); 
        }
        q=scan.nextInt();
        for(int j=0;j<q;j++){
            n1=scan.nextInt();
            n2=scan.nextInt();
            try{
                System.out.println(list[n1-1].get(n2-1));
            } catch(Exception e){
                System.out.println("ERROR!");
            }
        }
        scan.close();
    }
}
