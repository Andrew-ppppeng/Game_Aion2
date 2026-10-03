"""Copy only audited Vercel dry-run inputs to a new, isolated deployment directory.

First run: vercel deploy --dry --json > .qa/deploy-inputs.json
This avoids archive-mode inclusion of ignored research and local secrets.
"""
import datetime
import json
import pathlib
import shutil

root = pathlib.Path(__file__).resolve().parents[1]
inputs = json.loads((root / ".qa" / "deploy-inputs.json").read_text(encoding="utf-8-sig"))
staging = root / ".qa" / ("vercel-source-" + datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%d-%H%M%S-%f"))
staging.mkdir(parents=True)
blocked = {"research", "discord", ".agents", ".backups", ".qa", ".git", ".vercel", "node_modules", ".next", "tests", "scripts", "aion2_favicon"}
count, size = 0, 0
for record in inputs["files"]:
    relative = pathlib.Path(record["path"])
    source = (root / relative).resolve()
    if not source.is_file():
        continue
    if not source.is_relative_to(root) or relative.parts[0] in blocked or (relative.name.startswith(".env") and relative.name != ".env.example"):
        raise ValueError("Unsafe deployment input: " + str(relative))
    target = (staging / relative).resolve()
    if not target.is_relative_to(staging):
        raise ValueError("Unsafe staging target")
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, target)
    count += 1
    size += source.stat().st_size
linked = staging / ".vercel"
linked.mkdir()
shutil.copy2(root / ".vercel" / "project.json", linked / "project.json")
print(json.dumps({"staging": str(staging), "files": count, "bytes": size}))
