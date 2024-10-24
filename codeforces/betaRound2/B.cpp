
// #include<iostream>
// #include<vector>
// #include<array>
// using namespace std;

// array<int, 2> process(int value) {
//     int counter2=0;
//     int counter5=0;

//     while(true){
//         if(value%2!=0){
//             break;
//         }
//         else{
//             counter2++;
//             value/=2;
//         }
//     }

//     while(true){
//         if(value%5!=0){
//             break;
//         }
//         else{
//             counter5++;
//             value/=5;
//         }
//     }
//     return array<int,2>{counter2,counter5};
// }

// int main(){


//     int n;
//     cin>>n;

//     int matrix[n][n][6];
//     // vector< vector< array<int, 2> > > matrix;


//     for(int i=0;i<n;i++){
//         for(int j=0;j<n;j++){
//             int v;
//             cin>>v;


//             array<int,2> current=process(v);
//             // cout << "Processed value: " << current[0] << ", " << current[1] << endl;
//             matrix[i][j][0]=current[0];
//             matrix[i][j][1]=current[1];
//             matrix[i][j][2]=0;

//             matrix[i][j][3]=current[0];
//             matrix[i][j][4]=current[1];
//             matrix[i][j][5]=0;


//             //initlly hold [a,b,.....]
//             //later modify to [a,b,path,a,b,path] 
//         }
//     }

//     // cout<<matrix[1][1][0]<<"\n";

//     // for(int i=0;i<n;i++){
//     //     for(int j=0;j<n;j++){
//     //         cout<<matrix[i][j][0]<<matrix[i][j][1]<<matrix[i][j][3]" ";

//     //     }
//     // }

//     // int array1[n][6];
//     // int array2[n][6];

//     // for(int i=2;i<=n;i++){
//     //     int left=i-1;
//     //     int right=0;
//     //     for(int j=0;j<i;j++){

//     //         array2[j]=matrix[left][right];

//     //         // first=
//     //         // current=array2[j];
//     //         // bool left,top;
//     //         if(j-1>=0){
//     //             left=true;
//     //         }
            
//     //         // if()
//     //         left--;
//     //         right++;
//     //         //left = array1[j-1]
//     //         //top =array1[j]




//     //     }
//     // }
//     int j=1;
//     int left=0;
//     int right=0;
//     for(int i=0;i<2*n-1;i++){
//        int sum=i;
//        for(int j=0;j<i+1;j++){
//         left=sum-j;
//         right=j;
//         // if((0<=left<n) && (0<=right<n))
//         // if ((0 <= left && left < n) && (0 <= right && right < n))
//         // {
//         //     cout<<left<<right<<"\n";
//         //     if((left==0)&&(right==0)){

//         //     }
//         //     else if(((left-1>=0)&&(left-1<n)) && ((0<=right-1)&&(right-1<n))){
//         //         array <int,12> cases;
//         //         // cout<<"hi";
//         //         //left case
//         //         for(int f=0;f<12;f++){
//         //             if(f<=5){
//         //                 //left
//         //                 cases[f]=matrix[left][right-1][f]+matrix[left][right][f];    
//         //             }
//         //             else{
//         //                 int holder=11-f;
//         //                 cases[holder]=matrix[left][right-1][holder]+matrix[left][right][holder];
//         //             }

//         //         }
//         //         // cout<<cases[0]<<"ffff";
//         //         cases[2]=1;
//         //         cases[5]=1;
//         //         cases[8]=2;
//         //         cases[11]=2;

//         //         //min a

//         //         array <int,3> mina={cases[0],cases[1],cases[2]};
//         //         // cout<<mina[0];
//         //         array <int,3> minb={cases[0],cases[1],cases[2]};


