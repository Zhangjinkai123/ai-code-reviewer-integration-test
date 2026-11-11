# AI Code Reviewer Integration Test

这是 `Zhangjinkai123/ai-code-reviewer` 的外部仓库接入样例，用来验证
Reusable Workflow 的审查、Artifact、PR 评论和门禁行为。

## 上传到 GitHub

1. 在 GitHub 创建一个空仓库。
2. 将本目录内容推送到默认分支。
3. 在仓库 Settings -> Secrets and variables -> Actions 中新增：
   - `CR_API_KEY`：OpenAI 兼容服务的 API Key。
4. 根据使用的模型服务修改 `.github/workflows/ai-review.yml` 中的
   `base-url` 和 `model`。

## 验收流程

1. 从默认分支创建测试分支。
2. 修改 `app.py`，将安全的参数化查询改成字符串拼接，例如：

   ```python
   query = "SELECT * FROM users WHERE name = '" + name + "'"
   ```

3. 提交并创建 Pull Request。
4. 在 Actions 中确认 `AI Code Review` 运行，检查：
   - `review` Job 生成报告并上传 Artifact；
   - `publish` Job 在 PR 中创建评论；
   - 高危问题导致审查检查失败。
5. 修复问题并再次推送，确认新提交会重新审查。
6. 可在审查运行期间再次推送一次，用来验证旧 head 的报告不会发布过期评论。

注意：fork 发起的 PR 默认无法读取上游 Secret，审查会因缺少 API Key
而失败，这是 GitHub 的 Secret 安全限制，不代表 Workflow 配置错误。

