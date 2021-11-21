import sys

import click

sys.path.append('./src')

from ptpip.client import PtpIpClient

from ptpip.cli.get_device_info import GetDeviceInfoCommand
from ptpip.cli.get_device_prop_desc import GetDevicePropDescCommand
from ptpip.cli.get_device_prop_value import GetDevicePropValueCommand
from ptpip.cli.init_capture import InitCaptureCommand
from ptpip.cli.set_device_prop_value import SetDevicePropValueCommand

@click.group()
def cli():
    pass

@cli.command('device')
@click.option('--host', default=None, help='Hostname')
@click.option('--port', default=None, help='Port')
@click.option('--debug', default=False, help='Debug mode')
@click.option('--discover', default=True, help='Discover unoffically supported properties ?')
@click.option('--report', default='d5300.html', help='Report filename')
def getDeviceInfo(host, port, debug, discover, report):
    PtpIpClient(
        GetDeviceInfoCommand(discover, report).run,
        host = host,
        port = port,
        debug = debug
    )

@cli.command('propdesc')
@click.option('--host', default=None, help='Hostname')
@click.option('--port', default=None, help='Port')
@click.option('--debug', default=False, help='Debug mode')
@click.option('--name', help='Property name')
@click.option('--id', help='Property id')
def getDevicePropDesc(host, port, debug, name, id):
    PtpIpClient(
        GetDevicePropDescCommand(name, id).run,
        host = host,
        port = port,
        debug = debug
    )


@cli.command('setprop')
@click.option('--host', default=None, help='Hostname')
@click.option('--port', default=None, help='Port')
@click.option('--debug', default=False, help='Debug mode')
@click.option('--name', help='Property name')
@click.option('--id', help='Property id')
@click.option('--typename', help='Property type name')
@click.option('--typeid', help='Property type id')
@click.option('--value', help='Property value')
def setDevicePropValue(host, port, debug, name, id, typename, typeid, value):
    PtpIpClient(
        SetDevicePropValueCommand(name, id, typename, typeid, value).run,
        host = host,
        port = port,
        debug = debug
    )

@cli.command('getprop')
@click.option('--host', default=None, help='Hostname')
@click.option('--port', default=None, help='Port')
@click.option('--debug', default=False, help='Debug mode')
@click.option('--name', help='Property name')
@click.option('--id', help='Property id')
@click.option('--typename', help='Property type name')
@click.option('--typeid', help='Property type id')
def setDevicePropValue(host, port, debug, name, id, typename, typeid):
    PtpIpClient(
        GetDevicePropValueCommand(name, id, typename, typeid).run,
        host = host,
        port = port,
        debug = debug
    )

@cli.command('capture')
@click.option('--host', default=None, help='Hostname')
@click.option('--port', default=None, help='Port')
@click.option('--debug', default=False, help='Debug mode')
@click.option('--output', default=None, help='Save image to given filepath')
def initCapture(host, port, debug, output):
    PtpIpClient(
        InitCaptureCommand(output).run,
        host = host,
        port = port,
        debug = debug
    )

if __name__ == '__main__':
    cli()
