import numpy as np
from scipy.special import erf
from scipy.special import erfinv

x_range = [0, 4]  # x軸の範囲
y_range = [0, 1.8]  # y軸の範囲

division = 1000  # 分割数
step = (x_range[0] + x_range[1]) / division

n = 1000  # 試行回数

N = 3  # 手法の数

f_mu, f_sigma = 2, 0.5  # 被積分関数のパラメータ
p1_mu, p1_sigma = 0, 0.6  # 確率密度関数p1のパラメータ
p2_mu, p2_sigma = 2.1, 0.55  # 確率密度関数p2のパラメータ
# p2_mu, p2_sigma = 4, 0.6  # 確率密度関数p2のパラメータ


def f(x):
    return 1 / (f_sigma * np.sqrt(2 * np.pi)) * np.exp(- (x - f_mu)**2 / (2 * f_sigma**2))


def p1(x):
    return 1 / (p1_sigma * np.sqrt(2 * np.pi)) * np.exp(- (x - p1_mu)**2 / (2 * p1_sigma**2))


def p2(x):
    return 1 / (p2_sigma * np.sqrt(2 * np.pi)) * np.exp(- (x - p2_mu)**2 / (2 * p2_sigma**2))


def p3(x):
    return 0.25 * np.ones_like(x)


# p1の正規化定数
normalization_constant_p1 = 1 / (0.5 * (erf((x_range[1] - p1_mu) / (
    p1_sigma * np.sqrt(2))) - erf((x_range[0] - p1_mu) / (p1_sigma * np.sqrt(2)))))


# p2の正規化定数
normalization_constant_p2 = 1 / (0.5 * (erf((x_range[1] - p2_mu) / (
    p2_sigma * np.sqrt(2))) - erf((x_range[0] - p2_mu) / (p2_sigma * np.sqrt(2)))))

# 正規化されたNDF(p1)


def normalization_p1(x):
    return p1(x) * normalization_constant_p1

# 正規化されたNDF(p2)


def normalization_p2(x):
    return p2(x) * normalization_constant_p2


rand = np.random.uniform(-0.5, 0.5, n)

x_random_p1 = p1_mu + p1_sigma * np.sqrt(2) * erfinv(2 * rand)
x_random_p2 = p2_mu + p2_sigma * np.sqrt(2) * erfinv(2 * rand)
x_random_p3 = (rand + 0.5) * 4

estimated_value_p1 = 0  # モンテカルロ推定値
estimated_value_p2 = 0  # モンテカルロ推定値
estimated_value_p3 = 0  # モンテカルロ推定値
estimated_value_balance = 0  # モンテカルロ推定値
estimated_value_power = 0  # パワーヒューリスティック推定値


num_p1 = 0  # 計算用
num_p2 = 0  # 計算用
num_p3 = 0  # 計算用
num_balance = 0  # バランスヒューリスティックの計算用
num_power = 0  # パワーヒューリスティックの計算用
num_optimal = 0  # オプティマルヒューリスティックの計算用


convergent_process_p1 = []
convergent_process_p2 = []
convergent_process_p3 = []
convergent_process_balance = []
convergent_process_power = []
convergent_process_optimal = []

# バランスヒューリスティックの重み導出 ⇒ サンプルを引きながら変わっていくもの

balance_weight_process_p1 = []
balance_weight_process_p2 = []
balance_weight_process_p3 = []

# パワーヒューリスティックの重み導出 ⇒ サンプルを引きながら変わっていくもの

power_weight_process_p1 = []
power_weight_process_p2 = []
power_weight_process_p3 = []

# オプティマルヒューリスティックの重み導出 ⇒ サンプルを引きながら変わっていくもの

optimal_weight_process_p1 = []
optimal_weight_process_p2 = []
optimal_weight_process_p3 = []

# 分散を計算するための配列

estimated_values_p1 = []
estimated_values_p2 = []
estimated_values_p3 = []
estimated_values_balance = []
estimated_values_power = []
estimated_values_optimal = []
