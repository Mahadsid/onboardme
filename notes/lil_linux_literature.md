# Random Notes

- [How does the vim write with sudo trick work?](https://stackoverflow.com/questions/2600783/how-does-the-vim-write-with-sudo-trick-work)
- Pretty view markdown: `pandoc README.md | lynx -stdin`

## Firewall notes
- [How to control internet access for each program?](https://askubuntu.com/questions/45072/how-to-control-internet-access-for-each-program)

## UFW notes
Need to get `$remote_ip` at time of running if this is being set up as a secondary machine
```bash
ufw allow from $remote_ip to any port 22
```

This is to create special firewall configs for annoying apps want to phone home while they're supposed to be not running:
```bash
ufw app list
# move special app 
cp ufw/* /etc/ufw/applications.d
ufw app update discord
ufw app info discord
ufw deny discord
```

## K8s stuff

### KIND - because easy local testing on linux
```bash
# creating a quick small cluster (unnamed, defaults to name: kind)
sudo kind create cluster

# adding newly created KIND kubeconfig
sudo kind get kubeconfig > ~/.kube/kubeconfig


### vm stuff
```bash
# launches a vm with 2 vCPU, 32G disk, name of node: k8s-worker-1, Ubuntu Image verion 20.04
multipass launch -c 2 -d 32G -m 2G -n k8s-wkr-1 20.04
multipass launch -c 2 -d 32G -m 2G -n k8s-wkr-2 20.04

# I just don't wanna call it a master
multipass launch -c 2 -d 32G -m 2G -n k8s-manager-1 20.04

# to access a multipass instance if you need to
multipass shell k8s-worker-1
```