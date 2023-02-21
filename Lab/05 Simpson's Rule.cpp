#include<iostream>
using namespace std;
double func(double x){
    return (1/(1+x*x));
}

int main(){
    double a,b,h,y;
    int i,n;
    cout<<"Enter the lower limit : ";
    cin>>a;
    cout<<"Enter the upper limit : ";
    cin>>b;
    cout<<"Enter the number of subdivision : ";
    cin>>n;
    h=(b-a)/n;
    if(n%2==0){
        for(i=1;i<n;i++){
            if(i%2==0){
                y=y+2*func(a+i*h);
            }else{
                y=y+4*func(a+i*h);
            }
        }
        y=y+func(a)+func(a+n*h);
        y=y*(h/3);
        printf("Value of the integration : %.5lf\n",y);
    }else{
        cout<<"The number of subdivision should be multiple of two."<<endl;
    }return 0;
}
