import json
import random
import argparse
from pathlib import Path

random.seed(42)

BASE_DIR = Path(__file__).resolve().parent.parent
DOC_DIR = BASE_DIR / "Data" / "documents"
TRUTH_DIR = BASE_DIR / "Truth"
TRUTH_PATH = TRUTH_DIR / "ground_truth.jsonl"

DOC_DIR.mkdir(parents=True, exist_ok=True)
TRUTH_DIR.mkdir(parents=True, exist_ok=True)

FIRST_NAMES = [
    "Alex", "Priya", "Marco", "Jasmine", "Omar", "Elena", "Noah", "Sophia",
    "Mina", "Diego", "Hannah", "Ethan", "Ava", "Leo", "Amir", "Mei",
    "Ravi", "Sara", "Luis", "Nina"
]

LAST_NAMES = [
    "Chen", "Nair", "Silva", "Patel", "Garcia", "Kim", "Lopez", "Nguyen",
    "Brown", "Wang", "Johnson", "Miller", "Davis", "Martinez", "Anderson",
    "Thomas", "Taylor", "Moore", "Jackson", "Lee"
]

DEPARTMENTS = [
    "Business Intelligence",
    "Data Platform",
    "Finance Analytics",
    "Operations",
    "Marketing Analytics",
    "Product Analytics",
    "People Operations",
    "Engineering"
]

JOB_TITLES = [
    "Data Analyst",
    "Senior Data Analyst",
    "Analytics Engineer",
    "Business Analyst",
    "Data Scientist",
    "Senior Data Scientist",
    "Product Manager",
    "Software Engineer"
]

WEEKLY_HOURS = [35, 40, 45]
YEARS_AT_COMPANY = [2, 3, 4, 5, 6, 7]

GENERIC_COMPANY_PARAS = [
    "The company has continued expanding its internal reporting processes in response to growth across finance, operations, and product functions. Leadership has emphasized documentation quality, metric consistency, and stronger cross-functional visibility in quarterly planning cycles.",
    "In recent months, managers have highlighted the importance of combining technical execution with business context. Internal teams increasingly contribute to recurring reviews, project retrospectives, and staffing conversations that support long-term planning.",
    "Company documents frequently reference collaboration across departments, especially when analytics work intersects with operational goals. Several groups now maintain more structured internal records than they did during earlier growth phases.",
    "Internal communications often discuss workflow reliability, handoff quality, and staffing alignment. Team leads are encouraged to document role changes, allocation shifts, and cross-functional dependencies in a more standardized way.",
    "As the organization matures, employee responsibilities are described not only in formal team rosters but also in planning notes, project summaries, and internal memos. This has increased the amount of semi-structured information present in company documents.",
]

PROJECT_PARAS = [
    "A recent planning memo noted that several reporting pipelines would need better ownership definitions before the next quarterly review. Some teams are also revisiting dashboard maintenance responsibilities and metric governance practices.",
    "An operations update mentioned that multiple departments are balancing routine reporting work with ad hoc support for cross-team initiatives. This has made staffing documentation more important for resourcing decisions.",
    "A project summary described how internal analytics support is now distributed across several functions, with role clarity becoming more important as teams grow. Leadership wants future documentation to make staffing responsibilities easier to trace.",
    "Meeting notes from planning sessions emphasized that different teams contribute to forecasting, monitoring, and ad hoc analysis in overlapping ways. As a result, internal writeups often contain employee details mixed in with broader organizational discussion.",
]

ROLE_SENTENCE_TEMPLATES = [
    "{name} currently serves as a {job_title}.",
    "In recent planning documents, {name} is described as working as a {job_title}.",
    "According to the latest staffing summary, {name}'s role is listed as {job_title}.",
]

DEPT_SENTENCE_TEMPLATES = [
    "{name} is aligned with the {department} team.",
    "Most of {name}'s work is associated with {department}.",
    "Internal staffing notes place {name} in {department}.",
]

YEARS_SENTENCE_TEMPLATES = [
    "{name} has been with the company for {years} years.",
    "Current records indicate that {name} has spent {years} years at the company.",
    "{name}'s tenure is listed as {years} years.",
]

HOURS_SENTENCE_TEMPLATES = [
    "{name} typically works {hours} hours per week.",
    "Workload notes indicate that {name} generally maintains a {hours}-hour work week.",
    "{name}'s standard weekly schedule is {hours} hours.",
]

DISTRACTOR_SENTENCE_TEMPLATES = [
    "{name} supports initiatives tied to {department} and has been increasingly involved in cross-team coordination.",
    "Recent internal notes describe {name} as an important contributor within {department}.",
    "{name} has recently taken on more recurring work connected to {department}.",
    "Planning discussions mention {name} in connection with work related to {department}.",
]

def random_name(exclude=None):
    exclude = set(exclude or [])
    while True:
        name = f"{random.choice(FIRST_NAMES)} {random.choice(LAST_NAMES)}"
        if name not in exclude:
            return name

def sample_truth():
    return {
        "job_title": random.choice(JOB_TITLES),
        "department": random.choice(DEPARTMENTS),
        "years_at_company": random.choice(YEARS_AT_COMPANY),
        "weekly_hours": random.choice(WEEKLY_HOURS),
    }

