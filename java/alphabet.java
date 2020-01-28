import java.util.*;
class Main {
  public static void main(String[] args) {
    char ch;
    System.out.println("Enter character:");
    Scanner sc=new Scanner(System.in);
    ch = sc.next().charAt(0);
    System.out.println();
    if((ch>='a' && ch<='z')||(ch>='A' && ch<='Z')){
      System.out.println("Alphabet");
    }
    else{
      System.out.println("not an Alphabet");
    }

  }
}
