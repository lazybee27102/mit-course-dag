/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package tabulation;

/**
 *
 * @author phatnguyen Fibonacci solution bottom-up
 */
public class Fibonacci {

    public static int fib(int n) {
        if (n < 2) {
            return n;
        }

        int f[] = new int[n + 1];
        f[0] = 0;
        f[1] = 1;

        // 0,1,1,2,3,5,8
        // ....^ start from 2
        for (int i = 2; i <= n; i++) {
            f[i] = f[i - 1] + f[i - 2];
        }

        return f[n];
    }

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        System.out.println("The value of fibonacci at " + 0 + " is " + fib(0));
        System.out.println("The value of fibonacci at " + 1 + " is " + fib(1));
        System.out.println("The value of fibonacci at " + 2 + " is " + fib(2));
        System.out.println("The value of fibonacci at " + 5 + " is " + fib(5));
        System.out.println("The value of fibonacci at " + 10 + " is " + fib(10));
        System.out.println("The value of fibonacci at " + 20 + " is " + fib(20));
        System.out.println("The value of fibonacci at " + 40 + " is " + fib(40));
    }

}
