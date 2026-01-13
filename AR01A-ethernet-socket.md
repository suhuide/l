

# Serer
```c
root@linaro-alip:/# netstat -tuln | grep 8080
tcp        0      0 0.0.0.0:8080            0.0.0.0:*               LISTEN
root@linaro-alip:/#
```

# Client
```c
nc -zv 10.5.17.111 8080
Connection to 10.5.17.111 8080 port[tcp/http-alt] succeeded!
```