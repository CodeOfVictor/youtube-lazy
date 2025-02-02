import os
import re
import subprocess
from gpt4all import GPT4All

# Downloads YouTube subtitles in .vtt format (hiding yt-dlp logs)
def download_subtitles(video_url, lang="es"):
    command = [
        "yt-dlp",
        "--skip-download",
        "--write-auto-sub",
        "--sub-lang", lang,
        "--sub-format", "vtt",
        "-o", "subtitles",
        video_url
    ]
    subprocess.run(command, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


# Cleans a .vtt file and returns only the text without duplicates or unnecessary tags
def clean_subtitles(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.readlines()

    clean_lines = []
    seen_lines = set()  # To remove duplicate lines

    for line in content:
        line = line.strip()  # Remove extra spaces

        # Filter out unnecessary text and headers
        if not line or "align:start" in line or "position:" in line or "Kind: captions" in line:
            continue
        if line.startswith("WEBVTT") or line.startswith("Language:"):
            continue

        # Remove HTML tags and timestamps
        line = re.sub(r'<[^>]+>', '', line)
        line = re.sub(r'\d{2}:\d{2}:\d{2}\.\d{3} --> \d{2}:\d{2}:\d{2}\.\d{3}', '', line)

        if line not in seen_lines:
            seen_lines.add(line)
            clean_lines.append(line)

    return "\n".join(clean_lines)


# Splits text into smaller chunks (to fit model token limit)
def split_text(text, max_tokens=1500):
    words = text.split()
    chunks = []
    current_chunk = []

    for word in words:
        if len(current_chunk) + len(word) > max_tokens:
            chunks.append(" ".join(current_chunk))
            current_chunk = []
        current_chunk.append(word)

    if current_chunk:
        chunks.append(" ".join(current_chunk))

    return chunks


# Summarizes text using GPT4All
def summarize_text(model, text):
    # Split subtitles into smaller chunks
    text_chunks = split_text(text)

    summary_parts = []
    for i, chunk in enumerate(text_chunks):
        print(f"🔹 Resumiendo parte {i + 1}/{len(text_chunks)}...")
        response = model.generate(f"Resume este texto manteniendo la coherencia con partes anteriores:\n{chunk}")
        summary_parts.append(response)

    # Generate final summary from all partial summaries
    final_summary_prompt = "Aquí tienes varias partes resumidas de un texto más largo. Une toda la información en un único resumen coherente y conciso:\n" + "\n".join(
        summary_parts)
    final_summary = model.generate(final_summary_prompt)

    return final_summary


# Downloads, cleans, and summarizes subtitles
def get_subtitles(video_url):
    try:
        download_subtitles(video_url)
        subtitles_file = "subtitles.es.vtt"
        if not os.path.exists(subtitles_file):
            print("❌ No subtitles found.")
            return None

        subtitles = clean_subtitles(subtitles_file)
        os.remove(subtitles_file)

        return subtitles

    except Exception as e:
        print(f"❌ Error: {e}")
        return None


# --- EXECUTION ---
if __name__ == "__main__":
    print("Loading AI model...")
    model = GPT4All("Llama-3.2-3B-Instruct-Q4_0.gguf", device="gpu")

    video_url = input("🎥 Enter YouTube video URL: ")
    print("Getting subtitles from the video...")
    subtitles = get_subtitles(video_url)

    if subtitles:
        print("🔹 Processing subtitles for summary...")
        summary = summarize_text(model, subtitles)
        print("\n--- FINAL SUMMARY ---\n")
        print(summary)
