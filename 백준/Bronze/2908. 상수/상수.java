import java.util.Scanner;

public class Main {
	public static void main(String[] args) {	
		Scanner scan = new Scanner(System.in);
		int num1 = scan.nextInt();
		
		String strNum1 = String.valueOf(num1);
		int num2 = scan.nextInt();
		String strNum2 = String.valueOf(num2);

		String rStrNum1 = new StringBuffer(strNum1).reverse().toString();
		String rStrNum2 = new StringBuffer(strNum2).reverse().toString();
		
		int rNum1 = Integer.parseInt(rStrNum1);
		int rNum2 = Integer.parseInt(rStrNum2);
		
		if(rNum1 > rNum2) {
			System.out.println(rNum1);
		} else {
			System.out.println(rNum2);
		}
	}
}
