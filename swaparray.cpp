#include<iostream>
using namespace std;
int main()
{
    int arr[5]={10,20,30,40,50};
    int i;
    int n=5;
    cout<<arr[0]<<endl;
    for(i=0;i<n/2;i++)
    {
        arr[i]=arr[n-i-1]+arr[i];
        arr[n-i-1]=arr[i]-arr[n-i-1];
        arr[i]=arr[i]-arr[n-i-1];

    }
    cout<<arr[0]<<endl;
    for(i=0;i<n;i++)
        cout<<arr[i];
    return 0;
}
