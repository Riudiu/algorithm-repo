import java.util.Scanner;

public class Main {	
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		
		int a = scan.nextInt();    // 고정 비용
		int b = scan.nextInt();    // 가변 비용
		int c = scan.nextInt();    // 노트북의 가격
		
		long cost = 0;      // 총 비용 (고정비용+가변비용)
		long income = 0;    // 총 수익 (매출)
		long bep = 0;       // 손익분기점 (최초로 이익이 발생하는 판매갯수 세는 변수)
		
		if(b >= c) {      // 가변비용(노트북을 만드는데 필요한 비용)이 노트북 판매 가격보다 비쌀 경우
			bep = -1;     // 손익분기점이 존재할 수 없음 -> 손익분기점 -1로 고정 
			System.out.println(bep);
			
		} else {			// 판매가격이 더 높아서 이익이 발생하는 경우
			cost += a;       // 총 비용에 고정비용을 먼저 삽입
			
			while(true) {    // 손익분기점 돝파할 때까지 무한 반복
				bep += 1;     // 노트북 판매갯수 1씩 증가(손익분기점 카운팅) 
				cost += b;    // 총 비용에 노트북 생산에 필요한 가변비용 삽입
				income += c;   // 총 수익 또는 총 매출에 노트북 가격 삽입
				
				if(cost < income) {    // 총 수익이 총 비용을 넘어서는 경우 -> 손익분기점 돌파 
					break;    // 반복문 탈출
				}
			}
			System.out.println(bep);     // 손익분기점 출력
		}
		scan.close();
	}
}
