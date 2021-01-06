package javaTIL;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;


public class hamburger {
	static int material[];
	static int calo[];
	static int limitCal;
	static int maxScore;
	
	static void go(int depth, int sumScore, int sumCal) {
		
		if (sumScore > maxScore && sumCal <= limitCal)
			maxScore = sumScore;
		
		if (sumCal > limitCal)
			return;
		
		if (depth == material.length)
			return;
		
		go(depth+1, sumScore + material[depth], sumCal + calo[depth]);
		go(depth+1, sumScore, sumCal);	
	}
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		for (int tc = 1; tc <= T; tc++) {
			String[] str = br.readLine().split(" ");
			int materialNum = Integer.parseInt(str[0]);
			limitCal = Integer.parseInt(str[1]);
			material = new int[materialNum];
			calo = new int[materialNum];
			maxScore = 0;

			for (int i = 0; i < materialNum; i++) {
				String[] input = br.readLine().split(" ");	
				material[i] = Integer.parseInt(input[0]);
				calo[i] = Integer.parseInt(input[1]);
			}

			go(0,0,0);	
			System.out.println("#"+tc+" "+maxScore);
		}

	}
	
}
