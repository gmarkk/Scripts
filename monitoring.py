import smtplib
import psutil

def get_disk_usage():
    total, used, free, percent = psutil.disk_usage('/')
    return percent

def get_memory_usage():
    mem = psutil.virtual_memory()
    percent = mem.percent
    return percent

def send_email_alert(subject, body):
    sender_email = "xx"
    receiver_email = "xx"
    password = "xx"

    disk_percent = get_disk_usage()
    memory_percent = get_memory_usage()

    message = f"Subject: {subject}\n\n{body}\nDisk Usage: {disk_percent}%\nMemory Usage: {memory_percent}%"

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

if __name__ == "__main__":
    disk_threshold = 80  # Set the disk usage threshold in percentage
    memory_threshold = 85  # Set the memory usage threshold in percentage

    disk_percent = get_disk_usage()
    memory_percent = get_memory_usage()

    print(f"Disk Usage: {disk_percent}%")
    print(f"Memory Usage: {memory_percent}%")

    if disk_percent >= disk_threshold:
        message = "Warning: High disk usage!"
        send_email_alert("Disk Usage Alert", message)

    if memory_percent >= memory_threshold:
        message = "Warning: High memory usage!"
        send_email_alert("Memory Usage Alert", message)
