# Clickhouse storage

> Репликация и шардирование не настроены!

docker run -u root --rm -it --network host --env-file .env  -v "/var/databases/volumes.nosync/clickhouse-shard:/var/lib/clickhouse" alexakulov/clickhouse-backup tables --help


## Запуск хранилища
```
$ docker-compose up -d
```

## Бэкап и восстановление
Бэкапы сохраняеются на удаленный `sftp` сервер.
Для этого нужно сначала настроить коннект между серверами через ключ:

```
$ ssh-copy-id -i '/root/.ssh/id_rsa.pub' -p 22 root@<host>
```
После вводим пароль, и взаимодействие настроено. Далее можно подключаться так:

```
$ ssh -p 22 root@<host>
```

Далее надо заполнить `.env`:
```
$ cp .example_env .env
```

> В `.example_env` указан пароль от `clickhouse` - плохо конечно, но и в конфиге `xml` он уже указан. Надо делать генератор конфига.


> Через ключ не работает :(

### Список бэкапов
```
$ docker run -u root --rm -it --network host --env-file .env  -v "/var/storage/volumes.nosync/clickhouse-shard:/var/lib/clickhouse" alexakulov/clickhouse-backup:1.2.2 list
```

### Бэкап на удаленный сервер
```
$ docker run -u root --rm -it --network host --env-file .env  -v "/var/storage/volumes.nosync/clickhouse-shard:/var/lib/clickhouse" alexakulov/clickhouse-backup:1.2.2 create_remote 
```

### Восстановление с удаленного сервера
```
$ docker run -u root --rm -it --network host --env-file .env  -v "/var/storage/volumes.nosync/clickhouse-shard:/var/lib/clickhouse" alexakulov/clickhouse-backup:1.2.2 restore_remote <name>
```


#### testing
docker run -u root --rm -it --network host --env-file .env  -v "/var/storage/volumes.nosync/clickhouse-shard:/var/lib/clickhouse" alexakulov/clickhouse-backup:1.2.2 restore_remote 2022-01-18T12-30-25