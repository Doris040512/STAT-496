import os
import json
import time
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

BASE_URL = os.getenv("OPENAI_BASE_URL", "https://free.v36.cm/v1")
API_KEY = os.getenv("OPENAI_API_KEY")

if not API_KEY:
    raise RuntimeError("Missing OPENAI_API_KEY. Put it in .env as OPENAI_API_KEY=...")

client = OpenAI(api_key=API_KEY, base_url=BASE_URL)

BASE_DIR = Path(__file__).resolve().parent.parent
DOC_DIR = BASE_DIR / "Data" / "documents"
PROMPT_PATH = BASE_DIR / "prompts" / "extraction_prompt.txt"
TRUTH_PATH = BASE_DIR / "Truth" / "ground_truth.jsonl"
OUTPUT_DIR = BASE_DIR / "outputs" / "model_outputs"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

def load_truth():
    truth = {}
    with open(TRUTH_PATH, "r", encoding="utf-8") as f:
        for line in f:
            row = json.loads(line)
            truth[row["doc_id"]] = row
    return truth

def run():
    if not PROMPT_PATH.exists():
        raise FileNotFoundError(f"Prompt not found: {PROMPT_PATH}")

    prompt_template = PROMPT_PATH.read_text(encoding="utf-8")
    truth_map = load_truth()

    docs = sorted(DOC_DIR.glob("*.txt"))
    if not docs:
        raise RuntimeError(f"No documents found in {DOC_DIR}")

    for doc in docs:
        doc_id = doc.stem
        out_path = OUTPUT_DIR / f"{doc_id}.json"

        if out_path.exists():
            print(f"Skip existing: {out_path.name}")
            continue

        if doc_id not in truth_map:
            raise KeyError(f"{doc_id} not found in ground truth")

        target_name = truth_map[doc_id]["target_name"]
        document_text = doc.read_text(encoding="utf-8")

        prompt = prompt_template.replace("{{DOCUMENT}}", document_text)
        prompt = prompt.replace("{{TARGET_NAME}}", target_name)

        resp = None
        for attempt in range(3):
            try:
                resp = client.chat.completions.create(
                    model=MODEL,
                    messages=[
                        {
                            "role": "system",
                            "content": "You extract structured information from long documents and return strict JSON only."
                        },
                        {"role": "user", "content": prompt},
                    ],
                    temperature=0,
                )
                break
            except Exception as e:
                if attempt == 2:
                    raise
                wait = 2 ** attempt
                print(f"Error for {doc_id}: {e}. Retry in {wait}s...")
                time.sleep(wait)

        text = resp.choices[0].message.content.strip()

        wrapper = {
            "doc_id": doc_id,
            "target_name": target_name,
            "model": MODEL,
            "_raw": text,
            "parsed": None,
        }

        try:
            wrapper["parsed"] = json.loads(text)
        except json.JSONDecodeError:
            wrapper["parsed"] = None

        out_path.write_text(
            json.dumps(wrapper, indent=2, ensure_ascii=False),
            encoding="utf-8"
        )
        print(f"Saved {out_path}")

if __name__ == "__main__":
    run()