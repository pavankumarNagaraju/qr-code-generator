import qrcode
import argparse
import os

def generate_qr(url):
    # Ensure output directory exists
    output_dir = "qr_codes"
    os.makedirs(output_dir, exist_ok=True)

    # File name from domain
    file_name = url.replace("http://", "").replace("https://", "").replace("/", "_") + ".png"
    output_path = os.path.join(output_dir, file_name)

    # Generate QR code
    img = qrcode.make(url)
    img.save(output_path)

    print(f"[INFO] QR code generated and saved at: {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple QR Code Generator")
    parser.add_argument("--url", type=str, default="http://github.com/kaw393939", help="URL to encode in the QR code")
    args = parser.parse_args()
    generate_qr(args.url)
