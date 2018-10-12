// Spread the word
#include<iostream>
using namespace std;

int main(int argc, char const *argv[])
{
    int t, n, a[100000];
    cin>>t;
    if(t < 1 or t > int(1e4))
        exit(1);
    for(int i = 0; i < t; i++)
    {
        cin>>n;
        if(n < 2 or n > int(1e5))
            exit(1);
        for(int y = 0; y < n; y++)
            cin>>a[y];
        for(int y = 0; y < n; y++)
        {
            if(a[y] < 0 or a[y] > n)
                exit(1);
            if(a[0] < 1)
                exit(1);
        }
        int s = 1, count = 1;
        s += a[0];
        if(s >= n)
            cout<<count<<"\n";
        else
        {
            while(s < n)
            {
                for(int y = 0; y < s; y++)
                    s += a[y];
                count += 1;
            }
            cout<<count<<"\n";
        }
    }
    return 0;
}
