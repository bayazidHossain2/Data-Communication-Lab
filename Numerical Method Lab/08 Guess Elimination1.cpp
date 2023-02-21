#include<iostream>
using namespace std;
int main(){
    double A[20][20];
    int n;
    cout<<"Enter number of variable : ";
    cin>>n;
    for(int i=1;i<=n;i++){
        for(int j=1;j<=(n+1);j++){
            cout<<"\nInput the Value of A["<<i<<"]["<<j<<"] : ";
            cin>>A[i][j];
        }
    }

    ///Forming Upper Triangle.
    for(int i=1;i<=n;i++){
        for(int j=1;j<=n;j++){
            if(j>i){
                //cout<<"Calculation : "<<i<<' '<<j<<endl;
                double c = A[j][i]/A[i][i];
                for(int k=1;k<=(n+1);k++){
                    A[j][k] = A[j][k]-c*A[i][k];
                }
            }
        }
    }

    ///Showing Upper Triangle Matrix.
    for(int i=1;i<=n;i++){
        for(int j=1;j<=n;j++){
            cout<<A[i][j]<<'\t';
        }cout<<endl;
    }
    double x[n+1];
    for(int i=0;i<=0;i++){
        x[i]=0;
    }
    for(int i=n;i>=1;i--){
        double sum = 0;
        for(int j=1;j<=n;j++){
            if(j!=i){
                sum = sum+A[i][j]*x[j];
            }
        }
        x[i]=(A[i][n+1]-sum)/A[i][i];
    }

    for(int i=1;i<=n;i++){
        cout<<"X"<<i<<" = "<<x[i]<<endl;
    }
    return 0;
}

/*

4

1 2 4 8 5
1 3 9 27 7
1 5 25 125 8
1 7 49 343 9

*/
