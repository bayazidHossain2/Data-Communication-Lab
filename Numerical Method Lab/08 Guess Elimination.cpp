#include<iostream>
#include<math.h>
using namespace std;

int main(){
    int i,j,k,n;
    float A[20][20],c,x[10],sum;
    printf("\nEnter the number of variables: ");
    cin>>n;
    printf("\nEnter the elements of augmented matrix row-wise: \n\n");
    for(i=1;i<=n;i++){
        for(j=1;j<=(n+1);j++){
            printf("A[%d][%d] : ",i,j);
            cin>>A[i][j];
        }
    }
    ///Generation of upper triangular matrix
    for(i=1;i<=n;i++){
        for(j=1;j<=n;j++){
            if(j>i){
                c=A[j][i]/A[i][i];
                for(k=1;k<=(n+1);k++){
                    A[j][k]=A[j][k]-c*A[i][k];
                }
            }
        }
    }
    ///Upper Traingular Matrix
    printf("\nThe Upper Triangular matrix is:\n\n");
    for(i=1;i<=n;i++){
        for(j=1;j<=(n+1);j++){
            if(j==(n+1)){
                printf(" : ");
            }
            printf("%.3f ",A[i][j]);
        }cout<<endl;
    }
    for(int i=1;i<=n;i++){
        x[i]=0;
    }
    ///Backward Substitution
    printf("\nAfter Applying Backward Substitution.\n");
    for(i=n;i>=1;i--){
        sum=0;
        for(j=1;j<=n;j++){
            if(i!=j){
                sum = sum+A[i][j]*x[j];
            }
        }
        x[i]=(A[i][n+1]-sum)/A[i][i];
    }
    printf("\nThe solution is : \n");
    for(i=1;i<=n;i++){
        printf("\nx%d=%.4f\t",i,x[i]);
    }
    return 0;
}
