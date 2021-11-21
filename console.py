import sys

import click

sys.path.append('./src')

from ptpip.client import PtpIpClient

from ptpip.cli.get_device_info import GetDeviceInfoCommand
from ptpip.cli.get_device_prop_desc import GetDevicePropDescCommand
from ptpip.cli.get_device_prop_value import GetDevicePropValueCommand
from ptpip.cli.get_num_objects import GetNumObjectsCommand
from ptpip.cli.get_object_handles import GetObjectHandlesCommand
from ptpip.cli.get_storage_ids import GetStorageIdsCommand
from ptpip.cli.get_storage_info import GetStorageInfoCommand
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
@click.option('--more', default=False, help='Discover every possible property ?')
@click.option('--report', default='d5300.html', help='Report filename')
def getDeviceInfo(host, port, debug, discover, more, report):
    PtpIpClient(
        GetDeviceInfoCommand(discover, more, report).run,
        host = host,
        port = port,
        debug = debug
    )

@cli.command('propdesc')
@click.option('--host', default=None, help='Hostname')
@click.option('--port', default=None, help='Port')
@click.option('--debug', default=False, help='Debug mode')
@click.option('--name', help='Property name')
@click.option('--id', help='Property id', type=int)
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
@click.option('--id', help='Property id', type=int)
@click.option('--typename', help='Property type name')
@click.option('--typeid', help='Property type id', type=int)
@click.option('--value', required=True, help='Property value')
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
@click.option('--id', help='Property id', type=int)
@click.option('--typename', help='Property type name')
@click.option('--typeid', help='Property type id', type=int)
def getDevicePropValue(host, port, debug, name, id, typename, typeid):
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

@cli.command('storageids')
@click.option('--host', default=None, help='Hostname')
@click.option('--port', default=None, help='Port')
@click.option('--debug', default=False, help='Debug mode')
def getStorageIds(host, port, debug):
    PtpIpClient(
        GetStorageIdsCommand().run,
        host = host,
        port = port,
        debug = debug
    )

@cli.command('storage')
@click.option('--host', default=None, help='Hostname')
@click.option('--port', default=None, help='Port')
@click.option('--debug', default=False, help='Debug mode')
@click.option('--id', required=True, help='Storage id', type=int)
def getStorageInfo(host, port, debug, id):
    PtpIpClient(
        GetStorageInfoCommand(id).run,
        host = host,
        port = port,
        debug = debug
    )

@cli.command('numobjects')
@click.option('--host', default=None, help='Hostname')
@click.option('--port', default=None, help='Port')
@click.option('--debug', default=False, help='Debug mode')
@click.option('--id', required=True, help='Storage id', type=int)
@click.option('--format', help='Object format id', type=int)
@click.option('--formatname', help='Object format name')
@click.option('--handle', help='Object handle of the directory', type=int)
def getNumObjects(host, port, debug, id, format, formatname, handle):
    PtpIpClient(
        GetNumObjectsCommand(id, format, formatname, handle).run,
        host = host,
        port = port,
        debug = debug
    )

@cli.command('objhandles')
@click.option('--host', default=None, help='Hostname')
@click.option('--port', default=None, help='Port')
@click.option('--debug', default=False, help='Debug mode')
@click.option('--id', help='Storage id', type=int)
@click.option('--format', help='Object format id', type=int)
@click.option('--formatname', help='Object format name')
@click.option('--handle', help='Object handle of the directory', type=int)
@click.option('--all-storages', help='Search in all storages', type=bool)
@click.option('--all-formats', help='Search in all formats', type=bool)
def getObjectHandles(host, port, debug, id, format, formatname, handle, all_storages, all_formats):
	PtpIpClient(
		GetObjectHandlesCommand(id, format, formatname, handle, all_storages, all_formats).run,
		host = host,
		port = port,
		debug = debug
	)

if __name__ == '__main__':
    cli()
