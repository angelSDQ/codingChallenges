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

function findVertex(a, b, c) {
    x = -b / (2 * a)
    y = (a * (x * x) + (b * x) + c)
    return [x, y]
}
console.log(findVertex(1, -2, 1))