//         //         for(int g=0;g<4;g++){
//         //             int a=cases[g*3];
//         //             int b=cases[g*3+1];
//         //             if(a<=mina[0]){
//         //                 if(a<mina[0]){
//         //                     mina={a,b,cases[g*3+2]};
//         //                 }
//         //                 else if(a==mina[0]){
//         //                     if(b<mina[1]){
//         //                         mina={a,b,cases[g*3+2]};
//         //                     }
//         //                 }
//         //             }

//         //         }

//         //         for(int g=0;g<4;g++){
//         //             int a=cases[g*3];
//         //             int b=cases[g*3+1];
//         //             if(b<=minb[1]){
//         //                 if(b<minb[1]){
//         //                     minb={a,b,cases[g*3+2]};
//         //                 }
//         //                 else if(b==minb[1]){
//         //                     if(a<minb[1]){
//         //                         minb={a,b,cases[g*3+2]};
//         //                     }
//         //                 }
//         //             }

//         //         }
//         //         // cout<<mina[0]<<"hfeiuhfw";
//         //         for( int r=0;r<3;r++){
//         //             matrix[left][right][r]=mina[r];
//         //             matrix[left][right][r+3]=minb[r];
//         //         }





//         //     }
//         if((left>=0 && left<n)&&(right>=0 && right<n)){
           
//             if (left > 0 && right > 0) {
//                 cout<<"wefiuhe";
//                 array<int, 12> cases = {0}; // Initialize cases array to zero

//                 // Left case
//                 for (int f = 0; f < 12; f++) {
//                     if (f <= 5) {
//                         cases[f] = matrix[left][right - 1][f] + matrix[left][right][f];
//                     } else {
//                         // int holder = 11 - f;
//                         cases[f] = matrix[left-1][right][f%6] + matrix[left][right][f%6];
//                     }
//                 }

//                 for(int g=0;g<12;g++){
//                     cout<<cases[g]<<" ";
//                 }

//                 // Initialize minimum arrays with maximum values
//                 array<int, 3> mina = {numeric_limits<int>::max(), numeric_limits<int>::max(), 0};
//                 array<int, 3> minb = {numeric_limits<int>::max(), numeric_limits<int>::max(), 0};

//                 // Loop through cases to find mina and minb
//                 for (int g = 0; g < 4; g++) {
//                     int a = cases[g * 3];
//                     int b = cases[g * 3 + 1];
//                     int direction = cases[g * 3 + 2];

//                     // Update mina
//                     if (a < mina[0] || (a == mina[0] && b < mina[1])) {
//                         mina = {a, b, direction};
//                     }

//                     // Update minb
//                     if (b < minb[1] || (b == minb[1] && a < minb[0])) {
//                         minb = {a, b, direction};
//                     }
//                 }

//                 // Store results back into the matrix
//                 for (int r = 0; r < 3; r++) {
//                     matrix[left][right][r] = mina[r];
//                     matrix[left][right][r + 3] = minb[r];
//                 }
//             } // Closing bracket for the outer block


            

//                 else if((left==0)&&(right>0)){
                    

//                         if(right>0){
//                             for(int t=0;t<6;t++){
//                                 matrix[left][right][t]+=matrix[left][right-1][t];
//                             }
//                             matrix[left][right][2]=1;
//                             matrix[left][right][5]=1;
//                         }




//                 }
//                 else if((right==0)&&(left>0)){

                
//                     if(left>0){
//                         for(int t=0;t<6;t++){
//                             matrix[left][right][t]+=matrix[left-1][right][t];
//                             cout<<matrix[left-1][right][t]<<"and"<< matrix[left][right][t]<<"\n";
//                         }
//                         matrix[left][right][2]=2;
//                         matrix[left][right][5]=2;
//                     }

//                 }
//             }
//         }
//         // else if(0<left<n && 0<right<n){

//         // }
        
//     }

//     int lookFor=1;
//     int lowest=0;
//     int lookAt=0;
//     if(matrix[n-1][n-1][0]<matrix[n-1][n-1][4])
//         {
//             lookFor=1;
//             lookAt=2;
//             lowest=matrix[n-1][n-1][0];
//         }
//     else{
//         lookFor=2;
//         lookAt=5;
//         lowest=matrix[n-1][n-1][4];
//     }

