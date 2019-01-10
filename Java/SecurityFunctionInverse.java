import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        int[] Yvalues;
        Yvalues= new int[n];
        
        // INPUT
        for (int i = 0; i < n; i++)         
            Yvalues[i]=sc.nextInt();
        
        // BASIC SEARCH
        for (int i = 1; i <= n; i++) {
            for (int j = 0; j < n; j++) {
                if (Yvalues[j] == i)
                    System.out.println(j+1);
            }
        }    
    }
}
