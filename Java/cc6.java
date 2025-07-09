package Java;

// LeetCode-style Problem: Find the Vertex of a Quadratic Equation
//     Given three real numbers a, b, and c representing the coefficients of a quadratic equation:
//         f(x) = ax² + bx + c

//     Return the vertex of the parabola as a list [x, y], where:
//         - x is the x-coordinate of the vertex, calculated as x = -b / (2a)
//         - y is the value of the function at x: y = a * x² + b * x + c

//     Parameters:
//         a (float): Coefficient of x² (a ≠ 0)
//         b (float): Coefficient of x
//         c (float): Constant term

//     Returns:
//         list[float]: The coordinates [x, y] of the vertex

//     Examples:
//         >>> find_vertex(1, -2, 1)
//         [1.0, 0.0]

//         >>> find_vertex(2, -4, -6)
//         [1.0, -8.0]

//         >>> find_vertex(-1, 0, 0)
//         [0.0, 0.0]

public class cc6 {
    public static void main(String[] args) {
        float[] vertex = findVertex(1, 2,1);
        for (int i = 0; i < vertex.length; i++) {
            System.out.println(vertex[i]);
        }
}
    public static float[] findVertex(float a, float b, float c) {
        //create a float array with 2 empty seats
        float[] vertex = new float[2];
        // find x based on the formula below
        float x = -b / (2 * a);
        // find y based on the formula below
        float y = (a * (x * x) + (b * x) + c);
        // set my 1st empty array seat to x
        vertex[0] = x;
        // set my 2nd empty array seat to y
        vertex[1] = y;
        // return my float array
        return vertex;
    }
}

// def findVertex(a, b, c):
//     x = -b / (2 * a)
//     y = (a * (x * x) + (b * x) + c)
//     return [x,y]