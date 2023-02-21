#include<iostream>
#include<math.h>
using namespace std;
double func(double t,double y){
    return -20*y+7*exp(-0.5*t);
}
int main(){
    double x0,y0,k1,k2,h,x,y,xn;
    int i,n;
    printf("Enter Initial Condition :\n");
    cout<<"x0 = ";
    cin>>x0;
    cout<<"y0 = ";
    cin>>y0;
    cout<<"Enter Calculation point xn = ";
    cin>>xn;
    cout<<"h = ";
    cin>>h;
    printf("\nx\ty\tk1\tk2\n");
    cout<<"-----------------------------"<<endl;
    for(i = 1;x0<xn;i++){
        k1 = h*func(x0,y0);
        x0 = x0+i*h;
        k2 = h*func(x0,y0+k1);
        y0 = y0+0.5*(k1+k2);
        printf("%.4f\t%.4f\t%.4f\t%.4f\n",x0,y0,k1,k2);
    }
    printf("\nValue of y at x = %.4f is %.4f\n",xn,y0);

    return 0;

}
