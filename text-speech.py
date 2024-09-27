import os
from gtts import gTTS
from googletrans import Translator

class TextToSpeechTranslator:
    def __init__(self):
        self.translator = Translator()

    def translate_text(self, text, dest_language):
        try:
            translation = self.translator.translate(text, dest=dest_language)
            return translation.text
        except Exception as e:
            print(f"Terjadi kesalahan saat menerjemahkan: {e}")
            return None

    def text_to_speech(self, text, language, output_file):
        try:
            tts = gTTS(text=text, lang=language, slow=False)
            tts.save(output_file)
            print(f"File audio berhasil disimpan: {output_file}")
        except Exception as e:
            print(f"Terjadi kesalahan saat mengonversi teks ke ucapan: {e}")

def get_input(prompt):
    print(prompt)
    return input()

def main():
    converter = TextToSpeechTranslator()

    while True:
        print("\n=== Aplikasi Konversi Teks ke Ucapan dengan Penerjemahan ===")
        text = get_input("Masukkan teks (atau 'keluar' untuk mengakhiri): ")
        
        if text.lower() == 'keluar':
            break

        src_lang = get_input("Masukkan kode bahasa sumber (mis. 'en' untuk Inggris, 'id' untuk Indonesia): ")
        dest_lang = get_input("Masukkan kode bahasa tujuan: ")
        
        translated_text = converter.translate_text(text, dest_lang)
        if translated_text:
            print(f"\nTeks yang diterjemahkan: {translated_text}")
            
            output_file = f"output_{dest_lang}.mp3"
            converter.text_to_speech(translated_text, dest_lang, output_file)
        
        print("\n" + "="*60)

if __name__ == "__main__":
    main()