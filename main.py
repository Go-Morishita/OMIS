# 青山学院大学 理工学部 情報テクノロジー学科
# Go Morishita
# Optimal Multiple Importance Sampling の実装と他のヒューリスティックとの比較

import numpy as np

from config import *
from sampling_methods import calculate_balance_weights, calculate_power_weights, calculate_optimal_weights
from plotting import plot_graphs

for i in range(n):
    num_p1 += f(x_random_p1[i]) / normalization_p1(x_random_p1[i])
    estimated_value_p1 = num_p1 / (i + 1)
    convergent_process_p1.append(estimated_value_p1)  # 収束過程の値を追加

    num_p2 += f(x_random_p2[i]) / normalization_p2(x_random_p2[i])
    estimated_value_p2 = num_p2 / (i + 1)
    convergent_process_p2.append(estimated_value_p2)  # 収束過程の値を追加

    num_p3 += f(x_random_p3[i]) / p3(x_random_p3[i])
    estimated_value_p3 = num_p3 / (i + 1)
    convergent_process_p3.append(estimated_value_p3)  # 収束過程の値を追加

    # バランスヒューリスティック
    balance_weight = calculate_balance_weights(
        normalization_p1, normalization_p2, p3, x_random_p1[i], x_random_p2[i], x_random_p3[i], N)

    tmp_balance = (f(x_random_p1[i]) / normalization_p1(x_random_p1[i])) * balance_weight[0] + (f(x_random_p2[i]) /
                                                                                                normalization_p2(x_random_p2[i])) * balance_weight[1] + (f(x_random_p3[i]) / p3(x_random_p3[i])) * balance_weight[2]

    num_balance += tmp_balance

    # 分散計算のため
    estimated_values_balance.append(tmp_balance)

    estimated_value_balance = num_balance / (i + 1)
    convergent_process_balance.append(estimated_value_balance)  # 収束過程の値を追加

    # パワーヒューリスティック
    power_weight = calculate_power_weights(
        normalization_p1, normalization_p2, p3, x_random_p1[i], x_random_p2[i], x_random_p3[i], N)

    tmp_power = (f(x_random_p1[i]) / normalization_p1(x_random_p1[i])) * power_weight[0] + (f(x_random_p2[i]) /
                                                                                            normalization_p2(x_random_p2[i])) * power_weight[1] + (f(x_random_p3[i]) / p3(x_random_p3[i])) * power_weight[2]

    num_power += tmp_power

    # 分散計算のため
    estimated_values_power.append(tmp_power)

    estimated_value_power = num_power / (i + 1)
    convergent_process_power.append(estimated_value_power)  # 収束過程の値を追加

    # オプティマルヒューリスティック
    optimal_weight = calculate_optimal_weights(
        f, normalization_p1, normalization_p2, p3, x_random_p1[i], x_random_p2[i], x_random_p3[i], N, x_range[0], x_range[1], division)

    tmp_optimal = (f(x_random_p1[i]) / normalization_p1(x_random_p1[i])) * optimal_weight[0] + (f(x_random_p2[i]) /
                                                                                                normalization_p2(x_random_p2[i])) * optimal_weight[1] + (f(x_random_p3[i]) / p3(x_random_p3[i])) * optimal_weight[2]

    num_optimal += tmp_optimal

    # 分散計算のため
    estimated_values_optimal.append(tmp_optimal)

    estimated_value_optimal = num_optimal / (i + 1)
    convergent_process_optimal.append(estimated_value_optimal)  # 収束過程の値を追加

# 分散を計算

variance_balance = np.mean([(x - 1.0)**2 for x in estimated_values_balance])
variance_power = np.mean([(x - 1.0)**2 for x in estimated_values_power])
variance_optimal = np.mean([(x - 1.0)**2 for x in estimated_values_optimal])

# 分散計算はf/pの1.0周りの分散

print("target value: 1.0")
print("p1:" + str(estimated_value_p1))
print("p2:" + str(estimated_value_p2))
print("p3:" + str(estimated_value_p3))
print("balance:" + str(estimated_value_balance))
print("power:" + str(estimated_value_power))
print("optimal:" + str(estimated_value_optimal))

print("balance variance:" + str(variance_balance))
print("power variance:" + str(variance_power))
print("optimal variance:" + str(variance_optimal))

##########################################################

# バランスヒューリスティック重みの描画

for i in range(division):

    x = x_range[0] + i * (x_range[1] - x_range[0]) / division

    balance_weight = calculate_balance_weights(
        normalization_p1, normalization_p2, p3, x, x, x, N)

    balance_weight_process_p1.append(balance_weight[0])
    balance_weight_process_p2.append(balance_weight[1])
    balance_weight_process_p3.append(balance_weight[2])


##########################################################

# パワーヒューリスティック重みの描画

for i in range(division):

    x = x_range[0] + i * (x_range[1] - x_range[0]) / division

    power_weight = calculate_power_weights(
        normalization_p1, normalization_p2, p3, x, x, x, N)

    power_weight_process_p1.append(power_weight[0])
    power_weight_process_p2.append(power_weight[1])
    power_weight_process_p3.append(power_weight[2])


##########################################################

# オプティマルヒューリスティック重みの描画

for i in range(division):

    x = x_range[0] + i * (x_range[1] - x_range[0]) / division

    optimal_weight = calculate_optimal_weights(f,
                                               normalization_p1, normalization_p2, p3, x, x, x, N, x_range[0], x_range[1], division)

    optimal_weight_process_p1.append(optimal_weight[0])
    optimal_weight_process_p2.append(optimal_weight[1])
    optimal_weight_process_p3.append(optimal_weight[2])

balance_weight_process = [balance_weight_process_p1,
                          balance_weight_process_p2, balance_weight_process_p3]

power_weight_process = [power_weight_process_p1,
                        power_weight_process_p2, power_weight_process_p3]

optimal_weight_process = [optimal_weight_process_p1,
                          optimal_weight_process_p2, optimal_weight_process_p3]

convergent_process = [convergent_process_balance,
                      convergent_process_power, convergent_process_optimal]

plot_graphs(n, x_range[0], x_range[1], step, y_range[0], y_range[1],
            f, normalization_p1, normalization_p2, p3, balance_weight_process, power_weight_process, optimal_weight_process, convergent_process)
