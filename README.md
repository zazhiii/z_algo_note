# 算法题解知识库

本仓库用于沉淀算法竞赛与日常刷题资料，包括比赛复盘、按知识点整理的题单、可复用的算法模板，以及 Java、Python 语言速查笔记。现有内容以 Java 为主，适合作为学习路线索引、赛后补题清单和比赛前模板入口。

## 快速导航

| 目录 | 职责 | 使用方式 |
| --- | --- | --- |
| [contest](contest/README.md) | 按平台和场次保存比赛记录、当场思路、补题过程与代码 | 赛后复盘，从平台索引进入具体场次 |
| [problem-list](problem-list/README.md) | 按知识点收录题目、难度、标签和简短提示 | 按学习路径选题与查漏补缺 |
| [templates](templates/README.md) | 保存可复用的算法原理、实现、复杂度和注意事项 | 编码前复习，验证后再复制使用 |
| [languages](languages/README.md) | 记录语言特性、标准库和竞赛输入输出 | 查询 Java、Python 写法，不承载算法分类 |
| [to-organize](to-organize/README.md) | 暂存尚未拆分或无法稳定归类的资料 | 完成归类后迁移到题单或模板 |

## 推荐学习路径

[基础算法](problem-list/foundation/README.md) → [数据结构](problem-list/data-structure/README.md) → [搜索与图论](problem-list/graph/README.md) → [动态规划](problem-list/dynamic-programming/README.md) → [数学](problem-list/math/README.md)

1. 先通过题单理解典型问题和常见模型。
2. 完成练习后，对照对应的[算法模板](templates/README.md)总结原理、复杂度与边界。
3. 使用[比赛记录](contest/README.md)检验综合应用能力，并将赛后发现的新知识点补回题单。

字符串可在掌握基础算法后作为独立专题学习：[字符串题单](problem-list/string/README.md)。

## 知识点目录

### 基础算法

- [二分查找](problem-list/foundation/binary_search.md)
- [前缀和与差分](problem-list/foundation/prefix_sum.md)
- [双指针与滑动窗口](problem-list/foundation/two_pointers.md)
- [位运算](problem-list/foundation/bitwise_operations.md)
- [暴力与枚举](problem-list/foundation/brute_force.md)
- [排序](problem-list/foundation/sort.md)
- [贪心](problem-list/foundation/greedy.md)
- [排列与置换](problem-list/foundation/permutation.md)

### 数据结构

- [二叉树](problem-list/data-structure/binary_tree.md)
- [并查集](problem-list/data-structure/union_find.md)
- [Trie](problem-list/data-structure/trie.md)
- [单调队列](problem-list/data-structure/monotonic_queue.md)
- [单调栈](problem-list/data-structure/monotonic_stack.md)
- [集合](problem-list/data-structure/set.md)
- [堆](problem-list/data-structure/heap.md)

### 搜索与图论

- [广度优先搜索（BFS）](problem-list/graph/bfs.md)
- [深度优先搜索（DFS）](problem-list/graph/dfs.md)
- [图论基础](problem-list/graph/graph_basics.md)
- [最短路](problem-list/graph/shortest_path.md)
- [最近公共祖先（LCA）](problem-list/graph/lca.md)（倍增模板待补充）

### 动态规划

- [动态规划题单](problem-list/dynamic-programming/problems.md)
- [背包与经典动态规划模板](templates/dynamic-programming/dp.md)（LCS、LIS 待补充）

### 数学

- [数学题单](problem-list/math/problems.md)
- [数学基础模板](templates/math/math.md)
- [组合数学](templates/math/combinatorics.md)
- [计算几何](templates/math/geometry.md)

### 字符串

- [字符串题单](problem-list/string/problems.md)
- [字符串哈希模板](templates/string/string_hash.md)（待补充）

## 比赛平台入口

- [AtCoder](contest/atcoder/README.md)
- [Codeforces](contest/codeforces/README.md)
- [LeetCode](contest/leetcode/README.md)
- [牛客](contest/nowcoder/README.md)
- [洛谷](contest/luogu/README.md)

