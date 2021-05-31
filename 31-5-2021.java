import java.util.Scanner;

class Student{
    String name = "";
    int marks;
    Student(String name, int marks)
    {
        this.name = name;
        this.marks = marks;
    }
    public void addExtraMarks(int extraMarks)
    {
        this.marks += extraMarks;
        if(this.marks >100){
            this.marks = 100;
        }
    }
    @Override
    public String toString()
    {
        return  name+":"+marks;
    }
}
public class HELLO{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int N = Integer.parseInt(sc.nextLine());
        List<Student> students = new ArrayList<>();
        for(int ctr=1; ctr<= N; ctr++){
            String studentDetails[]=sc.nextLine.trim().split("\\s+");
            students.add(new Student(studentDetails[0], Integer.parseInt(studentDetails[1])));
        }
        for(Student stud : students) {
            stud.addExtraMarks(sc.nextInt());
            System.out.println(stud);
        }
    }
}