def make_target_name():
    return f"{random.choice(FIRST_NAMES)} {random.choice(LAST_NAMES)}"

def make_similar_names(target_name):
    first, last = target_name.split()
    same_last = random.choice([f"{random.choice(FIRST_NAMES)} {last}", None])
    same_first = random.choice([f"{first} {random.choice(LAST_NAMES)}", None])

    out = []
    if same_last and same_last != target_name:
        out.append(same_last)
    if same_first and same_first != target_name and same_first not in out:
        out.append(same_first)
    return out

def make_target_fact_block(target_name, truth):
    sentences = [
        random.choice(ROLE_SENTENCE_TEMPLATES).format(name=target_name, job_title=truth["job_title"]),
        random.choice(DEPT_SENTENCE_TEMPLATES).format(name=target_name, department=truth["department"]),
        random.choice(YEARS_SENTENCE_TEMPLATES).format(name=target_name, years=truth["years_at_company"]),
        random.choice(HOURS_SENTENCE_TEMPLATES).format(name=target_name, hours=truth["weekly_hours"]),
    ]
    random.shuffle(sentences)

    para1 = " ".join(sentences[:2])
    para2 = " ".join(sentences[2:]) + " " + random.choice(PROJECT_PARAS)
    return [para1, para2]

def make_distractor_block(name):
    department = random.choice(DEPARTMENTS)
    job_title = random.choice(JOB_TITLES)
    years = random.choice(YEARS_AT_COMPANY)
    hours = random.choice(WEEKLY_HOURS)

    s = [
        random.choice(DISTRACTOR_SENTENCE_TEMPLATES).format(name=name, department=department),
        random.choice(ROLE_SENTENCE_TEMPLATES).format(name=name, job_title=job_title),
        random.choice(DEPT_SENTENCE_TEMPLATES).format(name=name, department=department),
        random.choice(YEARS_SENTENCE_TEMPLATES).format(name=name, years=years),
        random.choice(HOURS_SENTENCE_TEMPLATES).format(name=name, hours=hours),
        random.choice(PROJECT_PARAS),
    ]
    random.shuffle(s)
    return " ".join(s[:3])

def make_background_section():
    paras = []
    for _ in range(4):
        paras.append(random.choice(GENERIC_COMPANY_PARAS) + " " + random.choice(PROJECT_PARAS))
    return paras

def build_document(position, target_name, truth):
    used = {target_name}
    similar_names = make_similar_names(target_name)
    used.update(similar_names)

    distractor_names = list(similar_names)
    while len(distractor_names) < 10:
        distractor_names.append(random_name(exclude=used))
        used.add(distractor_names[-1])

    random.shuffle(distractor_names)

    background = make_background_section()
    distractors = [make_distractor_block(n) for n in distractor_names]
    target_block = make_target_fact_block(target_name, truth)

    # A few extra mentions of the target without all facts
    weak_mentions = [
        f"In one staffing discussion, {target_name} was mentioned alongside several employees supporting recurring reporting work.",
        f"Another planning note briefly referenced {target_name} in the context of ongoing cross-team coordination.",
    ]

    chunks = []
    chunks.extend(background[:2])

    if position == "begin":
        chunks.extend(target_block)
        chunks.extend(weak_mentions[:1])
        chunks.extend(distractors[:5])
        chunks.extend(background[2:])
        chunks.extend(distractors[5:])
        chunks.extend(weak_mentions[1:])
    elif position == "middle":
        chunks.extend(distractors[:4])
        chunks.extend(background[2:3])
        chunks.extend(target_block)
        chunks.extend(weak_mentions)
        chunks.extend(distractors[4:])
        chunks.extend(background[3:])
    elif position == "end":
        chunks.extend(distractors)
        chunks.extend(background[2:])
        chunks.extend(weak_mentions)
        chunks.extend(target_block)
    else:
        raise ValueError("position must be begin, middle, or end")

    sections = [
        "Company Overview\n\n" + "\n\n".join(chunks[:4]),
        "Planning Notes\n\n" + "\n\n".join(chunks[4:8]),
        "Staffing and Project Updates\n\n" + "\n\n".join(chunks[8:]),
    ]
    return "\n\n".join(sections)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--n_per_condition", type=int, default=100)
    parser.add_argument("--overwrite", action="store_true")
    args = parser.parse_args()

    if args.overwrite:
        for f in DOC_DIR.glob("about_us_*.txt"):
            f.unlink()

    rows = []

    for position in ["begin", "middle", "end"]:
        for i in range(1, args.n_per_condition + 1):
            doc_id = f"about_us_{position}_{i:03d}"
            out_path = DOC_DIR / f"{doc_id}.txt"

            target_name = make_target_name()
            truth = sample_truth()
            text = build_document(position, target_name, truth)

            out_path.write_text(text, encoding="utf-8")

            rows.append({
                "doc_id": doc_id,
                "target_name": target_name,
                "ground_truth": truth
            })

    with open(TRUTH_PATH, "w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")

    print(f"Generated {len(rows)} documents in {DOC_DIR}")
    print(f"Wrote ground truth to {TRUTH_PATH}")

if __name__ == "__main__":
    main()