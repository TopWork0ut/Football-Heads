#include <stdio.h>
int number;  // кількість заданих сторні
int count;   // змінна в яку передаємо кількість триктуників 
int fUNCtion(int n); //прототип функції

int main(){

   int n;
   
   printf("Скільки чисел ви хочете ввести? : ");
   scanf("%d",&n);  //вводимо к-сть сторін
   fUNCtion(n);    //викликаємо функцію
   return 0;
}


int fUNCtion(int n){ 
    
    int sides[n]; 
    
    for (int i = 1; i <= n  ; i++){        //надаємо масиву чисел
         if ( n >= 3){
             printf("\nВведіть число %d : ",i);
             scanf("%d" , &number);
             sides[i] = number;
             
         }
         else {
            printf("\nВи ввели замале число сторін - мінімум 3");
            break;
         }
         
    }
    
    if (n >= 3 ){
    
        for (int i = 0; i <= n; i++) {
            for (int j = i + 1; j <= n; j++) {
                for (int k = j + 1; k <= n; k++){
 
                
                    if (   sides[i] + sides[j] > sides[k]
                        && sides[i] + sides[k] > sides[j]
                        && sides[k] + sides[j] > sides[i]) {
                        
                        count++;
                        printf("\n(%d,%d,%d) ",sides[i],sides[j],sides[k]);
                    }
                }
            }
        }
    } 
    printf("\n\nКількість трикутників = %d",count);
    return count; //повертає значення кількості можливих трикутників
}