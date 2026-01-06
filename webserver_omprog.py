import sys
import datetime
def main():
    log_file = '/var/log/omprog.log'
    try:
        message = sys.stdin.readline().strip()
        if message:
            timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            with open(log_file, 'a') as f:
                f.write(f"[{timestamp}] {message}\n")
    except Exception as e:
        with open('/tmp/omprog_error.log', 'a') as f:
            f.write(f"[{timestamp}] Error: {str(e)}\n")
if __name__ == '__main__':
    main()
