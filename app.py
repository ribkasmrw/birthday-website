from flask import Flask, render_template
import os

app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
app.config['UPLOAD_FOLDER'] = os.path.join(BASE_DIR, 'static', 'uploads')

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp', 'mp4', 'mov', 'avi', 'mkv', 'webm'}

# ============================================================
# ✏️  SESUAIKAN INI DENGAN NAMA & PESAN KAMU
# ============================================================
CONFIG = {
    "nama_pacar": "Jonaaaa",            # Ganti nama pacar kamu
    "nama_pengirim": "sayangmu",      # Ganti namamu
    "tanggal_ultah": "13 Mei",        # Ganti tanggal ulang tahunnya
    "pesan_utama": "Happy Birthday, my love beiii! 🎂",
    "pesan_panjang": (
        "Selamat ulang tahun ma beii, panjang umur, sehat selalu!!. "
        "Di hari yang sangat spesial ini, ika ingin kamu selalu ingat setiap momen' kitaa. "
        "setiap momen bersamamu adalah hadiah terindah dalam hidupku eaa. "
        "Semoga hari ini dan seterusnya dipenuhi kebahagiaan, tawa bersama keluarga dan ikaa <3. "
        "Apa yang menjadi keinginanmu semoga bisa tercapai. "
        "Aku cinta kamu selalu. 💖"
    ),
}
# ============================================================

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def is_video(filename):
    return filename.rsplit('.', 1)[1].lower() in {'mp4', 'mov', 'avi', 'mkv', 'webm'}

@app.route('/')
def index():
    # Get all uploaded files
    upload_folder = app.config['UPLOAD_FOLDER']
    media_files = []
    if os.path.exists(upload_folder):
        for filename in sorted(os.listdir(upload_folder)):
            if allowed_file(filename):
                media_files.append({
                    'filename': filename,
                    'is_video': is_video(filename),
                    'url': f'/static/uploads/{filename}'
                })
    return render_template('index.html', config=CONFIG, media_files=media_files)

if __name__ == '__main__':
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    print("\n🎂 ========================================")
    print("   Birthday Website sudah berjalan!")
    print("   Buka browser: http://localhost:5000")
    print("========================================\n")
    app.run(debug=True, host='0.0.0.0', port=5000)
