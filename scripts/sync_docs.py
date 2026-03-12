#!/usr/bin/env python3
"""
同步 problems 目录到 docs/problems

将 problems/ 目录下的代码和笔记同步到 MkDocs 文档目录
"""

import os
import shutil
from pathlib import Path

PROBLEMS_DIR = Path(__file__).parent.parent / "problems"
DOCS_PROBLEMS_DIR = Path(__file__).parent.parent / "docs" / "problems"


def sync_problems():
    """同步所有题目到 docs"""
    if not PROBLEMS_DIR.exists():
        print("No problems directory found")
        return

    # 确保目标目录存在
    DOCS_PROBLEMS_DIR.mkdir(parents=True, exist_ok=True)

    # 遍历所有题目
    for problem_dir in PROBLEMS_DIR.iterdir():
        if not problem_dir.is_dir():
            continue

        problem_name = problem_dir.name
        target_dir = DOCS_PROBLEMS_DIR / problem_name
        target_dir.mkdir(exist_ok=True)

        # 复制 README.md
        src_readme = problem_dir / "README.md"
        if src_readme.exists():
            shutil.copy(src_readme, target_dir / "index.md")

        # 如果没有 README，创建基本的 index.md
        else:
            (target_dir / "index.md").write_text(f"# {problem_name}\n\n*待补充*\n")

        # 复制代码文件，嵌入到 markdown 中
        code_files = list(problem_dir.glob("*.py"))
        if code_files:
            code_content = []
            for code_file in code_files:
                code = code_file.read_text()
                code_content.append(f"## {code_file.name}\n\n```python\n{code}\n```\n")

            # 追加代码到 index.md
            with open(target_dir / "index.md", "a") as f:
                f.write("\n\n---\n\n## 代码\n\n")
                f.write("\n".join(code_content))

        print(f"Synced: {problem_name}")

    print("\n✅ Sync complete!")


if __name__ == "__main__":
    sync_problems()
