# FlClash Huawei Re-Signed (Unofficial)

> 非官方第三方修改发行版，用于支持 Android APK 的华为 / HarmonyOS 设备安装兼容性测试；与 FlClash 原作者、华为官方无隶属或认证关系。

基于 [chen08209/FlClash](https://github.com/chen08209/FlClash)，将应用包名改为个人包名，并使用个人证书重新签名。感谢原作者及所有贡献者。

## 下载

访问 [Releases 页面](https://github.com/wangtao6616-gif/FlClash-Huawei-ReSigned/releases) 获取已发布的 APK。安装包是否可下载，以对应版本的实际附件为准。

## v0.9.1 版本信息

| 项目 | 内容 |
| --- | --- |
| 上游版本 | [v0.9.1](https://github.com/chen08209/FlClash/releases/tag/v0.9.1) |
| 平台 | Android ARM64（arm64-v8a） |
| 文件名 | `FlClash-0.9.1-arm64-personal.apk` |
| 个人包名 | `com.xigua.netapp` |
| versionCode | `2026103702` |
| 修改内容 | 包名、关联清单标识、资源包名、个人签名 |
| 文件大小 | 60,925,222 字节 |
| 许可证 | [GPL-3.0](LICENSE) |

DEX、原生库与 Flutter 资源均与上游 v0.9.1 对应文件逐字节一致。详见 [修改说明](releases/v0.9.1-modifications.md)、[处理脚本](tools/repackage_v0_9_1.py) 和 [核验记录](releases/v0.9.1-verification.json)。

## 安装和后续升级

- 从本仓库 v0.9.0 个人版升级：本次保留相同包名、相同签名证书并提高 versionCode，满足覆盖升级的静态条件。安装前建议导出配置备份。
- 上游官方 APK 的包名和签名不同，不能直接覆盖本个人版。应用内更新可能下载官方包，后续请使用本仓库保持同一包名和签名的新版。
- 仅适用于支持 Android APK 的系统；重新签名不保证消除系统风险提示或解决兼容性问题。
- 本版已完成静态文件和签名核验，**尚未进行华为真机安装及功能测试**。
- 签名私钥、密码和个人配置不得上传到公开仓库。

## 校验

v0.9.1 APK SHA-256：

```text
c9fc8e913e000c24c294d12b0b226a96dcd033e6232498153965606ef68b4f96
```

签名证书 SHA-256（与 v0.9.0 个人版相同）：

```text
c7b3a2be9fdd258e6b1253340cc28d31b741938e8072b7799861a54546152a47
```

Windows PowerShell：

```powershell
Get-FileHash .\FlClash-0.9.1-arm64-personal.apk -Algorithm SHA256
```

## 原项目与许可

- [原项目 chen08209/FlClash](https://github.com/chen08209/FlClash)
- [v0.9.1 对应源码与构建说明](https://github.com/chen08209/FlClash/tree/v0.9.1)
- [v0.9.0 历史发行版](https://github.com/wangtao6616-gif/FlClash-Huawei-ReSigned/releases/tag/v0.9.0-huawei.1)

FlClash 的著作权归原权利人所有，原项目采用 GPL-3.0。此仓库提供个人发行改动、处理脚本和核验记录；完整 FlClash 源码及依赖请从上游对应版本获取。Release 自动生成的 Source code 附件只包含本仓库文件，不代表 FlClash 完整源码。本项目不代表上游或华为官方审核、认证或推荐，软件不附带任何保证。
