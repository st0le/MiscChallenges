package org.exor.interviewstreet.evernote;

import java.io.FileReader;
import java.util.Iterator;
import java.util.Scanner;

public class CircularBuffer {

	private class CircularArrayIterator implements Iterator<String> {

		private String[] arr;
		private int front, size;

		public CircularArrayIterator(String[] arr, int front, int size) {
			this.front = front;
			this.size = size;
			this.arr = arr;
		}

		@Override
		public boolean hasNext() {
			return size > 0;
		}

		@Override
		public String next() {
			size -= 1;
			return arr[front++ % arr.length];
		}

		@Override
		public void remove() {
			throw new UnsupportedOperationException();
		}

	}

	private class CircularArray implements Iterable<String> {
		private String[] arr;
		private int maxSize, size;
		private int front, rear;

		public CircularArray(int maxSize) {
			arr = new String[this.maxSize = maxSize];
		}

		public void append(String a) {
			arr[rear++ % maxSize] = a;
			if (size < maxSize)
				size++;
			else 
				front++;
		}

		public void remove(int n) {
			if (n >= size) {
				size = 0;
				front = rear = 0;
			} else {
				front += n;
				size -= n;
			}
		}

		@Override
		public Iterator<String> iterator() {
			return new CircularArrayIterator(arr, front, size);
		}

	}

	public static void main(String[] args) throws Exception {
		new CircularBuffer().solve();
	}

	public void solve() throws Exception {
		Scanner scan = null;//new Scanner(System.in);
		scan = new Scanner(
				new FileReader(
						"C:\\Users\\gauravkamath\\Desktop\\Circular-buffer_testcases\\input01.txt"));
		int N = scan.nextInt();
		CircularArray ca = new CircularArray(N);
		boolean done = false;
		while (!done) {
			switch (scan.next().charAt(0)) {
			case 'A':
				int n = scan.nextInt();
				for (int j = 0; j < n; j++)
					ca.append(scan.next());
				break;
			case 'R':
				ca.remove(scan.nextInt());
				break;
			case 'L':
				for (String s : ca)
					System.out.println(s);
				break;
			case 'Q':
				done = true;
				break;
			default:
				break;
			}
		}

	}
}
