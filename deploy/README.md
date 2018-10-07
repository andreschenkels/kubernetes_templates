# Setup

## SSH
Install `open-ssh`, and add relevant keys to `~/.ssh/authorized_keys`.
See this [guide for generating SSH keys](https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/).

## Network
1. Renaming host(s)
* in `/etc/hostname` and `/etc/hosts`
* or under Ubuntu > 18.xx: `sudo hostnamectl set-hostname <HOSTNAME>`,and `preserve_hostname: true` in `/etc/cloud/cloud.cfg`

2. Setting static IP and shared network if needed (e.g. VirtualBox machines)
* through `/etc/network/interface`
```
auto enp0s8
iface enp0s8 inet static
    address 192.168.56.2
    netmask 255.255.255.0
```
* or under Ubuntu > 18.xx with `netplan` in `/etc/netplan/01-netcfg.yaml`
```
network:
  version: 2
  renderer: networkd
  ethernets:
    enp0s8:
      dhcp4: no
      addresses: [192.168.56.2/24]
      nameservers:
        addresses: [8.8.8.8,8.8.4.4]
```
then `sudo netplan --debug apply`

## k8s
More details available [here](https://kubernetes.io/docs).

1. `docker`
Everything detailed [here](https://docs.docker.com/install/linux/docker-ce/ubuntu/#install-using-the-repository).
```
sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    software-properties-common
```
```
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
```
```
sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"
```
```
sudo apt-get install docker-ce
```
and allow to [run as non root user](https://docs.docker.com/install/linux/linux-postinstall/#manage-docker-as-a-non-root-user)

2. `kubeadm`, `kubelet` and `kubectl`
```
sudo su
apt-get update && apt-get install -y apt-transport-https curl
curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add -
cat <<EOF >/etc/apt/sources.list.d/kubernetes.list
deb http://apt.kubernetes.io/ kubernetes-xenial main
EOF
apt-get update
apt-get install -y kubelet kubeadm kubectl
apt-mark hold kubelet kubeadm kubectl
```
For `kubectl` autocompletion,
```
echo "source <(kubectl completion bash)" >> ~/.bashrc
```

3. Secrets & environment variables
Define persistent environment name in `/etc/environment`, e.g. `ENV="staging"`.
```
kubectl create secret docker-registry --dry-run=true docker --docker-server=docker.io --docker-username=<your-name> --docker-password=<your-pword> --docker-email=<your-email> -o yaml > docker-secret.yaml
kubectl apply -f docker-secret.yaml
```

4. MySQL users
When setting up cluster for the first time, MySQL users and grants have to be created:
```
CREATE USER 'username'@'%' IDENTIFIED BY 'password';
GRANT ALL ON 'database'.* TO 'username'@'%';
```
Note: to connect from Adminer to MySQL, a first connection from the CLI seems to be required:
```
kubectl exec -it mysql-7ffbb86857-f546g -- bash -l
mysql -h mysql -u username -p
```
Not sure if this is due to MySQL itself, or k8s DNS setup and discovery (the MySQL service is headless).
