#include<iostream>
using namespace std;

int factorial_cap(int num)
{
    int n = 1, i = 1;
    while(n < num)
    {
        i += 1;   
        n *= i;
    }
    return i;
}

int range_prod(int lo, int hi)
{
    if((lo+1) < hi)
    {
        int mid = (hi+lo)/2;
        return (range_prod(lo, mid) * range_prod(mid+1, hi));
    }
    if (lo == hi)
        return lo;
    return lo * hi;
}

float treefactorial(int n)
{
    if(n < 2)
        return 1;
    return range_prod(1, n);
}

int main(int argc, char const *argv[])
{
    
    return 0;
}
