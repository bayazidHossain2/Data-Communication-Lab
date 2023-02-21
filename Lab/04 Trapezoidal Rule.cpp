#include<iostream>
#include<math.h>
using namespace std;
/*
double f(double x){
    return 1/(1+pow(x,2));
}*/
double f(double x){
    return (1/x);
}

int main(){
    double a,b,integration,h,k;
    int i,n;
    cout<<"Enter lower limit of integration : ";
    cin>>a;
    cout<<"Enter upper limit of integration : ";
    cin>>b;
    cout<<"Enter number of sub intervals: ";
    cin>>n;
    h=(b-a)/n;
    integration = f(a)+f(b);
    for(int i=1;i<=n-1;i++){
        k=a+i*h;
        cout<<"value of x"<<i<<" : "<<k<<" f(x"<<i<<") : "<<f(k)<<endl;
        integration=integration+2*f(k);
    }
    integration=integration*h/2;
    cout<<"Required value of integration is:  "<<integration<<endl;
    return 0;
}
