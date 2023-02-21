#include<bits/stdc++.h>
using namespace std;
//#define f(x) cos(x)-3*x+1
//#define g(x) (1+cos(x))/3

#define f(x) 2*x-cos(x)-3   /// x = 1.5236
#define fi(x) 0.5*(cos(x)+3)

int main()
{
    int step=1;
    float x0,x1,e=0.00001;
    cout<<"Enter initial guess :";
    cin>>x0;
    do
    {
        if(step >50){
            break;
        }
        x1=fi(x0);
        cout<<"Iteration->"<<step<<" : "<<"x1 = "<<x1<<" "<<"f(x1) = "<<f(x1)<<endl;
        step=step+1;
        x0=x1;
    }while(fabs(f(x1))>e);
    cout<<"Root is = "<<x1;

    return 0;
}