//     int steps=2*n-2;
//     int currenti=n-1;
//     int currentj=n-1;
//     char path[steps];

//     for(int i=0;i<steps;i++){
//         // cout<<matrix[currenti][currentj][lookAt];
//         if(matrix[currenti][currentj][lookAt]==1){
//             path[i]='R';
//             currentj--;
//         }
//         else{
//             path[i]='D';
//             currenti--;
//         }
//     }

//     for( int i=0;i<steps;i++){
//         cout<<path[i];
//     }

//     for(int i=0;i<n;i++){
//         for( int j=0;j<n;j++){
//             cout<<i<<j<<" ";
//             for(int p=0;p<6;p++){
//                 cout<<matrix[i][j][p]<<" ";
//             }
//             cout<<"\n";
//         }
//     }

//     // char path[steps-1];





//     return 0;
// }



#include <iostream>
#include <vector>
#include <array>
#include <limits>
#include <algorithm>
using namespace std;

array<int, 2> process(int value) {
    int counter2 = 0, counter5 = 0;

    while (value > 0 && value % 2 == 0) {
        counter2++;
        value /= 2;
    }

    while (value > 0 && value % 5 == 0) {
        counter5++;
        value /= 5;
    }

    return {counter2, counter5};
}

int main() {
    int n;
    cin >> n;

    if (n <= 0) {
        cout << "Matrix size must be greater than zero." << endl;
        return 1; // Exit if n is not valid
    }

    // Create a 2D vector to store (count of 2s, count of 5s, path direction)
    vector<vector<array<int, 3>>> matrix(n, vector<array<int, 3>>(n, {0, 0, 0}));

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            int v;
            cin >> v;
            auto current = process(v);
            matrix[i][j][0] = current[0]; // count of 2s
            matrix[i][j][1] = current[1]; // count of 5s
        }
    }

    // Initialize the first cell
    matrix[0][0][2] = -1; // Starting point, no direction

    // Fill the matrix with dynamic programming
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (i == 0 && j == 0) continue; // Skip the starting cell

            // Check from the top cell
            if (i > 0) {
                int newCount2 = matrix[i - 1][j][0] + matrix[i][j][0];
                int newCount5 = matrix[i - 1][j][1] + matrix[i][j][1];
                
                if (newCount2 < matrix[i][j][0] || (newCount2 == matrix[i][j][0] && newCount5 < matrix[i][j][1])) {
                    matrix[i][j][0] = newCount2;
                    matrix[i][j][1] = newCount5;
                    matrix[i][j][2] = 1; // Coming from above
                }
            }

            // Check from the left cell
            if (j > 0) {
                int newCount2 = matrix[i][j - 1][0] + matrix[i][j][0];
                int newCount5 = matrix[i][j - 1][1] + matrix[i][j][1];

                if (newCount2 < matrix[i][j][0] || (newCount2 == matrix[i][j][0] && newCount5 < matrix[i][j][1])) {
                    matrix[i][j][0] = newCount2;
                    matrix[i][j][1] = newCount5;
                    matrix[i][j][2] = 2; // Coming from left
                }
            }
        }
    }

    // Determine the minimum trailing zeros
    int minZeros = min(matrix[n - 1][n - 1][0], matrix[n - 1][n - 1][1]);
    cout << minZeros << endl;

    // Backtrack to find the path
    string path;
    int currentI = n - 1, currentJ = n - 1;
    
    while (currentI != 0 || currentJ != 0) {
        if (matrix[currentI][currentJ][2] == 1) { // Coming from above
            path.push_back('D');
            currentI--;
        } else { // Coming from left
            path.push_back('R');
            currentJ--;
        }
    }

    reverse(path.begin(), path.end());
    cout << path << endl;

    return 0;
}
