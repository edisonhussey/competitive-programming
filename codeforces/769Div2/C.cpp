#include<iostream>
using namespace std;


int main(){
    int cases;
    cin>>cases;

    while(cases--){
        int a,b;

        cin>>a>>b;

        int min=b-a;

        for(int i=0;i<b-a;i++){
            for(int j =0;j<b-a;j++){
                
                int ma=i;
                int mb=j;

                if(((a+ma)&(a+ma-1))==0){

                    int newB=b+mb;
                    int newA=newB | (a+ma);
                    int overflow=newA-newB;
                    if(overflow+1+mb+ma<min){
                        min=overflow+1+mb+ma;
                    }


                }


                // int newB=b+mb;
                // int newA=newB | (a+ma);
                // int overflow=newA-newB;
                // if(overflow+1+mb+ma<min){
                //     min=overflow+1+mb+ma;
                // }


            }
        }
        cout<<min<<"\n";
    }


    return 0;
}