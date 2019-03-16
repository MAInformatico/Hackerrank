import java.io.*;
import java.util.*;
import java.lang.reflect.*;


class Singleton{
    private static Singleton sing;
    public static String str;
    private Singleton() {}
    public static Singleton getSingleInstance(){
        if (sing== null) {
            sing= new Singleton();
        }
    return sing;
    }
}
