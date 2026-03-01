# OpenCLAW X.com 趋势

![OpenCLAW Banner](background.png)

展示 X.com 上关于 OpenCLAW 的热门帖子网页。

## 功能特点

- **官方账号** - @openclaw 官方发布的最新动态
- **每日 Top 5** - 其他用户发布的关于 OpenCLAW 的热门帖子（当日）
- **每周 Top 5** - 其他用户发布的关于 OpenCLAW 的热门帖子（最近7天）
- **卡片展示** - 每个帖子以卡片形式展示，包含：
  - 帖子配图或作者主页背景
  - 作者信息（头像、昵称、账号）
  - 帖子内容摘要
  - 互动数据（点赞、评论、转发）
  - 原文链接

## 技术栈

- 纯 HTML/CSS/JavaScript
- 无需后端服务器，直接在浏览器中运行

## 数据来源

- 使用 Jina AI Reader API 获取 X.com 帖子数据
- 帖子按点赞 + 评论 + 转发总数排序

## 使用方法

1. 克隆仓库：
   ```bash
   git clone https://github.com/ahucslf/openclaw-x-trending.git
   ```

2. 直接在浏览器中打开 `index.html` 文件

## 自定义数据

如需更新帖子数据，编辑 `index.html` 中的 JavaScript 数据数组：
- `officialPosts` - 官方账号帖子
- `dailyPosts` - 每日热门帖子
- `weeklyPosts` - 每周热门帖子

## 预览

![OpenCLAW Preview](background.png)

打开 `index.html` 即可预览效果。

## License

MIT
