import http.server
import socketserver
import os

# Konfigurasi
PORT = 8000
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)
    
    def end_headers(self):
        # Tambahkan header untuk cache control
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        self.send_header('Expires', '0')
        super().end_headers()

    def log_message(self, format, *args):
        # Custom log format
        print(f"[{self.log_date_time_string()}] {format % args}")

def run_server():
    """Menjalankan HTTP server"""
    handler = MyHTTPRequestHandler
    
    with socketserver.TCPServer(("", PORT), handler) as httpd:
        print("=" * 60)
        print("🚀 Server Mesin Turing - Konversi Huruf ke Biner")
        print("=" * 60)
        print(f"📂 Directory: {DIRECTORY}")
        print(f"🌐 Server berjalan di: http://localhost:{PORT}")
        print(f"🌐 Atau akses via: http://127.0.0.1:{PORT}")
        print("=" * 60)
        print("✅ Server aktif! Tekan CTRL+C untuk menghentikan server")
        print("=" * 60)
        print()
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n")
            print("=" * 60)
            print("🛑 Server dihentikan oleh user")
            print("=" * 60)
            httpd.shutdown()

if __name__ == "__main__":
    run_server()