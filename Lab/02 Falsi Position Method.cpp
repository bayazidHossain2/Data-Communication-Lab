#include<iostream>
#include<math.h>
using namespace std;
double fn(double x){
    //return x*x*x-x-1; //a = 1, b = 2, x = 1.32467
    return x*x*x-9*x+1; //a = 2, b = 4, x = 2.9428

}
int main(){
    cout<<7/6.0<<endl;
    double a,b,m,err,tol=0.0005;
    start:
    cout<<"Enter the initial guess: ";
    cin>>a>>b;
    if(fn(a)*fn(b)>0){
        cout<<"Initial guess is not correct."<<endl;
        cout<<"f("<<a<<") = "<<fn(a)<<endl;
        cout<<"f("<<b<<") = "<<fn(b)<<endl;
        cout<<"Try again."<<endl;
        goto start;
    }else{
        int s=0;
        do{
            if(s==50){
                break;
            }s++;
            ///Formula for falsi position Method.
            m=(a*(fn(b))-b*(fn(a)))/((fn(b))-(fn(a))+0.0);

            //cout<<fn(a)<<' '<<fn(m)<<' '<<(fn(m))<<endl;
            //cout<<"m is : "<<m<<endl;
            cout<<"f(m) is : "<<fn(m)<<endl;
            if(fn(m)==0){
                cout<<"We found the root is : "<<m<<endl;
                return 0;
            }else if((fn(m))<0){
                a=m;
            }else{
                b=m;
            }cout<<"In step : "<<s<<" root is "<<m<<" the value of error is : "<<fn(m)<<endl;
            //cout<<a<<' '<<b<<endl;
        }while(fabs(fn(m))>tol);
        cout<<endl<<"The approximate root is : "<<m<<", with the error is : "<<fn(m)<<endl;
    }return 0;
}