各平台入口只负责索引仓库内已有的比赛记录；具体题目的原始平台链接保留在对应题解或题单中。

## 题解记录规范

### 单题记录

- 标题或首个条目写明平台、题号和题名；外部原题链接放在具体题解或题单中。
- 至少记录核心思路、关键状态或不变量、时间复杂度、空间复杂度和边界条件。
- 代码注明语言；若代码尚未通过样例或在线评测，必须标记为“待复核”。
- 完整推导与实现放在题解或模板中；题单只保留分类、难度、标签和一两句提示。
- 同一道题可以出现在多个知识点下，但每处应注明该分类对应的练习重点。

新增单题、比赛复盘或算法文档时，分别使用[单题题解模板](templates/problem_solution.md)、[比赛复盘模板](templates/contest_review.md)和[算法文档模板](templates/algorithm_document.md)。

### 状态说明

| 状态 | 含义 |
| --- | --- |
| 已完成 | 已记录可用思路或代码，但不等同于已沉淀为通用模板 |
| 已复核 | 已检查实现、复杂度和关键边界，可作为稳定参考 |
| 待复核 | 已有实现，但仍需样例、在线评测或边界用例验证 |
| 待补充 / `TODO` | 内容缺失或只有占位说明，暂不可视为完整资料 |
| `exc` | 历史记录中的未完成标记，整理时按“待补充”处理 |
| 待整理 | 内容已保留，但主知识点或最终归属尚未确定 |

每份 Markdown 只使用一个一级标题；章节、子章节和题目依次使用二至四级标题。英文目录统一使用小写，文件名优先使用小写 `snake_case`；比赛文件沿用平台常见编号格式。

## 常用模板入口

- 基础算法：[双指针](templates/foundation/two_pointers.md) · [贪心](templates/foundation/greedy.md) · [排列生成](templates/foundation/permutation.md) · [排序](templates/foundation/sort.md)（待补充）
- 数据结构：[并查集](templates/data-structure/union_find.md) · [Trie](templates/data-structure/trie.md) · [单调队列](templates/data-structure/monotonic_queue.md)
- 搜索与图论：[Dijkstra 最短路](templates/graph/shortest_path.md)
- 动态规划：[背包与经典动态规划](templates/dynamic-programming/dp.md)
- 数学：[数学基础](templates/math/math.md) · [组合数学](templates/math/combinatorics.md) · [计算几何](templates/math/geometry.md)
- 语言骨架：[Java 竞赛输入输出](languages/java/Main.java) · [Java 速查](languages/java/README.md) · [Python 速查](languages/python/README.md)

复制模板前，先确认输入格式、数据范围、下标约定、整数范围和图的有向性；带有“待补充”或“待复核”状态的内容不能直接视为稳定模板。

## 最近整理与待补充

### 最近整理

- 2026-08-20：按比赛平台、知识点、模板类型和语言重新整理目录，拆分聚合文件，并统一入口与命名；详细映射见[信息架构迁移映射](REORGANIZATION.md)。
- 2026-08-20：补充题解、比赛复盘和算法文档骨架，明确题单与模板的内容边界。

### 待补充

- [排序模板](templates/foundation/sort.md)：补充稳定性、自定义比较器和常用排序复杂度。
- [字符串哈希模板](templates/string/string_hash.md)：补充基数、模数、区间哈希公式和碰撞风险。
- [LCA 题单](problem-list/graph/lca.md)：补充树上倍增模板及复杂度说明。
- [动态规划模板](templates/dynamic-programming/dp.md)：补充最长公共子序列（LCS）和最长递增子序列（LIS）。
- [Python 速查](languages/python/README.md)：目前仅有集合笔记，容器、字符串、数学函数和输入输出仍待补充。
- [待整理题单](problem-list/to-organize/README.md)与[待整理清单](to-organize/README.md)：继续拆分综合练习和 LeetCode Hot 100 旧笔记。
