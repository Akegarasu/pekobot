<p align="center">
<img src="https://i.loli.net/2021/02/10/hOZgH3Qki5E26wT.png" width="200" height="200" alt="go-cqhttp">
</p>


<div align="center">

# pekobot

_✨ 基于 asyncio 的  Python 异步开黑啦机器人框架，兼容 [nonebot](https://github.com/nonebot/nonebot) 项目 ✨_

</div>

<p align="center">
  <a href="https://github.com/Akegarasu/pekobot/stargazers">
    <img src="https://img.shields.io/github/stars/Akegarasu/pekobot?style=social?color=blueviolet" alt="release">
  </a>
  <a href="https://raw.githubusercontent.com/Akegarasu/pekobot/master/LICENSE">
    <img src="https://img.shields.io/github/license/Akegarasu/pekobot" alt="license">
  </a>
  <a href="https://github.com/Akegarasu/pekobot/releases">
    <img src="https://img.shields.io/github/v/release/Akegarasu/pekobot?color=blueviolet&include_prereleases" alt="release">
  </a>
  <a href="https://github.com/howmanybots/onebot/blob/master/README.md">
    <img src="https://img.shields.io/badge/OneBot-v11-blue?style=flat&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEAAAABABAMAAABYR2ztAAAAIVBMVEUAAAAAAAADAwMHBwceHh4UFBQNDQ0ZGRkoKCgvLy8iIiLWSdWYAAAAAXRSTlMAQObYZgAAAQVJREFUSMftlM0RgjAQhV+0ATYK6i1Xb+iMd0qgBEqgBEuwBOxU2QDKsjvojQPvkJ/ZL5sXkgWrFirK4MibYUdE3OR2nEpuKz1/q8CdNxNQgthZCXYVLjyoDQftaKuniHHWRnPh2GCUetR2/9HsMAXyUT4/3UHwtQT2AggSCGKeSAsFnxBIOuAggdh3AKTL7pDuCyABcMb0aQP7aM4AnAbc/wHwA5D2wDHTTe56gIIOUA/4YYV2e1sg713PXdZJAuncdZMAGkAukU9OAn40O849+0ornPwT93rphWF0mgAbauUrEOthlX8Zu7P5A6kZyKCJy75hhw1Mgr9RAUvX7A3csGqZegEdniCx30c3agAAAABJRU5ErkJggg==" alt="cqhttp">
  </a>
</p>



<p align="center">
  <a href="https://github.com/Akegarasu/pekobot/wiki">文档</a>
  ·
  <a href="https://github.com/Akegarasu/pekobot/releases">下载</a>
  ·
  <a href="https://github.com/Akegarasu/pekobot/tree/main/demo">开始使用</a>
</p>


---

pekobot 在 [原版 nonebot](https://github.com/nonebot/nonebot) 的基础上做了部分修改和拓展，以此适配开黑啦

---

### 关于本项目

本项目的目标是使基于nonebot的开发者平滑的将自己的qqbot**迁移**至开黑啦平台，尽量减少代码修改。

从根本上来说，本项目基于是 [nonebot](https://github.com/nonebot/nonebot) 与 [aiocqhttp](https://github.com/nonebot/aiocqhttp) （均为MIT License）的一个融合魔改项目，使用`pekocore`代替了`aiocqhttp`进行适配，使用`aiohttp`重写了 ws 连接部分、Event 处理部分以及全部的 api 部分。

### 优秀的开源项目

在编写本项目中，以下项目带给我很大的帮助，并且我从以下项目中学习了许多。

**nonebot**: [https://github.com/nonebot/nonebot](https://github.com/nonebot/nonebot)

**aiocqhttp**: [https://github.com/nonebot/aiocqhttp](https://github.com/nonebot/aiocqhttp)

**khl.py**: [https://github.com/TWT233/khl.py](https://github.com/TWT233/khl.py)