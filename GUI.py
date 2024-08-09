import tkinter as tk
import psutil

def display_sysinfo():
    total_ram = psutil.virtual_memory().total // (1024 ** 2)  # Convert to MB
    free_ram = psutil.virtual_memory().free // (1024 ** 2)
    used_ram = psutil.virtual_memory().used // (1024 ** 2)
    total_swap = psutil.swap_memory().total // (1024 ** 2)
    free_swap = psutil.swap_memory().free // (1024 ** 2)
    used_swap = psutil.swap_memory().used // (1024 ** 2)

    sysinfo_text.set(f"System Information\n"
                     f"===================================\n"
                     f"Total RAM: {total_ram} MB\n"
                     f"Free RAM: {free_ram} MB\n"
                     f"Used RAM: {used_ram} MB\n"
                     f"Total Swap: {total_swap} MB\n"
                     f"Free Swap: {free_swap} MB\n"
                     f"Used Swap: {used_swap} MB\n")

def display_diskinfo():
    partitions = psutil.disk_partitions()
    disk_info_text = "Disk Usage Information\n" \
                     "===================================\n"
    for partition in partitions:
        disk_usage = psutil.disk_usage(partition.mountpoint)
        disk_info_text += f"{partition.device}:\n" \
                          f"Total: {disk_usage.total // (1024 ** 3)} GB\n" \
                          f"Used: {disk_usage.used // (1024 ** 3)} GB\n" \
                          f"Free: {disk_usage.free // (1024 ** 3)} GB\n" \
                          f"Percent Used: {disk_usage.percent}%\n\n"
    diskinfo_text.set(disk_info_text)

def monitor_memory_usage():
    memory_info = psutil.virtual_memory()
    used_memory_percent = memory_info.percent
    memory_usage_text.set(f"Memory Usage: {used_memory_percent}%")

def monitor_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)  # Measure CPU usage over 1 second
    cpu_usage_text.set(f"CPU Usage: {cpu_usage}%")

def monitor_network_usage():
    net_io_counters = psutil.net_io_counters()
    bytes_sent = net_io_counters.bytes_sent
    bytes_recv = net_io_counters.bytes_recv
    packets_sent = net_io_counters.packets_sent
    packets_recv = net_io_counters.packets_recv
    network_usage_text.set(f"Network Usage\n"
                           f"===================================\n"
                           f"Bytes Sent: {bytes_sent} bytes\n"
                           f"Bytes Received: {bytes_recv} bytes\n"
                           f"Packets Sent: {packets_sent}\n"
                           f"Packets Received: {packets_recv}\n")

def clear_output():
    sysinfo_text.set("")
    diskinfo_text.set("")
    memory_usage_text.set("")
    cpu_usage_text.set("")
    network_usage_text.set("")

root = tk.Tk()
root.title("System Monitoring Tool")
root.configure(bg="#205075")

sysinfo_text = tk.StringVar()
diskinfo_text = tk.StringVar()
memory_usage_text = tk.StringVar()
cpu_usage_text = tk.StringVar()
network_usage_text = tk.StringVar()

sysinfo_label = tk.Label(root, textvariable=sysinfo_text, justify="left", font=("Helvetica", 10))
diskinfo_label = tk.Label(root, textvariable=diskinfo_text, justify="left", font=("Helvetica", 10))
memory_usage_label = tk.Label(root, textvariable=memory_usage_text, justify="left", font=("Helvetica", 10))
cpu_usage_label = tk.Label(root, textvariable=cpu_usage_text, justify="left", font=("Helvetica", 10))
network_usage_label = tk.Label(root, textvariable=network_usage_text, justify="left", font=("Helvetica", 10))

sysinfo_label.grid(row=0, column=1, sticky="w", padx=10, pady=5)
diskinfo_label.grid(row=1, column=1, sticky="w", padx=10, pady=5)
memory_usage_label.grid(row=2, column=1, sticky="w", padx=10, pady=5)
cpu_usage_label.grid(row=3, column=1, sticky="w", padx=10, pady=5)
network_usage_label.grid(row=4, column=1, sticky="w", padx=10, pady=5)

clear_button = tk.Button(root, text="Clear Screen", font=("Helvetica", 10), fg="black", bg="#00ff40", borderwidth=6, command=clear_output)
clear_button.grid(row=5, column=0, sticky="w", padx=10, pady=5)

display_sysinfo_button = tk.Button(root, text="Display System Information", font=("Helvetica", 10), fg="black", bg="#00ff40", borderwidth=6, command=display_sysinfo)
display_sysinfo_button.grid(row=0, column=0, sticky="w", padx=10, pady=5)

display_diskinfo_button = tk.Button(root, text="Display Disk Information", font=("Helvetica", 10), fg="black", bg="#00ff40", borderwidth=6, command=display_diskinfo)
display_diskinfo_button.grid(row=1, column=0, sticky="w", padx=10, pady=5)

monitor_memory_usage_button = tk.Button(root, text="Monitor Memory Usage", font=("Helvetica", 10), fg="black", bg="#00ff40", borderwidth=6, command=monitor_memory_usage)
monitor_memory_usage_button.grid(row=2, column=0, sticky="w", padx=10, pady=5)

monitor_cpu_usage_button = tk.Button(root, text="Monitor CPU Usage", font=("Helvetica", 10), fg="black", bg="#00ff40", borderwidth=6, command=monitor_cpu_usage)
monitor_cpu_usage_button.grid(row=3, column=0, sticky="w", padx=10, pady=5)

monitor_network_usage_button = tk.Button(root, text="Monitor Network Usage", font=("Helvetica", 10), fg="black", bg="#00ff40", borderwidth=6, command=monitor_network_usage)
monitor_network_usage_button.grid(row=4, column=0, sticky="w", padx=10, pady=5)

root.mainloop()
