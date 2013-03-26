package org.exor.interviewstreet.evernote;

import java.util.Scanner;

public class SelfMult {

	public static void main(String[] args) {
		new SelfMult().solve();
	}

	public void solve() {
		Scanner scan = new Scanner(System.in);
		int N = scan.nextInt();
		int[] arr = new int[N];
		long p = 1;
		int zeroCnt = 0;
		for (int i = 0; i < N; i++) {
			arr[i] = scan.nextInt();
			if (arr[i] != 0)
				p *= arr[i];
			else
				zeroCnt++;
		}
		for (int i : arr) {
			switch (zeroCnt) {
			case 0:
				System.out.println(p / i);
				break;
			case 1:
				System.out.println(i == 0 ? p : 0);	
				break;
			default:
				System.out.println(0);
				break;
			}
		}
	}

}
