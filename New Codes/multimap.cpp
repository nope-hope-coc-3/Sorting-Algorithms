#include<iostream>
#include<map>
#include<string>
using namespace std;
int main()
{
    multimap<char,string> m;
    int n;
    cin>>n;
    //insert
    for(int i=0;i<n;i++)
    {
        char ch;
        string s;
        cin>>ch>>s;
        m.insert(make_pair(ch,s));
    }
    //display
    /*for(auto p:m)
    {
        cout<<p.first<<" "<<p.second<<endl;
    }*/
    //erase
    auto it=m.begin();
    m.erase(it);
    for(auto p:m)
    {
        cout<<p.first<<" "<<p.second<<endl;
    }
    auto it2=m.lower_bound('b');
    auto it3=m.upper_bound('c');
    for(auto it4=it2;it4!=it3;it4++)
    {
        cout<<it4->second<<endl;
    }
    auto f=m.find('b');
    cout<<(*f).second<<endl;
    if(f->second=="bat")
    {
        m.erase(f);
    }
    for(auto p:m)
    {
        cout<<p.first<<" "<<p.second<<endl;
    }
    
    
    return 0;
    
}
