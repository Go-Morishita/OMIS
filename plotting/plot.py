import numpy as np
import matplotlib.pyplot as plt


def plot_graphs(n, x_start, x_end, step, y_start, y_end, f, p1, p2, p3, balance_weight_process, power_weight_process, optimal_weight_process, convergent_process):
    # グラフの描画
    fig, axes = plt.subplots(1, 5, figsize=(15, 3))
    (ax1, ax2, ax3, ax4, ax5) = axes
    # 関数の描画（一段目）
    x = np.arange(x_start, x_end, step)
    ax1.plot(x, f(x), label='f', color='black')
    ax1.plot(x, p1(x), label='p1', color='orange')
    ax1.plot(x, p2(x), label='p2', color='skyblue')
    ax1.plot(x, p3(x), label='p3', color='green')

    ax1.set_title('a) integrand and sampling techniques')
    ax1.set_xlim(x_start, x_end)  # x軸の範囲
    ax1.set_ylim(y_start, y_end)  # y軸の範囲（少し余裕を持たせる）
    ax1.legend()
    ax1.grid(True)  # グリッドを表示

    # バランスヒューリスティック重みの描画（一段目）
    x = np.arange(x_start, x_end, step)
    ax2.plot(x, balance_weight_process[0], label='p1', color='orange')
    ax2.plot(x, balance_weight_process[1], label='p2', color='skyblue')
    ax2.plot(x, balance_weight_process[2], label='p3', color='green')
    ax2.set_title('b) Balance heuristic weights')
    ax2.set_xlim(x_start, x_end)  # x軸の範囲
    ax2.set_ylim(0, 1)  # y軸の範囲
    ax2.set_xlabel('Iterations')
    ax2.set_ylabel('Weights Value')
    ax2.legend()
    ax2.grid(True)  # グリッドを表示

    # パワーヒューリスティック重みの描画（一段目）
    x = np.arange(x_start, x_end, step)
    ax3.plot(x, power_weight_process[0], label='p1', color='orange')
    ax3.plot(x, power_weight_process[1], label='p2', color='skyblue')
    ax3.plot(x, power_weight_process[2], label='p3', color='green')
    ax3.set_title('c) Power heuristic weights')
    ax3.set_xlim(x_start, x_end)  # x軸の範囲
    ax3.set_ylim(0, 1)  # y軸の範囲
    ax3.set_xlabel('Iterations')
    ax3.set_ylabel('Weights Value')
    ax3.legend()
    ax3.grid(True)  # グリッドを表示

    # オプティマルヒューリスティック重みの描画（一段目）
    x = np.arange(x_start, x_end, step)
    ax4.plot(x, optimal_weight_process[0], label='p1', color='orange')
    ax4.plot(x, optimal_weight_process[1], label='p2', color='skyblue')
    ax4.plot(x, optimal_weight_process[2], label='p3', color='green')
    ax4.set_title('d) Optimal heuristic weights')
    ax4.set_xlim(x_start, x_end)  # x軸の範囲
    ax4.set_ylim(-4, 4)  # y軸の範囲
    ax4.set_xlabel('Iterations')
    ax4.set_ylabel('Weights Value')
    ax4.legend()
    ax4.grid(True)  # グリッドを表示

    # 収束過程のモンテカルロ積分値の描画（一段目）
    # ax5.plot(convergent_process_p1, label='p1', color='orange')
    # ax5.plot(convergent_process_p2, label='p2', color='skyblue')
    # ax5.plot(convergent_process_p3, label='p3', color='green')
    ax5.plot(convergent_process[0], label='balance', color='red')
    ax5.plot(convergent_process[1], label='power', color='yellow')
    ax5.plot(convergent_process[2], label='optimal', color='blue')

    ax5.set_title('e) Convergence process')
    ax5.set_xlim(0, n)  # x軸の範囲
    ax5.set_xlabel('Iterations')
    ax5.set_ylabel('Estimated Value')
    ax5.legend()
    ax5.grid(True)  # グリッドを表示

    # # 関数の描画（二段目）
    # x = np.arange(x_start, x_end, step)
    # ax6.plot(x, f(x), label='f', color='black')
    # ax6.plot(x, p1(x), label='p1', color='orange')
    # ax6.plot(x, p2(x), label='p2', color='skyblue')
    # ax6.plot(x, p3(x), label='p3', color='green')

    # ax6.set_title('a) integrand and sampling techniques')
    # ax6.set_xlim(x_start, x_end)  # x軸の範囲
    # ax6.set_ylim(y_start, y_end)  # y軸の範囲（少し余裕を持たせる）
    # ax6.legx_end()
    # ax6.grid(True)  # グリッドを表示

    # # バランスヒューリスティック重みの描画（二段目）
    # x = np.arange(x_start, x_end, step)
    # ax7.plot(x, balance_weight_process_p1, label='p1', color='orange')
    # ax7.plot(x, balance_weight_process_p2, label='p2', color='skyblue')
    # ax7.plot(x, balance_weight_process_p3, label='p3', color='green')
    # ax7.set_title('b) Balance heuristic weights')
    # ax7.set_xlim(x_start, x_end)  # x軸の範囲
    # ax7.set_ylim(0, 1)  # y軸の範囲
    # ax7.set_xlabel('Iterations')
    # ax7.set_ylabel('Weights Value')
    # ax7.legx_end()
    # ax7.grid(True)  # グリッドを表示

    # # パワーヒューリスティック重みの描画（二段目）
    # x = np.arange(x_start, x_end, step)
    # ax8.plot(x, power_weight_process_p1, label='p1', color='orange')
    # ax8.plot(x, power_weight_process_p2, label='p2', color='skyblue')
    # ax8.plot(x, power_weight_process_p3, label='p3', color='green')
    # ax8.set_title('c) Power heuristic weights')
    # ax8.set_xlim(x_start, x_end)  # x軸の範囲
    # ax8.set_ylim(0, 1)  # y軸の範囲
    # ax8.set_xlabel('Iterations')
    # ax8.set_ylabel('Weights Value')
    # ax8.legx_end()
    # ax8.grid(True)  # グリッドを表示

    # # オプティマルヒューリスティック重みの描画（二段目）
    # x = np.arange(x_start, x_end, step)
    # ax9.plot(x, optimal_weight_process_p1, label='p1', color='orange')
    # ax9.plot(x, optimal_weight_process_p2, label='p2', color='skyblue')
    # ax9.plot(x, optimal_weight_process_p3, label='p3', color='green')
    # ax9.set_title('d) Optimal heuristic weights')
    # ax9.set_xlim(x_start, x_end)  # x軸の範囲
    # ax9.set_ylim(-4, 4)  # y軸の範囲
    # ax9.set_xlabel('Iterations')
    # ax9.set_ylabel('Weights Value')
    # ax9.legx_end()
    # ax9.grid(True)  # グリッドを表示

    # # 収束過程のモンテカルロ積分値の描画（二段目）
    # # ax10.plot(convergent_process_p1, label='p1', color='orange')
    # # ax10.plot(convergent_process_p2, label='p2', color='skyblue')
    # # ax10.plot(convergent_process_p3, label='p3', color='green')
    # ax10.plot(convergent_process_balance, label='balance', color='red')
    # ax10.plot(convergent_process_power, label='power', color='yellow')
    # ax10.plot(convergent_process_optimal, label='optimal', color='blue')

    # ax10.set_title('e) Convergence process')
    # ax10.set_xlim(0, n)  # x軸の範囲
    # ax10.set_xlabel('Iterations')
    # ax10.set_ylabel('Estimated Value')
    # ax10.legx_end()
    # ax10.grid(True)  # グリッドを表示

    plt.tight_layout()
    plt.show()
