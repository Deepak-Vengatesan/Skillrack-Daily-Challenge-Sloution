import java.util.*;

class Student{
   String name,regno;
   int age;
   Student(String name,int age,String regno){
       this.name = name.toLowerCase();
       this.regno = regno.toLowerCase();
       this.age = age;
   }
   public boolean equals(Student stud){
       if(this.age == stud.age){
           if(this.name.equals(stud.name)){
               if(this.regno.equals(stud.regno)){
                   return true;
               }
           }
           return false;
       }
       return false;
   }
}

public class Hello{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        Student student1 = getStudent(sc);
        Student student2 = getStudent(sc);
        System.put.println(student1.equals(student2)? "EQUAL" : "NOT EQUAL");

    } // end of main method

    private static Student getStudent(scanner sc){
        String name = sc.nextLine().trim();
        int age = Integer.parseInt(sc.nextLine().trim());
        String country = sc.nextLine().trim();
        return new Student(name, age, country);
    } // end of getCitizen method
} // end of Hello world