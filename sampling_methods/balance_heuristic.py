def calculate_balance_weights(p1, p2, p3, x_random_p1, x_random_p2, x_random_p3, techniques_num):

    x_random = [x_random_p1, x_random_p2, x_random_p3]

    for i in range(techniques_num):
        denominator = p1(
            x_random[i]) + p2(x_random[i]) + p3(x_random[i])

        if (i == 0):
            balance_weight_p1 = (p1(x_random[i])) / denominator
        if (i == 1):
            balance_weight_p2 = (p2(x_random[i])) / denominator
        if (i == 2):
            balance_weight_p3 = (p3(x_random[i])) / denominator

    balance_weight = [balance_weight_p1, balance_weight_p2, balance_weight_p3]

    return balance_weight
