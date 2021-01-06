package javaTIL;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class calculator2 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		
		for (int tc = 1; tc<=T; tc++) {
			int N = Integer.parseInt(br.readLine());
			String[] str = br.readLine().split(" ");
			int data[] = new int[N];
			for (int i=0; i<N; i++) {
				data[i] = Integer.parseInt(str[i]);
			}
			int max = data[0];
			
			for(int i=1; i<N; i++) {
				if(max == 0 || max == 1) {
					max+=data[i];
				}
				else if(data[i]==0 || data[i]==1) {
					max+=data[i];
				}
				else {
					max*=data[i];
				}
			}
			System.out.println("# " + tc +" "+max);
		}	
	}
}
