#!/bin/bash
wg-quick up wg0
flag=true
while true; do
  if [[ -f /config/wg0.conf ]] && $flag; then
    PRIVATEKEY=$(wg genkey)
    PUBLICKEY=$(echo $PRIVATEKEY | wg pubkey)
    SERVER_IP=$(curl -s ifconfig.me)
    echo -e "[Interface]\nPrivateKey = $PRIVATEKEY\nAddress = 10.0.0.7/24\nDNS = 1.1.1.1, 1.0.0.1\n\n[Peer]\nPublicKey = $PUBLICKEY\nAllowedIPs = 10.0.0.0/24\nEndpoint = $SERVER_IP:51820" > ./wg_client.conf
    wg set wg0 peer $PUBLICKEY allowed-ips 10.0.0.0/24
    flag=false
  fi
  sleep 1
done
