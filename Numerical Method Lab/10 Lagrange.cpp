#include<iostream>
#include<math.h>
using namespace std;
int main(){
    int n;
    cout<<"Enter the number of point : ";
    cin>>n;
    double X[n],Y[n],x,y=0;
    cout<<"Enter all the abscissa : "<<endl;
    for(int i=0;i<n;i++){
        cout<<"X["<<i<<"] : ";
        cin>>X[i];
    }
    cout<<"Enter all the ordinate : "<<endl;
    for(int i=0;i<n;i++){
        cout<<"Y["<<i<<"] : ";
        cin>>Y[i];
    }
    cout<<"Enter the Value of x : ";
    cin>>x;
    for(int i=0;i<n;i++){
        double k=1;
        for(int j=0;j<n;j++){
            if(j!=i){
                k=k*(x-X[j])/(X[i]-X[j]);
            }
        }
        y=y+k*Y[i];
    }cout<<"Value of y at x="<<x<<" is : "<<y<<endl;
    return 0;
}
