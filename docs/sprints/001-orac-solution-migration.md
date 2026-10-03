# Sprint 001: ORAC 满分解答迁移

## 目标

将 `aaron_wang` 在 ORAC 上 14 道唯一的 100 分 Python 提交迁移到本仓库，每题一个源码文件，并保留可验证的来源元数据。

## 验收标准

- [ ] `metadata/submissions.json` 恰好记录 14 道唯一题目。
- [ ] 每条记录的语言为 Python、分数为 100，并对应一个独立源码文件。
- [ ] `solutions/` 中恰好包含 14 个登记过的 `.py` 文件。
- [ ] 每个源码文件的 SHA-256 与元数据一致。
- [ ] 全部源码通过 Python 语法编译检查。
- [ ] 仓库不包含密码、Cookie、Token、题面或抓取页面。
- [ ] README 提供 14 道题目的名称、ORAC 链接和源码索引。
- [ ] Git 提交使用 Aaron Wang 明确指定且关联 GitHub 的 Gmail 地址。
- [ ] 推送后从远端核对默认分支和提交 SHA。

## 实施计划

- [x] **Task 1：冻结 ORAC 满分题目清单**
- [x] **Task 2：Scrum 验收标准与架构审批**
- [x] **Task 3：先写仓库完整性测试**
- [x] **Task 4：运行测试并确认红灯**
- [x] **Task 5：写入 14 份源码、元数据和 README，不修改算法逻辑**
- [x] **Task 6：运行测试并达到绿灯**
- [x] **Task 7：核对 Aaron Gmail 与 GitHub 写入身份**
- [x] **Task 8：提交、推送并远端复核**

