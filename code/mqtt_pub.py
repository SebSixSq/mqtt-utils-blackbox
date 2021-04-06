#!/usr/bin/env python3

import os
import sys
import logging
import argparse
import paho.mqtt.client as mqtt


def mqtt_on_connect(client, userdata, flags, rc):
    logging.info(f'Connected with result code {rc}')


def mqtt_connect(host='127.0.0.1', port=1883):
    client = mqtt.Client()
    client.on_connect = mqtt_on_connect
    client.connect(host, port)
    client.enable_logger()
    client.loop_start()
    return client


def read_and_mqtt_publish(mqtt_client, mqtt_topic, buffer_size=1000000):
    i = 0
    data = 'data'
    while len(data):
        data = sys.stdin.buffer.read(buffer_size)
        mqtt_client.publish(mqtt_topic, data)


def get_argument_parser():
    parser = argparse.ArgumentParser(add_help=False, formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--help', action='help', help='show this help message and exit')
    parser.add_argument('-h', '--host',  default=os.environ.get('MQTT_HOST',  '127.0.0.1'),      help='MQTT broker host')
    parser.add_argument('-p', '--port',  default=os.environ.get('MQTT_PORT',  1883),  type=int,  help='MQTT broker port')
    parser.add_argument('-t', '--topic', default=os.environ.get('MQTT_TOPIC', 'example/topic'),  help='MQTT topic')
    parser.add_argument('-b', '--size',  default=os.environ.get('BUF_SIZE',  1000000), type=int, help='Buffer size')
    return parser


def main():
    args = get_argument_parser().parse_args()

    #logging.basicConfig(level=logging.DEBUG)

    mqtt_client = mqtt_connect(args.host, args.port)

    read_and_mqtt_publish(mqtt_client, args.topic, args.size)



if __name__ == '__main__':
    main()
