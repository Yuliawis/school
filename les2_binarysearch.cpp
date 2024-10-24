#include <iostream>
#include <vector>

using namespace std;

int main() {
    int n, k;
    cin >> n >> k;
    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    // a[low] < k
    // a[high] >= k
    int low = -1;
    int high = n;

    while (low + 1 < high) {
        int mid = (low + high)/2;
        if (a[mid] >= k) {
            high = mid;
        }
        else {
            low = mid;
        }
        
    }
    cout << low << ' ' << high << endl;
    cout << a[high] << endl;
    
    if (high < n && a[high] == k){
        cout << "Yes";
    }
    else {
        cout << "No";
    }
}