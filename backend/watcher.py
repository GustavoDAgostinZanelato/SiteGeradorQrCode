import time
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class WatcherHandler(FileSystemEventHandler):
    def __init__(self):
        self.process = None
        self.restart()

    def restart(self):
        if self.process:
            self.process.terminate()
        self.process = subprocess.Popen(["python", "app.py"])

    def on_any_event(self, event):
        if event.src_path.endswith(".py"):
            print(f"\n🔄 Mudança detectada em: {event.src_path}")
            self.restart()

if __name__ == "__main__":
    path = "."  # monitora a própria pasta backend
    event_handler = WatcherHandler()
    observer = Observer()
    observer.schedule(event_handler, path=path, recursive=True)
    observer.start()

    print("👀 Watchdog está monitorando alterações em arquivos .py...")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("🛑 Watchdog encerrado.")

    observer.join()
