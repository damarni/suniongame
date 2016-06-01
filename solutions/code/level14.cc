#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;

// The valid range is [l, r).
string get_path(ll l, ll r, ll x) {
  ll h = (l+r)>>1ll; // Root of the subtree.
  if(x==h) return ""; // We are in the root.
  string ret;
  if(x<h) {
    ret = 'L' + get_path(l, h, x);
  }
  else {
    ret = 'R' + get_path(h+1ll, r, x);
  }
  return ret;
}

int main() {
  int n = 60; // Large enough tree.
  ll u,v; cin >> u >> v;
  string root_to_u_path = get_path(0, 1ll<<(ll(n)), u);
  string root_to_v_path = get_path(0, 1ll<<(ll(n)), v);
  int lca = 0;
  // Remove all common prefix, that is, path to LCA.
  while (lca < root_to_u_path.size() and lca < root_to_v_path.size() and
         root_to_u_path[lca] == root_to_v_path[lca])
    ++lca;
  // Going up until LCA.
  for(int i=lca; i<root_to_u_path.size(); ++i)
    cout << 'U';
  // Go to 'v' using the path from LCA to 'v'.
  for(int i=lca; i<root_to_v_path.size(); ++i)
    cout << root_to_v_path[i];
  cout << endl;
}
