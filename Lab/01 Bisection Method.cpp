#include<iostream>
#include<math.h>
using namespace std;
//#define f(x) x*x*x-x-1 // a = 1 , b = 2, x = 1.325
//#define f(x) x*x*x-3*x-2 // a = 1 , b = 3, x = 2
#define f(x) sin(x)-5*x+2 // a = 0 , b = 1, x = 0.4961
int main(){
    float a,b,m,err,tol=0.0005;
    start:
    cout<<"Enter the initial guess: ";
    cin>>a>>b;
    if(f(a)*f(b)>0){
        cout<<"Initial guess is not correct."<<endl;
        cout<<"f("<<a<<") = "<<f(a)<<endl;
        cout<<"f("<<b<<") = "<<f(b)<<endl;
        cout<<"Try again."<<endl;
        goto start;
    }else{
        int s=0;
        do{
            if(s==50){
                cout<<"limit 50 occur. Increase limit or tolerance."<<endl;
                break;
            }s++;
            m=(a+b)/2.0;
            //cout<<f(a)<<' '<<f(m)<<' '<<f(a)*(f(m))<<endl;
            //cout<<"m "<<f(a)*f(m)<<endl;
            if(f(m)==0){
                cout<<"We found the root is : "<<m<<endl;
                return 0;
            }else if((f(a))*(f(m))<0){
                b=m;
            }else{
                a=m;
            }cout<<"In step : "<<s<<" root is "<<m<<" the value of tolerance is : "<<f(m)<<endl;
            //cout<<a<<' '<<b<<endl;
        }while(fabs(f(m))>tol);
        cout<<endl<<"The approximate root is : "<<m<<", with the tolerance : "<<f(m)<<endl;
    }return 0;
}
