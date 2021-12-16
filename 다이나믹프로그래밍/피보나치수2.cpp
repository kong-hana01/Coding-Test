// https://www.acmicpc.net/problem/2748
#include <iostream>
int main() {
	int n;
	std::cin >> n;
	long long int *arr = new long long int [n+1];
	arr[0] = 0;
	arr[1] = 1;
	for (int i = 2; i <= n; i++) arr[i] = arr[i - 2] + arr[i - 1];
	std::cout << arr[n];
}