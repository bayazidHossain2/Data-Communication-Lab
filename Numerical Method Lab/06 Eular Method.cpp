#include<iostream>
#include<math.h>
using namespace std;

double func(double t,double y){
    return -20*y+7*exp(-0.5*t);///Y(0)=5 h=0.1  Y(0.2) = 4.9659
}
int main(){
    double x0,y0,xn,h,yn,slope;
    int i,n;
    printf("Enter Initial Condition :\n");
    cout<<"x0 = ";
    cin>>x0;
    cout<<"y0 = ";
    cin>>y0;
    cout<<"Enter Calculation point xn = ";
    cin>>xn;
    cout<<"Enter number of steps: ";
    cin>>n;
    h = (xn-x0)/n;
    printf("\nx0\ty0\tslope\tyn\n");
    cout<<"-----------------------------------------"<<endl;
    for(i = 0;i<n;i++){
        slope = func(x0,y0);
        yn = y0+h*slope;
        printf("%.4f\t%.4f\t%.4f\t%.4f\n",x0,y0,slope,yn);
        y0 = yn;
        x0 += h;
    }
    printf("\nValue of y at x = %.4f is %.4f\n",xn,yn);

    return 0;
}
