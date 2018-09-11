// Cipher

#include<iostream>
using namespace std;

int main(int argc, char const *argv[])
{
    string s, gg;
    cin>>s;
    int n;
    cin>>n;
    if(n < 0 && n > 1000)
        return 0;
    int k = n & 26;
    int i;
    for (i = 0; s[i] != '\0'; i++);
    int len = i;
    for (i = 0; i < len; i++)
    {
        if (int(s[i]) >= 65 && int(s[i]) <= 90)
        {
            gg[i] = s[i] + k;
        }
        else if (int(s[i]) >= 97 && int(s[i]) <= 122)
        {
            gg[i] = s[i] + k;
        }
        else if (int(s[i]) >= 0 && int(s[i]) <= 9)
        {
            int c = 0;
            c = int(s[i]) % 10;
            gg[i] += c;
        }
    }
    cout<<gg;
    return 0;
}
