#!/bin/bash
wg-quick up wg0
while true; do
  if [[ -f /config/wg0.conf ]]; then
    PRIVATEKEY=$(wg genkey)
    PUBLICKEY=$(echo $PRIVATEKEY | wg pubkey)
    SERVER_IP=$(curl -s ifconfig.me)
    echo -e "[Interface]\nPrivateKey = $PRIVATEKEY\nAddress = 10.0.0.3/24\nDNS = 1.1.1.1, 1.0.0.1\n\n[Peer]\nPublicKey = $PUBLICKEY\nAllowedIPs = 0.0.0.0/0\nEndpoint = $SERVER_IP:51820" > ./peer.conf
  fi
  sleep 1
done
