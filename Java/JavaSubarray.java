import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] data=new int[n];
        int total=0;
        for (int i=0; i<n; i++){
            data[i]=sc.nextInt();
            int s=data[i];
            if (s<0) total++;
            for (int j=i-1; j>=0; j--){
                s+=data[j];
                if (s<0) total++;
            }
        }
        System.out.println(total);
    }    
}
