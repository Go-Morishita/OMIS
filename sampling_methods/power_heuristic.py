def calculate_power_weights(p1, p2, p3, x_random_p1, x_random_p2, x_random_p3, techniques_num):

    x_random = [x_random_p1, x_random_p2, x_random_p3]

    for i in range(techniques_num):
        denominator = pow(p1(
            x_random[i]), 2) + pow(p2(x_random[i]), 2) + pow(p3(x_random[i]), 2)

        if (i == 0):
            power_weight_p1 = pow(p1(
                x_random[i]), 2) / denominator
        if (i == 1):
            power_weight_p2 = pow(p2(
                x_random[i]), 2) / denominator
        if (i == 2):
            power_weight_p3 = pow(p3(x_random[i]), 2) / denominator

    power_weight = [power_weight_p1, power_weight_p2, power_weight_p3]

    return power_weight
