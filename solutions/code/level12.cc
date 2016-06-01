#include <iostream>
using namespace std;
typedef unsigned long long ll;
const ll from = 0;
const ll to = 1152921504606847076ULL;

int main() {
  ll cur = 1286634875943980746ULL;
  ll pot = 1;
  while ((pot<<1) < to) {
    pot <<= 1;
  }
  for (ll i = pot; i <= to; ++i) {
    cur ^= i;
  }
  cout << cur << endl;
}
