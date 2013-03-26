package org.exor.interviewstreet.evernote;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import java.util.PriorityQueue;

public class FrequentTerms {

	public static void main(String[] args) throws Exception {
		new FrequentTerms().solve();
	}

	private class Node implements Comparable<Node>{
		public String w;
		public int freq;

		public Node(String w) {
			this.w = w;
		}

		@Override
		public int compareTo(Node o) {
			if(freq == o.freq)
				return w.compareTo(o.w);
			return freq < o.freq ? 1 : -1;
		}

	}

	public void solve() throws Exception {
		BufferedReader scan = new BufferedReader(new InputStreamReader(
				System.in));
		int N = Integer.parseInt(scan.readLine());
		Map<String, Node> map = new HashMap<String, Node>();
		for (int i = 0; i < N; i++) {
			String w = scan.readLine();
			Node node = map.get(w);
			if (node == null)
				map.put(w, node = new Node(w));
			node.freq++;
		}
		PriorityQueue<Node> pq = new PriorityQueue<Node>(map.values());
		N = Integer.parseInt(scan.readLine());
		while(N-->0 && !pq.isEmpty()) {
			System.out.println(pq.poll().w);
		}
	}
}
