#include<iostream>
using namespace std;

int main(int argc, char const *argv[])
{
    int m, n;
    cin>>m>>n;
    int a[m][n];
    int c, d;
    int row[m];
    int col[n];
    int p = 0, r = 0;
    for(int i = 0; i < m; i++)
    {
        for(int j = 0; j < n; j++)
        {
            cin>>a[i][j];
            if(a[i][j] == 0)
            {
                row[p] = i;
                col[r] = j;
                p++, r++;   
            }
        }
    }
    for(int i = 0; i < m; i++)
    {
        for(int j = 0; j < n; j++)
        {
            for(int k = 0; k < max(m, n); k++)
            {
                if(row[k] == i || col[k] == j)
                    a[i][j] = 0;
            }
        }
    }
    for(int i = 0; i < m; i++)
    {
        for(int j = 0; j < n; j++)
            cout<<a[i][j]<<"\t";
        cout<<"\n";
    }
    return 0;
}
