import java.io.*;
import java.util.*;
import java.util.Scanner;

public class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String str = scan.nextLine();
        scan.close();
        
        String rever = new StringBuilder(str).reverse().toString();
        System.out.println(str.equals(rever) ? "Yes" : "No");    }
}
