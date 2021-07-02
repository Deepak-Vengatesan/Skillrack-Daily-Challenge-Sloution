import java.util.Scanner;

interface College {
    public void printStudentName(String name);
    public void printCollegeName(String name);
}

interface Department {
    public void printDepartmentName(String dept_name);

} 

class Studnet implements College, Department {
    Public void printStudnetName(String name) {
        System.out.println("Name: ",+ name);
    }

    @override 
    public void printDepartmentName(String name){
        System.out.println("Department: " + name);
    }

    @override 
    public void printCollegeName(string name){
        System.out.println("College: " + name);
    }
} // end of studnet

public class Hello{
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        Student stud = new Student();
        stud.printStudentName(sc.nextLine());
        stud.printDepartmentName(sc.nextLine());
        stud.printCollegeName(sc.nextLine());
    } // end of main function
} //end of hello class 



