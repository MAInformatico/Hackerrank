import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner sc= new Scanner(System.in);
        int length=sc.nextInt();
        int v=0;
        int total=0;
        int[] data= new int[length];
        int f=sc.nextInt();
        total=f<0 ? 1:0;
        for(int i=1; i<length;i++){
            v=sc.nextInt();
            data[i]=data[i-1]+v;
            if(data[i]<0) total++;
            
            for(int j=0; j<i;j++){
                int val= data[i]-data[j];
                if(val<0) total++;
            }
        }
        System.out.println(total);
    }    
}
