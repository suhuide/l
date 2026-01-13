[memo.md](memo.md)
```c
ls@ls-VirtualBox:~$ 
cd ~/
ls -la
more .gitconfig 
mv .gitconfig /data/
mkdir /data/.ssh
mv .ssh/gerrit_rsa /data/.ssh/
mv .ssh/known_hosts /data/.ssh/
ls -la
ls .git_template/
ls .git_template/hooks/
vi .git_template/hooks/commit-msg 
cd .ssh/
ls -la
cp config /data//.ssh/
vi config 
shutdown -h 0
ifconfig
ls
cd s06g/
ls
ls -a
du -sh
repo init -u ssh://gerrit/lens/manifest -b S06G -m s06g_android11_rk3566.xml --repo-url=ssh://gerrit/git_repo
git clone "http://SZ000062@10.5.103.101:8010/a/rk/rk/device/rockchip/rk3566" && (cd "rk3566" && gitdir=$(git rev-parse --git-dir); curl -o ${gitdir}/hooks/commit-msg http://10.5.103.101:8010/static/commit-msg; chmod +x ${gitdir}/hooks/commit-msg)
cd ..
rm -rf s06g/
mkdir s06g
ls
du
du -sh
ls
cd s06g/
git clone "http://SZ000062@10.5.103.101:8010/a/rk/rk/device/rockchip/rk3566" && (cd "rk3566" && gitdir=$(git rev-parse --git-dir); curl -o ${gitdir}/hooks/commit-msg http://10.5.103.101:8010/static/commit-msg; chmod +x ${gitdir}/hooks/commit-msg)
ls
cd rk3566/
ls
ls -l
df -h
du -sh
git log
ifconfig
repo init -u ssh://gerrit/lens/manifest -b S06G -m s06g_android11_rk3566.xml --repo-url=ssh://gerrit/git_repo
cd ..
cd .
cd ..
rm -rf s06g/
mkdir -p s06g && cd s06g
repo init -u ssh://gerrit/lens/manifest -b S06G -m s06g_android11_rk3566.xml --repo-url=ssh://gerrit/git_repo
repo
git config -l
cd ~/.ssh/
ls -la
vi config 
ssh-keygen -t rsa -C "SZ000062@hnlens.com"
ls -la
more config 
vi id_rsa.pub 
more id_rsa.pub 
git config --global user.name "SZ000062"
git config --global user.email "SZ000062@hnlens.com"
git config -l
cd -
ls -la
cd ..
ls -la
rm s06g/ -rf
ls -la
mkdir /data
cd da
cd /data/
ls -la
sudo ld /dev/sd* -la
sudo mount /dev/sdb /data
ls -la
vi /etc/fstab 
sudo vi /etc/fstab 
reboot
mkdir -p s06g && cd s06g
ls
repo init -u ssh://gerrit/lens/manifest -b S06G -m s06g_android11_rk3566.xml --repo-url=ssh://gerrit/git_repo
git config
git config -l
repo init -u ssh://gerrit/lens/manifest -b S06G -m s06g_android11_rk3566.xml --repo-url=ssh://gerrit/git_repo
df -h
repo
cd /data
cd s06g/
repo
repo init
cd /data/s06g/
more ~/.ssh/config 
repo init -u ssh://gerrit/lens/manifest -b S06G -m s06g_android11_rk3566.xml --repo-url=ssh://gerrit/git_repo
cd ..
rm -rf s06g/
mkdir -p s06g && cd s06g
repo init -u ssh://gerrit/lens/manifest -b S06G -m s06g_android11_rk3566.xml --repo-url=ssh://gerrit/git_repo
ls -l
cd
cd .ssh/
ls -a
ll
chmod 600 id_rsa.pub 
ll
cat known_hosts 
vim known_hosts 
ls
cat config 
vim  config 
clear
```