long long gcd(long long a, long long b){
    if (a < b) swap(a, b);
    while(b != 0){
        a = a % b;
        swap (a, b);
    }
    return a;
}

long long lmc(long long a, long long b){
    return a*b/gcd(a, b);
}