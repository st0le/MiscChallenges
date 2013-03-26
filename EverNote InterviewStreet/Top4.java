package org.exor.interviewstreet.evernote;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Random;

public class Top4 {

	public static void main(String[] args) throws Exception {
		new Top4().solve();
	}

	private static void swap(int[] arr, int i, int j) {
		int t = arr[i];
		arr[i] = arr[j];
		arr[j] = t;
	}

	/**
	 * @param arr
	 * @param k
	 * @return kth smallest element at arr[k]
	 */
	public static int quickSelect(int[] arr, int k) {
		if (k < 0 || k >= arr.length)
			throw new IllegalArgumentException("k not in range.");
		return quickSelect(arr, 0, arr.length, k);
	}

	private static int quickSelect(int[] arr, int lb, int ub, int k) {
		Random r = new Random();
		while (lb < ub) {
			int left = lb + 1, right = ub - 1;
			int randIndex = r.nextInt(ub - lb) + lb;
			if (lb != randIndex)
				swap(arr, lb, randIndex);
			int pivot = arr[lb];
			do {
				while (left < ub && pivot >= arr[left])
					left++;
				while (right >= lb && pivot < arr[right])
					right--;
				if (left < right)
					swap(arr, left, right);
			} while (left < right);
			swap(arr, lb, right);
			if (k < right) {
				ub = right;
			} else {
				lb = left;
			}
		}
		return arr[k];
	}

	public void solve() throws Exception {
		BufferedReader scan = new BufferedReader(new InputStreamReader(
				System.in), 20 * 1024);
		int N = Integer.valueOf(scan.readLine());
		int[] arr = new int[N];
		for (int i = 0; i < N; i++)
			arr[i] = -Integer.parseInt(scan.readLine());
		quickSelect(arr, 4);
		int[] s = Arrays.copyOf(arr, 4);
		Arrays.sort(s);
		for (int i = 0; i < 4; i++)
			System.out.println(-s[i]);
	}
}
