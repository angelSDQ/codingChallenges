/*
 * LeetCode-style Problem (Easy-Medium): Find the Vertex and Type of a Quadratic
 * Equation
 * Given three real numbers `a`, `b`, and `c` representing the coefficients of a
 * quadratic equation: f(x) = ax² + bx + c
 * Return a **single string** in the format: "Vertex: (x, y), Type: minimum" or
 * "Vertex: (x, y), Type: maximum"
 * 
 * Where:
 * - `x` is the x-coordinate of the vertex, calculated as x = -b / (2a)
 * - `y` is the value of the function at x: y = a * x² + b * x + c
 * - Both `x` and `y` are rounded to **2 decimal places**
 * - "minimum" if a > 0, "maximum" if a < 0
 * 
 * Parameters:
 * a (float): Coefficient of x² (a ≠ 0)
 * b (float): Coefficient of x
 * c (float): Constant term
 * 
 * Returns:
 * str: The result string formatted as described
 * 
 * Examples:
 * >>> find_vertex(1, -2, 1)
 * 'Vertex: (1.0, 0.0), Type: minimum'
 * 
 * >>> find_vertex(-2, 4, 6)
 * 'Vertex: (1.0, 8.0), Type: maximum'
 * 
 * >>> find_vertex(-1, 0, 0)
 * 'Vertex: (0.0, 0.0), Type: maximum'
 */

// declare a public class cc7 {
//  Inside a the class cc7 declare main method
//  public static void main(String[] args) {
//      Inside the main method call your function vertexAndQuadraticType() passing in 3 parameters a, b, and c values
//      System.out.println(vertexAndQuadraticType(1, -2, 1));
//   
//  
//  declare vertexAndQuadraticType() method and passing in 3 parameters a, b, and, c DONT FORGET return type
//  public static String vertexAndQuadraticType(a, b, c) {
//      inside vertexAndQuadraticType() method declare variables x, y, and minOrMaxType DONT FORGET to add return type
//      float x = -b / (2 * a);
//      float y = a * (x * x) + b * x + c;
//      set minOrMaxType to an empty string
//      String minOrMaxType = "";
//      use an if statement to check the condition a > 0 to set the minOrMaxType 
//      if (a > 0) {
//          minOrMaxType = "minimum";
//      } else {
//          minOrMaxType = "maximum";
//      }
//      return "Vertex: (" + x + ", " + y "), Type: + minOrMaxType";   
//  }
//}
public class cc7 {
    public static void main(String[] args) {
        System.out.println(vertexAndQuadraticType(1, -2, 1));
    }
    public static String vertexAndQuadraticType(float a, float b, float c) {
        float x = -b / (2 * a);
        float y = a * (x * x) + b * x + c;
        String minOrMaxType = "";
        if (a > 0) {
            minOrMaxType = "minimum";
        } else {
            minOrMaxType = "maximum";
        }
        return "Vertex: (" + x + ", " + y + "), Type: " + minOrMaxType;  
    }
}

