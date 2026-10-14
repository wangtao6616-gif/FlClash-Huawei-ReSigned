# FlClash Huawei Re-Signed (Unofficial)

> **非官方第三方发行版 / Unofficial community redistribution**

基于 [chen08209/FlClash](https://github.com/chen08209/FlClash) v0.9.0 的 Android ARM64 个人重新签名安装包，供华为 / HarmonyOS 设备兼容性测试。**本项目与 FlClash 原作者及华为官方没有隶属或认证关系。**

## 版本信息

| 项目 | 详情 |
| --- | --- |
| 上游 | [chen08209/FlClash](https://github.com/chen08209/FlClash) |
| 原版版本 | v0.9.0 |
| 平台 | Android ARM64 (arm64-v8a) |
| 本地安装包文件名 | `FlClash-0.9.0-arm64-personal.apk` |
| 本次调整 | 个人重新签名（并非华为官方认证/安全白名单） |
| 许可证 | [GNU GPL-3.0](LICENSE) |

## 下载

请访问 [Releases 页面](../../releases) 查找已发布的安装包。**仓库当前是否已经提供 APK，以 Releases 实际附件为准。**

## 安装和安全说明

- 仅用于测试第三方重签名 APK 在特定华为设备上的兼容性；**重新签名并不能保证解除系统的风险提示或绕过设备安全策略**。
- 下载安装前请自行核验 APK 来源、完整性和签名。不要因为仓库名就认定为官方或受华为认可的软件。
- 重新签名版本与上游官方签名不同，不能直接覆盖原版升级。以后要覆盖安装本分支，也需要保留同一应用包名并使用**同一签名密钥**；否则通常需要先卸载并备份数据。
- 请勿在公开仓库上传 keystore、签名私钥、密码或个人配置文件。

## APK 校验

本项目准备发布的个人版 APK（v0.9.0，arm64）的 SHA-256：

```text
8fb5f85257360fe1085a52399eb413b5a8072695bbad4c599add49b2850d6931
```

Windows PowerShell 校验：

```powershell
Get-FileHash .\FlClash-0.9.0-arm64-personal.apk -Algorithm SHA256
```

## 上游源码和许可

- [原项目源码](https://github.com/chen08209/FlClash)
- [v0.9.0 对应源码](https://github.com/chen08209/FlClash/tree/v0.9.0)
- [上游 v0.9.0 Release](https://github.com/chen08209/FlClash/releases/tag/v0.9.0)

原项目采用 GPL-3.0。分发修改版二进制时还必须满足 GPL 对**相应源码**及构建修改内容的提供要求。如果 APK 包含重新打包、改名或其他代码修改，应公开这些改动和可重现构建步骤；仅提供上游链接不一定充分满足许可义务。

## 致谢与免责声明

感谢 FlClash 作者 [chen08209](https://github.com/chen08209) 及项目贡献者。FlClash 的著作权归原权利人所有；此个人版由第三方自行维护，不代表上游官方推荐、审核或担保。软件按 GPL-3.0 条款提供，不附带任何保证。
