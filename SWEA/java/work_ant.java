package javaTIL;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;


public class work_ant {

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int data[][] = new int[10][10];
		int dy[] = {0,1};
		int dx[] = {1,0};
		
		for(int y=0; y<10; y++) {
			String[] line = br.readLine().split(" ");
			for(int x=0; x<10; x++) {
				data[y][x] = Integer.parseInt(line[x]);
			}
		}
		
		data[1][1] = 9;
		int sy = 1;
		int sx = 1;
		boolean flag = true;
		
		while(true) {
			if (flag) {
				int ny = sy + dy[0];
				int nx = sx + dx[0];
				if(data[ny][nx] == 0) {
					data[ny][nx] = 9;
					sy = ny;
					sx = nx;
				}
				else if (data[ny][nx] == 1) {
					ny = sy+dy[1];
					nx = sx+dx[1];
					if(data[ny][nx] == 0) {
						flag = true;
						sy = ny;
						sx = nx;
						data[ny][nx] = 9;
					}
					else {
						if(data[ny][nx] == 2) {
							data[ny][nx] = 9;
							break;
						}
						else {break;}
					}					
				}
				else {
					data[ny][nx] = 9;
					break;
				}
			}
			
		}
		for (int y=0; y<10; y++) {
			System.out.println();
			for(int x = 0; x<10; x++) {
				if(x==9) {
					System.out.print(data[y][x]);
				}
				else
				System.out.print(data[y][x]+" ");
			}
		}
		
	}

}
