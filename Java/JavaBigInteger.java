import java.io.*;
import java.util.*;
import java.math.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        BigInteger n= new BigInteger(scan.next());
        BigInteger m= new BigInteger(scan.next());
        BigInteger result;
        result=n.add(m);
        System.out.println(result);
        result=n.multiply(m);
        System.out.println(result);
    }
}
