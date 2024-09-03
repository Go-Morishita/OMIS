import numpy as np

# 関数の内積は区分求積法で行う


def dot_function(func1, func2, start, end, div):
    x = np.linspace(start, end, div)
    y = func1(x) * func2(x)
    return np.trapz(y, x)


def A_matrix(techniques_num, x, p1, p2, p3, start, stop, div):
    A = np.zeros((techniques_num, techniques_num))
    p_funcs = [p1, p2, p3]

    denominator = sum(p_funcs[j](x) for j in range(techniques_num))

    for i in range(techniques_num):
        for k in range(techniques_num):
            A[i, k] = dot_function(lambda x: p_funcs[i](x),
                                   lambda x: (p_funcs[k](x) / denominator),
                                   start, stop, div)
    return A


def b_vector(techniques_num, x, f, p1, p2, p3, start, end, div):
    b = np.zeros((techniques_num))
    p_funcs = [p1, p2, p3]

    denominator = sum(p_funcs[j](x) for j in range(techniques_num))

    for i in range(techniques_num):
        b[i] = dot_function(lambda x: f(x), lambda x: (p_funcs[i](x) / denominator),
                            start, end, div)

    return b


def calculate_optimal_weights(f, p1, p2, p3, x_random_p1, x_random_p2, x_random_p3, techniques_num, start, end, div):
    x_random = [x_random_p1, x_random_p2, x_random_p3]
    p_funcs = [p1, p2, p3]
    optimal_weight = []

    for i in range(techniques_num):

        alpha = np.linalg.solve(
            A_matrix(techniques_num, x_random[i], p1, p2, p3, start, end, div),
            b_vector(techniques_num, x_random[i], f, p1, p2, p3, start, end, div))

        term_1 = alpha[i] * p_funcs[i](x_random[i]) / f(x_random[i])

        term_2_1 = p_funcs[i](x_random[i]) / \
            sum(p_funcs[j](x_random[i]) for j in range(techniques_num))

        term_2_2 = 1 - sum(alpha[j] * p_funcs[j](x_random[i])
                           for j in range(techniques_num)) / f(x_random[i])

        optimal_weight.append(term_1 + term_2_1 * term_2_2)

    return optimal_weight
