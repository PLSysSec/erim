# Set IRQ affinity mask to CPU 0
cd /proc/irq/
echo 1 | tee */smp_affinity

# CPU Frequency
cd /sys/devices/system/cpu/
echo performance | tee cpu*/cpufreq/scaling_governor
echo 3510000 | tee cpu*/cpufreq/scaling_max_freq
echo 3500000 | tee cpu*/cpufreq/scaling_min_freq

