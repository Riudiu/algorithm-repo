import java.util.*;

public class Main {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		Map<Integer, Integer> input = new HashMap<>();
		int max = 0;    // 최댓값을 담는 변수 max
		
		for (int i = 1; i <= 9; i++) {
			int num = scan.nextInt();
			input.put(num, i);
			
			if (max < num) {
				max = 0;
				max += num;
			}
		}
		System.out.println(max);
		System.out.println(input.get(max));
	}
}
