import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);   
		int sum = 0;      // 총점을 담는 변수 sum
		
		for (int i = 0; i < 5; i++) {    // 반복문을 통해 5회 실행   
			int num = scan.nextInt();    // 입력받는 점수, 새로 입력받을 때마다 초기화
			sum += num;        // 입력받은 점수를 sum에 담기
		}
		System.out.println(sum);   // 총점 출력
	}
}
