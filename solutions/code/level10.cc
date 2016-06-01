#include <iostream>
typedef unsigned long long ll;

const ll from = 1337;
const ll to = 1333333333333337;

ll f(ll x) {
  ll ans = 0, act = 0;
  for (int bit = 63; bit >= 0; --bit) {
    ll tmp = act | (1ULL<<bit);
    if (tmp <= x) {
      ans += ll(bit) * (1ULL<<(bit-1)) + (tmp^x) + 1;
      act = tmp;
    }
  }
  return ans;
}

int main() {
  std::cout << f(to) - f(from-1) << std::endl;
}
