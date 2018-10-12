#include<iostream>
using namespace std;

int max(int a[], int n)
{
    int m = a[0];
    for(int i = 0; i < n; i++)
    {
        if(a[i] > m)
            m = a[i];
    }
    return m;
}

int ind(int a[], int n, int m)
{
    int i = 0;
    for(;i < n; i++)
    {
        if (a[i] == m)
            break; 
    }
    return i;
}

int main(int argc, char const *argv[])
{
    int t, n, a[100000], b[100000];
    cin>>t;
    if(t < 1 || t > int(1e3))
        exit(1);
    for(int i = 0; i < t; i++)
    {
        cin>>n;
        if(n < 1 || n > int(1e5))
            exit(1);
        for(int j = 0; j < n; j++)
        {
            cin>>a[j];
            if(a[j] < 0 || a[j] > int(1e8))
                exit(1);
        }
        for(int j = 0; j < n; j++)
        {   
            cin>>b[j];
            if(b[j] < 0 || b[j] > int(1e8))
                exit(1);
        }
        int m = max(b, n);
        int index = ind(b, n, m);
        if(b[index - 1] >= b[index] || b[index - 2] >= b[index] || b[index + 1] >= b[index] || b[index + 2] >= b[index])
            cout<<"NIE"<<"\n";
        else
            cout<<"TAK"<<"\n";
    }
    return 0;
}
