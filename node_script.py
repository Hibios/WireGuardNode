import os
import time
import codecs
from cryptography.hazmat.primitives.asymmetric.x25519 import X25519PrivateKey
from cryptography.hazmat.primitives import serialization
import subprocess


def generate_private_key():
    private_key = X25519PrivateKey.generate()
    bytes_ = private_key.private_bytes(encoding=serialization.Encoding.Raw, format=serialization.PrivateFormat.Raw, encryption_algorithm=serialization.NoEncryption())
    return private_key, codecs.encode(bytes_, 'base64').decode('utf8').strip()


def generate_public_key(private_key):
    pubkey = private_key.public_key().public_bytes(encoding=serialization.Encoding.Raw, format=serialization.PublicFormat.Raw)
    return codecs.encode(pubkey, 'base64').decode('utf8').strip()

private_key, format_str = generate_private_key()
public_key = generate_public_key(private_key)

with open('wg0.conf', 'w') as f:
    f.write(f"""
[Interface]
PrivateKey = {format_str}
Address = 10.0.0.1/24
ListenPort = 51820
PostUp = iptables -A FORWARD -i wg0 -j ACCEPT; iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
PostDown = iptables -D FORWARD -i wg0 -j ACCEPT; iptables -t nat -D POSTROUTING -o eth0 -j MASQUERADE

[Peer]
PublicKey = {public_key}
AllowedIPs = 10.0.0.2/32
    """)

print("Файл конфигурации wg0.conf для WireGuard создан.")
