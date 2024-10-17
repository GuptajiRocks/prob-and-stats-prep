import java.util.Scanner;

class Student {
    Scanner sc = new Scanner(System.in);
    boolean placed;
    boolean accepted;
    boolean eligible;
    boolean offered;
    boolean applied;
    String name;
    String rollNo;
    String branch;
    double cgpa;

    Student(){}

    Student(String nm, String rno, double cg, String brn) {
        name = nm;
        rollNo = rno;
        cgpa = cg;
        branch = brn;
    }

    boolean getCurrentStatus() {
        return applied;
    }

    void updateCGPA(double newcg) {
        cgpa = newcg;
    }

    void offerChoice() {
        System.out.println("Do you want to accept the offer?: ");
        String choice = sc.nextLine();
        if (choice == "yes" || choice == "YES") {
            accepted = true;
        } else {
            accepted = false;
        }
    }
}

class Company {
    String name;
    String role;
    double pack;
    double cgcriteria;
    String date;

    void getSelectedStudents() {

    }

    void updateRole(String newRole) {
        role = newRole;
    }

    void updatePackage(double newPack) {
        pack = newPack;
    }

    void updatecgCriteria(double newcgcri) {
        cgcriteria = newcgcri;
    }
    
}


public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String starterChoice = sc.nextLine();
        if (starterChoice.equals("Enter FutureBuilder")) {
            System.out.println("Entering the program!");
            //FutureBuilderApplication();
        } else {
            System.out.println("Bye bye");
        }  
        
        sc.close();
    }
    
}
