/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package memoization;

import java.util.HashMap;
import java.util.Map;

/**
 *
 * @author phatnguyen
 * Top-down solution
 *                              
                         fib(5)
                     /             \
               fib(4)                fib(3)
             /      \                /     \
         fib(3)      fib(2)         fib(2)    fib(1)
        /     \        /    \       /    \
  fib(2)   fib(1)  fib(1) fib(0) fib(1) fib(0)
  /    \
fib(1) fib(0)

 * fib(3) appears 2 times
 * fib(2) appears 3 times
 * Solution: Store the value inside a lookup table then get it whenever need it
 * without computing again.
 */
public class Fibonacci {

    private Map<Integer, Integer> lookupNumbers = new HashMap<>();

    public int fib(int n) {
        if (!lookupNumbers.containsKey(n)) {
            if (n <= 1) {
                lookupNumbers.put(n, n);
            } else {
                lookupNumbers.put(n, fib(n - 1) + fib(n - 2));
            }
        }

        return lookupNumbers.get(n);
    }

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Fibonacci fibonacci = new Fibonacci();
        System.out.println("The value of fibonacci at " + 0 + " is " + fibonacci.fib(0));
        System.out.println("The value of fibonacci at " + 1 + " is " + fibonacci.fib(1));
        System.out.println("The value of fibonacci at " + 2 + " is " + fibonacci.fib(2));
        System.out.println("The value of fibonacci at " + 5 + " is " + fibonacci.fib(5));
        System.out.println("The value of fibonacci at " + 10 + " is " + fibonacci.fib(10));
        System.out.println("The value of fibonacci at " + 20 + " is " + fibonacci.fib(20));
        System.out.println("The value of fibonacci at " + 40 + " is " + fibonacci.fib(40));
    }

}
