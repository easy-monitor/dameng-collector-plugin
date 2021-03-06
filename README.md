# EasyOps 达梦数据库监控插件包

EasyOps 达梦数据库监控插件包是适用于 EasyOps 新版监控平台，专门提供达梦数据库监控服务的官方插件包。它提供了对达梦数据库的常见监控指标进行采集的采集插件以及可视化的仪表盘展示。

## 目录

- [背景](#背景)
- [适用环境](#适用环境)
- [准备工作](#准备工作)
- [使用方法](#使用方法)
- [项目内容](#项目内容)
- [维护者](#维护者)
- [许可证](#许可证)

## 背景

由于目前在 EasyOps 新版监控平台上搭建达梦数据库监控场景需要经过以下步骤：

1. 按照标准输出格式编写采集脚本。
2. 在插件中心创建采集插件，使用步骤1输出的指标数据录入监控指标。
3. 使用创建的采集插件为具体的资源实例创建采集任务。
4. 理解监控指标含义后配置仪表盘展示。

所以为了实现达梦数据库监控场景的快速搭建，该项目对达梦数据库一些常见的监控指标及其采集脚本进行了封装，同时提供一个基本的仪表盘展示。

用户能够借助 EasyOps 平台提供的自动化工具来一键导入该插件包，真正做到达梦数据库监控场景的开箱即用。
 
## 适用环境

主流的达梦数据库版本。

## 准备工作

1. 采集的 agent 需要编译安装达梦的 python 驱动包,  并验证能够成功导入dmPython库。
```
import dmPython
```


## 使用方法

1. 下载该项目的压缩包 ( https://github.com/easy-monitor/dameng-collector-plugin/archive/master.zip )。

2. 建议解压到 EasyOps 平台服务器上的 `/data/easyops/monitor_plugin_packages` 目录下。

3. 使用 EasyOps 平台提供的自动化工具一键导入该插件包，具体命令如下，请替换其中的 `8888` 为当前 EasyOps 平台具体的 `org`。

```sh
$ cd /usr/local/easyops/collector_plugin_service/tools
$ sh plugin_op.sh install 8888 /data/easyops/monitor_plugin_packages/dameng-collector-plugin
```

4. 导入成功后访问 EasyOps 平台的「采集插件」列表页面 ( http://your-easyops-server/next/collector-plugin )，就能看到导入的 "dameng_collector_plugin" 采集插件。

5. 接下来可使用该采集插件为具体的达梦数据库实例创建采集任务。

## 项目内容

### 目录结构

```
dameng-collector-plugin
├── dashboard.json
├── origin_metric.json
└── script
    ├── plugin.yaml
    └── src
        ├── run.sh
        └── collector.py
```

该项目的目录结构遵循标准的 EasyOps 监控插件包规范，具体内容如下：

- dashboard.json: 仪表盘的定义文件
- origin_metric.json: 采集插件关联的监控指标定义文件
- script: 采集插件关联的程序包目录，执行采集任务时会部署到指定的目标机器上
- script/plugin.yaml: 采集插件包的定义文件
- script/src: 采集插件包的脚本目录

### plugin.yaml

```yaml
# 支持 easyops/prometheus/zabbix-agent 三种采集类型
# 1. easyops: 表示使用 EasyOps Agent 进行指标采集
# 2. prometheus: 表示对接 Prometheus Exporter 进行指标采集
# 3. zabbix-agent: 表示对接 Zabbix Agent 进行指标采集
agentType: easyops

# 采集插件的名称，也是采集插件关联的程序包名称
name: dameng_collector_plugin
# 采集插件关联的程序包版本名称
version: 1.0.0

# 仅支持 simple-script 采集方式（采集类型为 easyops 时必须指定）
# 1. simple-script 表示使用执行脚本的采集方式
type: simple-script

# 采集命令（采集方式为 simple-script 时必须指定）
command:
  collect:
    type: shell              # 脚本类型支持 shell/python/powershell
    user: root               # 执行用户
    interpreter: /bin/bash   # 脚本解释器
    scriptPath:              # 采集脚本相对 script 目录的路径分割后的数组, 例如：src/run.sh 的相对路径会被分割为 [src, run.sh]
      - src
      - run.sh

# 采集插件类别 
category: 数据库
# 采集插件参数列表
params:
  - host_ip
  - port
  - user
  - password
  - dm_bin_path
```

## 维护者

@easyopscyrilchen

## 许可证

[MIT](#许可证) © EasyOps
