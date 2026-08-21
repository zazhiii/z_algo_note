# 文档质量检查

本目录提供只读、零第三方依赖的 Markdown 检查脚本，使用仓库现有的 Python 3 运行。脚本不会改写题解或自动修复问题；发现问题时返回非零退出码。

## 本地结构检查

在仓库根目录运行：

```bash
python scripts/check_docs.py
```

默认检查 Git 已跟踪和未被忽略的 Markdown 文件，包括：

- 是否包含一级标题；
- 反引号或波浪线代码围栏是否闭合；
- Markdown、引用式及常见 HTML 相对链接指向的文件是否存在，并检查路径大小写；
- 是否为空文档；
- 是否超过 100 KiB 或 1000 行；
- 单个文件是否超过 10 个裸 HTTP(S) URL；
- 文件名是否符合仓库规范：普通文档使用小写 `snake_case`，比赛记录也可使用小写 `kebab-case`，`README.md` 和常见仓库元文档除外；
- 现有 Markdown 或各文档目录中的 Markdown 是否被 `.gitignore` 规则意外忽略。

规模和裸 URL 阈值可以显式调整：

```bash
python scripts/check_docs.py --max-bytes 153600 --max-lines 1500 --max-bare-urls 20
```

退出码为 `0` 表示通过，`1` 表示发现质量问题，`2` 表示命令参数错误。GitHub Actions 在 `push` 和 `pull_request` 时只运行这一确定性检查。

检查器自身的回归测试同样不需要额外依赖：

```bash
python -m unittest discover -s scripts/tests -v
```

## 外链可达性检查

外部网站会发生临时故障、限流或网络抖动，因此外链检查是单独的、按需执行的命令，不包含在默认检查和 CI 中：

```bash
python scripts/check_external_links.py
```

可通过 `--timeout` 调整单次请求超时，通过 `--workers` 调整并发数。外链不可访问时该独立命令返回 `1`，但不会影响常规文档 CI。
