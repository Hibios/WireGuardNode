# WireGuardNode
Развёртывание Wireguard в docker-compose, генерация ключей для клиента и сервера, создание конфигурационных файлов, а также отправка сообщений через приватную сеть Wireguard.
Реализация:
- создано 2 виртуальных сервера: Россия(Wireguard), Казахстан(Клиент)
- на сервере Россия запущены сервисы через docker-compose в нужном порядке, просмотреть логи и пинг от клиента: docker-compose logs -f -t
- на сервере Казахстан установлен клиент wireguard, запускается python start_client.py файл для отправки ping, так как сервер уже подключён к туннелю.
  
![image](https://github.com/Hibios/WireGuardNode/assets/42024589/d01b097f-ac83-4636-bc67-f2837aa3a107)
