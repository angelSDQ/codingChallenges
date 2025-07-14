package Java;

// Problem: Quadratic Equation Solver

// Given three real number coefficients `a`, `b`, and `c` of a quadratic equation of the form: ax² + bx + c = 0

// Return the real roots of the equation using the quadratic formula: x = (-b ± √(b² - 4ac)) / 2a

// Return:
// - A list of two real roots [x1, x2] if the discriminant is positive.
// - A list with a single real root [x] if the discriminant is zero.
// - An empty list [] if there are no real roots (i.e., discriminant < 0).

// Constraints:
// - -1000 ≤ a, b, c ≤ 1000
// - a ≠ 0

// Example 1:
// Input: a = 1, b = -3, c = 2
// Output: [2.0, 1.0]
// Explanation: The roots are x = 2 and x = 1

// Example 2:
// Input: a = 1, b = 2, c = 1
// Output: [-1.0]
// Explanation: The root is x = -1

// Example 3:
// Input: a = 1, b = 0, c = 1
// Output: []
// Explanation: Discriminant is negative, no real roots

// Function Signature:
// def solve_quadratic(a: float, b: float, c: float) -> list[float]:

// define a function solvesForQuadratic() takes 3 parameters a, b, and c
// def solvesForQuadratic(a, b, c):
//    create a variable discriminant and set = to the formula (b * b) - (4 * a * c)
//    discriminant = (b * b) - (4 * a * c)
//    use an if statement to check if the discriminant is > 0
//    if discriminant > 0:
//        root1 = (-b + math.sqrt((b * b) - (4 * a * c))) / (2 * a)
//        root2 = (-b - math.sqrt((b * b) - (4 * a * c))) / (2 * a)
//        return [root1, root2]
//    elif discriminant == 0:
//        realRt = -b / (2 * a)
//        return [realRt]
//    else:
//        return []


public class cc5 {
    public static void main(String[] args) {
        float[] roots = solvesForQuadratic(1, 2,1);
        for (int i = 0; i < roots.length; i++) {
            System.out.println(roots[i]);
        }
    }
    public static float[] solvesForQuadratic(float a, float b, float c) {
        float[] roots = new float[2];
        float discriminant = (b * b) - (4 * a * c);
        if (discriminant > 0 ) {
            roots[0] = (float) (-b + Math.sqrt((b * b) - (4 * a * c))) / (2 * a);
            roots[1] = (float) (-b - Math.sqrt((b * b) - (4 * a * c))) / (2 * a);
            return roots;
        } else if (discriminant == 0) {
            roots[0] = -b / (2 * a);
            return roots;
        } else {
            return roots;
        }
    }
}

// double myDouble = 123.456;
// float myFloat = (float) myDouble; 