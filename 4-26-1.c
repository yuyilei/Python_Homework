#include<stdio.h>
int main() {
    short int a[4] , i , j ; 
    unsigned short int b[4] , max , min , res ; 
    for (  i = 0 ; i < 4 ; i ++ ){
        scanf("%hd",&a[i]) ; 
        b[i] = (unsigned short int)a[i] ; 
    }
    max = b[1] ; 
    min = b[1] ; 
    for ( i = 1 ; i < 4 ; i++ ) {
        for ( j = i ; j < 4 ; j++ ){
            if ( max < b[i] ){
                max  = b[i] ; 
            }
            if ( min > b[i] ){
                min = b[i] ;
            }
        }
    }
    res  = max - min ; 
    printf("max:%hu , min:%hu , max - min = %hu",max , min , res) ; 
    return 0 ; 
}
