# Three-body Simulator
## 作者
一位不愿留下姓名初一学生
## 简介
这是一个三体模拟器,，由 `python` 写成，以 `pygame zero` 为核心。
## 项目结构
```
three_body/
  ├─ .gitignore
  ├─ main.py
  ├─ README.md
  ├─ star.py
  ├─ stars.yaml  
  └─ __pycache__/
       ├─ point.cpython-310.pyc
       └─ star.cpython-310.pyc
```
| 文件名        | 作用                                               |
| ------------- | -------------------------------------------------- |
| .gitignore    | git文件                                            |
| main.py       | 主文件，运行它！                                   |
| README.md     | 介绍文件，即本文                                   |
| star.py       | 类文件，包含恒星、行星类                           |
| stars.yaml    | 配置文件，包含形体的数量、初始动量、质量等，可自定义 |
| \_\_pycache__ | python缓存                                         |

## 更新明细
### Version 1.0 更新说明
> - 完成天体和物理引擎
> - 引入`pyyaml`实现配置文件功能
  

### Version 1.1 更新说明
> - 主功能完工
> - 添加`README.md`和`update.md`
> - 引入`git`

### Version 2.0 更新说明
> - 添加轨迹
> - 添加配置文件中的轨迹相关配置项
> - 添加配置文件说明文档`docs.md`

### Version 2.1 更新说明
> - 添加空格键暂停
> - 添加上下左右键移动视角
> - 添加配置文件中视角移动速度配置项`camera_speed`
> - 将`docx.md`和`update.md`并入`README.md`

### Version 2.1.1-2.2.3 更新说明
> - 修复了暂停时仍有日志输出的bug
> - 在.gitignore中删除了`READ.md`和`stars.yaml`
> - 上传到`Github`仓库`mc-admin-bit/ths`


## `stars.yaml`配置文件说明
> 默认配置
> ```yaml
> # 900x600
> stars:
>   - mass: 100000000000000
>     pos: [450, 200]
>     vel: [-1, 0]
>     color: [255, 0, 0]
>   - mass: 100000000000000
>     pos: [300, 400]
>     vel: [0, 0]
>     color: [0, 255, 0]
>   - mass: 100000000000000
>     pos: [600, 400]
>     vel: [0, 0]
>     color: [0, 0, 255]
> planets:
>   - mass: 10000
>     pos: [450, 300]
>     vel: [0, 0]
>     color: [255, 255, 255]
> star_trajectory: true
> planet_trajectory: true
> trajectory_length: 20
> camera_speed: 2
> ```
| 名称                | 二级名称 | 含义                           |
| ------------------- | -------- | ------------------------------ |
| `stars`             |          | 恒星配置                       |
| `stars`             | `mass`   | 恒星质量                       |
| `stars`             | `pos`    | 恒星初始位置 (x, y)            |
| `stars`             | `vel`    | 恒星初始加速度 (dx, dy)        |
| `stars`             | `color`  | 恒星颜色 (R, G, B)             |
|                     |          |                                |
| `planets`           |          | 行星配置                       |
| `planets`           | `mass`   | 行星质量                       |
| `planets`           | `pos`    | 行星初始位置 (x, y)            |
| `planets`           | `vel`    | 行星初始加速度 (dx, dy)        |
| `planets`           | `color`  | 行星颜色 (R, G, B)             |
|                     |          |                                |
| `star_trajectory`   |          | 恒星轨迹开关                   |
| `planet_trajectory` |          | 行星轨迹开关                   |
| `trajectory_length` |          | 轨迹长度                       |
| `camera_speed`      |          | 使用上下左右键移动视角时的速度(像素/帧) |

## 必须第三方库
> pygame, pgzero, pgzrun, pyyaml


##### Version 2.1.2 最后一次编辑于 *2026.11.7, 淮安* 