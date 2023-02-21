#include<iostream>
#include<math.h>
using namespace std;
//#define pi 3.14159
//#define f(x) 3*x-cos(x*pi/180.0)-1
//#define df(x) 3+sin(x*pi/180.0)
//#define f(x) x*x-4*x-7
//#define df(x) 2*x-4
#define f(x) cos(x) - x*exp(x)
#define df(x) -sin(x)-exp(x)-x*exp(x)

int main(){
    double x0,xi,e=0.001;
    cout<<"Enter the initial guess : ";
    cin>>x0;
    int step=0;
    do{
        step++;
        xi=x0-((f(x0))/((df(x0))+0.0));
        cout<<"Step "<<step<<": x = "<<xi<<" f(x) : "<<(f(xi))<<endl;
        x0=xi;
    }while(step<20&&(fabs(f(xi))>e));

    cout<<"Hence root is : "<<x0<<endl;
    return 0;
}
