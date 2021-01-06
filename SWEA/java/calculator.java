package javaTIL;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class calculator {

	static int data[];
	static int max;
	static int N;
	
	static void cal(int depth, int sum) {
		if (depth == N) {
			if (sum > max) {
				max = sum;
			}
			return;
		}
		cal(depth+1, sum+data[depth]);
		cal(depth+1, sum*data[depth]);
		
	}
	
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		
		for (int tc = 1; tc<=T; tc++) {
			N = Integer.parseInt(br.readLine());
			String[] str = br.readLine().split(" ");
			data = new int[N];
			for (int i=0; i<N; i++) {
				data[i] = Integer.parseInt(str[i]);
			}
			max = 0;
			
			cal(1,data[0]);
			System.out.println("# " + tc +" "+max);
		}	

	}

}
