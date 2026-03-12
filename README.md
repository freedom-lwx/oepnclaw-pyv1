# LeetCode 练习记录

我的 LeetCode 刷题记录仓库，包含代码、笔记和在线文档。

## 📖 在线文档

**访问地址：** https://freedom-lwx.github.io/openclaw-pyv1/

推送代码后自动更新网站。

## 📁 目录结构

```
openclaw-pyv1/
├── docs/               # MkDocs 文档源文件
│   ├── index.md        # 首页
│   ├── problems/       # 题目文档（自动生成）
│   └── notes/          # 学习笔记
├── problems/           # 题目代码
│   └── 0001-two-sum/
│       ├── solution.py
│       └── README.md
├── template/           # 题目模板
├── scripts/            # 辅助脚本
├── mkdocs.yml          # MkDocs 配置
└── requirements.txt    # Python 依赖
```

## 🚀 快速开始

### 本地预览网站

```bash
# 安装依赖
pip install -r requirements.txt

# 同步题目到文档
python scripts/sync_docs.py

# 启动本地服务器
mkdocs serve
```

打开 http://127.0.0.1:8000 查看效果。

### 添加新题目

1. 复制模板：
   ```bash
   cp -r template problems/0001-two-sum
   ```

2. 修改 `problems/0001-two-sum/solution.py` 和 `README.md`

3. 同步文档并推送：
   ```bash
   python scripts/sync_docs.py
   git add . && git commit -m "Add problem 0001" && git push
   ```

## 📊 进度统计

| 难度 | 完成 |
|------|------|
| Easy | 0 |
| Medium | 0 |
| Hard | 0 |

---

开始刷题！💪
