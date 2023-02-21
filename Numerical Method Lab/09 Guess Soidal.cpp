#include<iostream>
#include<math.h>

using namespace std;

#define f1(x,y,z) (17-y+2*z)/20
#define f2(x,y,z) (-18-3*x+z)/20
#define f3(x,y,z) (25-2*x+3*y)/20

int main(){
    double x0,y0,z0,x1,y1,z1,e1,e2,e3,e;
    int count = 1;
    cout<<"Enter the initial Guesses: \n";
    cin>>x0>>y0>>z0;
    cout<<"Enter tolerable error : ";
    cin>>e;
    cout<<"\nCount \tx\ty\tz\n"<<endl;
    do{
        x1=f1(x0,y0,z0);
        y1=f2(x1,y0,z0);
        z1=f3(x1,y1,z0);
        printf("%d \t%.3lf\t%.3lf\t%.3lf\n",count,x1,y1,z1);
        e1 = fabs(x0-x1);
        e2 = fabs(y0-y1);
        e3 = fabs(z0-z1);
        count++;
        x0=x1;
        y0=y1;
        z0=z1;
    }while(e1>e&&e2>e&&e3>e);
    printf("\nSolution : x=%.3lf\ty=%.3lf\tz=%.3lf\n\n",x1,y1,z1);
    return 0;
}
