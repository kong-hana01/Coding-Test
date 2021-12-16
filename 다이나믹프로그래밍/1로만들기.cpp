// https://www.acmicpc.net/problem/1463
#include <iostream>
#include <queue>
#include <vector>
#include <functional>
int main() {
	int n;
	std::cin >> n;
	int* arr = new int[n+1];
	for (int i = 0; i < n + 1; i++) arr[i] = 1e6;
	arr[n] = 1;
	std::queue<int> q;
	q.push(n);
	do {
		int x = q.front();
		q.pop();
		if (x % 3 == 0){
			q.push(x / 3);
			arr[x / 3] = std::min(arr[x] + 1, arr[x/3]);
		}
		if (x % 2 == 0) {
			q.push(x / 2);
			arr[x / 2] = std::min(arr[x] + 1, arr[x / 2]);
		}
		if (x > 2) {
			q.push(x - 1);
			arr[x - 1] = std::min(arr[x] + 1, arr[x - 1]);
		}
	}
	while (arr[1] == 1e6);
	std::cout << arr[1] - 1;
}