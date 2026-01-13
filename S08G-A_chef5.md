# 1、账户配置：[git操作指南](http://10.5.103.101:5080/rjb/ls_rjb_doc/-/blob/main/10_%E6%93%8D%E4%BD%9C%E6%B5%81%E7%A8%8B/git%E6%93%8D%E4%BD%9C%E6%8C%87%E5%8D%97.md)

# 2、[Gerrit CodeReview hooks(commit-msg) 配置](http://10.5.103.101:5080/rjb/ls_rjb_doc/-/blob/main/10_%E6%93%8D%E4%BD%9C%E6%B5%81%E7%A8%8B/Gerrit%20CodeReview%20hooks(commit-msg)%20%E9%85%8D%E7%BD%AE.md)

# 3、代码同步
## 3.1、主线开发
### 3.1.1 平板：下载thundercomm turbox qcm8550 主线开发代码
底版本代码下载见：[S08G-A_chef5.md](http://10.5.103.101:5080/systemteam/systemteam_doc/-/blob/main/21_%E9%85%8D%E7%BD%AE/%E4%BB%A3%E7%A0%81%E5%90%8C%E6%AD%A5%E4%B8%8E%E5%8D%87%E7%BA%A7/S08G-A_chef5.md)                 
所在远端 name：clo & lens          
所在分支 branch：android13/qcm8550/s08g-a          

```
cd ${workspace}
mkdir -p sm8550 && cd sm8550

repo init -u ssh://gerrit/lens/manifest -b S08G-A -m android13_qcm8550_s08g-a.xml --repo-url=ssh://gerrit/lens/git_repo --no-repo-verify -c

repo sync -j8 -c
```

### 3.1.2 音响：下载 amlogic 主线开发代码
所在远端 name：origin         
所在分支 branch：linux66/a113l2/s08g-a/dock  
```
cd ${workspace}
mkdir -p dock && cd dock

repo init -u ssh://gerrit/lens/manifest -b S08G-A -m dock_s08g-a.xml --repo-url=ssh://gerrit/lens/git_repo --no-repo-verify -c

repo sync -j8 -c
```

# 4、编译

## 4.1 平板

## 4.2 音响
Building the BA401 smart speaker for 64-bit App on kernel 5.4 (BA400+D613)               
Below amlogic is root directory of SDK.
```
cd dock 
source setenv.sh a4_ba400_spk_a64_k66_release
make
```
Image location
```
output/a4_ba400_spk_a64_k66_release/images/aml_upgrade_package.img
```

@from 2024.10.12 on
```
#完整重编
source setenv.sh a4_ba400_spk_a64_release;make clean;make json-c-rebuild;make ell-rebuild;make mdnsresponder-rebuild;make
#首次编译
source setenv.sh a4_ba400_spk_a64_release;make json-c-rebuild;make
```

# 5、变更历史
| 日期 | 变更项 | 变更后代码同步 |
| ------ | ------ | --------- |
| 2024.8.13 | 首次上库  |**dock:** baseline/buildroot-openlinux-2024r1-a113x2-a113l2 <br>|
| 2024.8.29 |  更改音响repo代码，主线开发分支名： linux66/a113l2/s08g-a/dock --> a113l2/s08g-a/dock ||
| 2024.10.15 |  添加2个库： lens/vendor/amlogic/matter;lens/vendor/amlogic/ot-br-posix |[\[TASK_13183\]dock添加仓库](http://10.5.103.101:9080/task-view-13183.html)|
