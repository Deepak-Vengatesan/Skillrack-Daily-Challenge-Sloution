package com.skillrack;
import java.util.*;

public class BasicCalculator{
   public static int addition(int x, int y){
       return x+y;
   }
   public static int subtraction(int x, int y){
       return x-y;
   }
   public static int multiplication(int x, int y){
       return x*y;
   }
   public static int integerDivision(int x, int y){
       return x/y;
   }
   public static double floatDivision(int x, int y){
       return x/(y*1.0);
   }
   public static int modulo(int x, int y){
       return x%y;
   }

}