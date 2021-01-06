package javaTIL;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class spaghetti {
	static int count;
	static int sandClock[];
	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		
		for(int tc=1; tc<=T; tc++) {
			count = 0;
			String[] str =  br.readLine().split(" ");
			int N = Integer.parseInt(str[0]);
			int B = Integer.parseInt(str[1]);
			int E = Integer.parseInt(str[2]);
			String[] clock = br.readLine().split(" ");
			sandClock = new int[N];
			for(int i=0; i<N; i++) {
				sandClock[i] = Integer.parseInt(clock[i]);
			}
			
			for(int j=0; j<N; j++) {
				for(int k=B-E; k <= (B+E); k++) {
					if (sandClock[j] == k) {
						count+=1;
					}
				}
				
				
			}
			System.out.println("#"+tc+" "+count);
		}
	}

}
