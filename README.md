# GitHub Star 管理器

这个Python脚本允许你管理你在GitHub上标星的仓库。它可以获取你所有标星的仓库，并批量取消标星。
<p align="center">
<b><a href="#">中文</a></b>
<b> | </b>
  <b><a href="README_EN.md">English</a></b>
</p>

## 功能

- 从你的GitHub账户获取所有标星的仓库
- 将标星的仓库保存到JSON文件中以便离线访问
- 批量取消所有仓库的标星

## 前提条件

在开始之前，请确保你满足以下要求：

- Python 3.6+
- 安装了`requests`库
- 具有`user`权限的GitHub个人访问令牌

## 安装

1. 克隆此仓库：
   ```
   git clone https://github.com/huhusmang/github-star-manager.git
   cd github-star-manager
   ```

2. 安装所需的Python包：
   ```
   pip install requests
   ```

3. 将你的GitHub个人访问令牌设置为环境变量：
   ```
   export personal_access_token="personal_access_token"
   ```

## 使用方法

使用Python运行脚本：

```
python star_manager.py
```

脚本将执行以下操作：

1. 检查`starred_repos.json`文件是否存在：
   - 如果存在，从该文件加载标星的仓库。
   - 如果不存在，从GitHub获取所有标星的仓库并保存到`starred_repos.json`。

2. 取消所有列表中仓库的标星。

## 工作原理

1. 脚本使用GitHub API获取已认证用户的所有标星仓库。
2. 它将获取的数据保存到JSON文件中，以便将来使用并避免不必要的API调用。
3. 然后，它遍历标星仓库列表并取消每个仓库的标星。

## 配置

脚本使用以下GitHub API端点：

- `https://api.github.com/user/starred` 用于获取标星的仓库
- `https://api.github.com/user/starred/{owner}/{repo}` 用于取消特定仓库的标星

使用的GitHub API版本是 `2022-11-28`。

## 安全性

此脚本需要GitHub个人访问令牌。切勿共享你的令牌或将其提交到版本控制系统。始终使用环境变量或安全的秘密管理工具来处理敏感信息。

## 贡献

欢迎贡献、问题和功能请求。如果你想贡献，请查看[问题页面](https://github.com/你的用户名/github-star-manager/issues)。
