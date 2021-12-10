// (세 자리 수) × (세 자리 수)는 다음과 같은 과정을 통하여 이루어진다.
// (생략)

import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        int a, b;
        a = sc.nextInt();
        b = sc.nextInt();
        int result = a*b;
        
        int tempNum = b;
        while(tempNum > 0) {
            b = tempNum%10;
            tempNum /= 10;
            System.out.println(a*b);
        }
        System.out.println(result);
    }   
}