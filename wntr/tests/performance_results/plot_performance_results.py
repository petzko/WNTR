import performance_results as res
import matplotlib.pyplot as plt

plt.subplot(3,3,1)
plt.plot(range(len(res.Net1_total_sim_time)),res.Net1_total_sim_time)
plt.ylabel('Total sim time')
plt.title('Net1')
plt.subplot(3,3,2)
plt.plot(range(len(res.Net3_total_sim_time)),res.Net3_total_sim_time)
plt.title('Net3')
plt.subplot(3,3,3)
plt.plot(range(len(res.Net6_mod_total_sim_time)),res.Net6_mod_total_sim_time)
plt.title('Net6_mod')
plt.subplot(3,3,4)
plt.plot(range(len(res.Net1_time_per_step)),res.Net1_time_per_step)
plt.ylabel('Time per step')
plt.gcf().subplots_adjust(left=0.4)
plt.subplot(3,3,5)
plt.plot(range(len(res.Net3_time_per_step)),res.Net3_time_per_step)
plt.gcf().subplots_adjust(left=0.4)
plt.subplot(3,3,6)
plt.plot(range(len(res.Net6_mod_time_per_step)),res.Net6_mod_time_per_step)
plt.gcf().subplots_adjust(left=0.4)
plt.subplot(3,3,7)
plt.plot(range(len(res.Net1_num_steps)),res.Net1_num_steps)
plt.ylabel('# of steps')
plt.gcf().subplots_adjust(left=0.1)
plt.subplot(3,3,8)
plt.plot(range(len(res.Net3_num_steps)),res.Net3_num_steps)
plt.gcf().subplots_adjust(left=0.1)
plt.subplot(3,3,9)
plt.plot(range(len(res.Net6_mod_num_steps)),res.Net6_mod_num_steps)
plt.gcf().subplots_adjust(left=0.1)
plt.savefig('performance_results_plot.pdf',format='pdf')
plt.close()

plt.subplot(3,3,1)
plt.plot(range(len(res.Net1_avg_head_diff)),res.Net1_avg_head_diff)
plt.ylabel('Avg head diff')
plt.ylim(0,0.001)
plt.title('Net1')
plt.subplot(3,3,2)
plt.plot(range(len(res.Net3_avg_head_diff)),res.Net3_avg_head_diff)
plt.ylim(0,0.001)
plt.title('Net3')
plt.subplot(3,3,3)
plt.plot(range(len(res.Net6_mod_avg_head_diff)),res.Net6_mod_avg_head_diff)
plt.ylim(0,0.1)
plt.title('Net6_mod')
plt.subplot(3,3,4)
plt.plot(range(len(res.Net1_avg_demand_diff)),res.Net1_avg_demand_diff)
plt.ylabel('Avg demand diff')
plt.ylim(0,0.00001)
plt.gcf().subplots_adjust(left=0.4)
plt.subplot(3,3,5)
plt.plot(range(len(res.Net3_avg_demand_diff)),res.Net3_avg_demand_diff)
plt.ylim(0,0.00001)
plt.gcf().subplots_adjust(left=0.4)
plt.subplot(3,3,6)
plt.plot(range(len(res.Net6_mod_avg_demand_diff)),res.Net6_mod_avg_demand_diff)
plt.ylim(0,0.001)
plt.gcf().subplots_adjust(left=0.4)
plt.subplot(3,3,7)
plt.plot(range(len(res.Net1_avg_flow_diff)),res.Net1_avg_flow_diff)
plt.ylabel('Avg flow diff')
plt.ylim(0,0.00001)
plt.gcf().subplots_adjust(left=0.1)
plt.subplot(3,3,8)
plt.plot(range(len(res.Net3_avg_flow_diff)),res.Net3_avg_flow_diff)
plt.ylim(0,0.00001)
plt.gcf().subplots_adjust(left=0.1)
plt.subplot(3,3,9)
plt.plot(range(len(res.Net6_mod_avg_flow_diff)),res.Net6_mod_avg_flow_diff)
plt.ylim(0,0.001)
plt.gcf().subplots_adjust(left=0.1)
plt.savefig('performance_results_plot2.pdf',format='pdf')
plt.close()

plt.subplot(3,3,1)
plt.plot(range(len(res.Net1_head_diff_std_dev)),res.Net1_head_diff_std_dev)
plt.ylabel('head diff std_dev')
plt.ylim(0,0.001)
plt.title('Net1')
plt.subplot(3,3,2)
plt.plot(range(len(res.Net3_head_diff_std_dev)),res.Net3_head_diff_std_dev)
plt.ylim(0,0.001)
plt.title('Net3')
plt.subplot(3,3,3)
plt.plot(range(len(res.Net6_mod_head_diff_std_dev)),res.Net6_mod_head_diff_std_dev)
plt.ylim(0,0.1)
plt.title('Net6_mod')
plt.subplot(3,3,4)
plt.plot(range(len(res.Net1_demand_diff_std_dev)),res.Net1_demand_diff_std_dev)
plt.ylabel('demand diff std_dev')
plt.ylim(0,0.00001)
plt.gcf().subplots_adjust(left=0.4)
plt.subplot(3,3,5)
plt.plot(range(len(res.Net3_demand_diff_std_dev)),res.Net3_demand_diff_std_dev)
plt.ylim(0,0.00001)
plt.gcf().subplots_adjust(left=0.4)
plt.subplot(3,3,6)
plt.plot(range(len(res.Net6_mod_demand_diff_std_dev)),res.Net6_mod_demand_diff_std_dev)
plt.ylim(0,0.1)
plt.gcf().subplots_adjust(left=0.4)
plt.subplot(3,3,7)
plt.plot(range(len(res.Net1_flow_diff_std_dev)),res.Net1_flow_diff_std_dev)
plt.ylabel('flow diff std_dev')
plt.ylim(0,0.00001)
plt.gcf().subplots_adjust(left=0.1)
plt.subplot(3,3,8)
plt.plot(range(len(res.Net3_flow_diff_std_dev)),res.Net3_flow_diff_std_dev)
plt.ylim(0,0.00001)
plt.gcf().subplots_adjust(left=0.1)
plt.subplot(3,3,9)
plt.plot(range(len(res.Net6_mod_flow_diff_std_dev)),res.Net6_mod_flow_diff_std_dev)
plt.ylim(0,0.1)
plt.gcf().subplots_adjust(left=0.1)
plt.savefig('performance_results_plot3.pdf',format='pdf')
plt.close()