import bluetooth
import time

from micropython import const

from lib.tools import Payload

_IRQ_CENTRAL_CONNECT    = const(1)
_IRQ_CENTRAL_DISCONNECT = const(2)
_IRQ_GATTS_WRITE        = const(3)

_FLAG_READ              = const(0x0002)
_FLAG_WRITE_NO_RESPONSE = const(0x0004)
_FLAG_WRITE             = const(0x0008)
_FLAG_NOTIFY            = const(0x0010)

_UART_UUID = bluetooth.UUID("6E400001-B5A3-F393-E0A9-E50E24DCCA9E")
#
_UART_TX = (
    bluetooth.UUID("6E400003-B5A3-F393-E0A9-E50E24DCCA9E"),
    _FLAG_READ | _FLAG_NOTIFY,
)
#
_UART_RX = (
    bluetooth.UUID("6E400002-B5A3-F393-E0A9-E50E24DCCA9E"),
    _FLAG_WRITE | _FLAG_WRITE_NO_RESPONSE,
)
#
_UART_SERVICE = (
    _UART_UUID,
    (_UART_TX, _UART_RX),
)

_DEV_NAME = "EL_OMAR"

class BLE_send_sequence:
    def __init__(self, ble, name=_DEV_NAME):
        self._ble = ble
        self._ble.active(True)
        self._ble.irq(self._irq)
        ((self._handle_tx, self._handle_rx),) = self._ble.gatts_register_services((_UART_SERVICE,))
        self._connections = set()
        self._write_callback = None
        #
        payload = Payload(name=name, services=[_UART_UUID])
        self._payload = payload.get()
        self._advertise()
    #
    def _irq(self, event, data):
        # Track connections so we can send notifications.
        if event == _IRQ_CENTRAL_CONNECT:
            conn_handle, _, _ = data
            print("Conexión nueva", conn_handle)
            self._connections.add(conn_handle)
        elif event == _IRQ_CENTRAL_DISCONNECT:
            conn_handle, _, _ = data
            print("Desconexión", conn_handle)
            self._connections.remove(conn_handle)
            # Start advertising again to allow a new connection.
            self._advertise()
        elif event == _IRQ_GATTS_WRITE:
            conn_handle, value_handle = data
            value = self._ble.gatts_read(value_handle)
            if value_handle == self._handle_rx and self._write_callback:
                self._write_callback(value)
    #
    def send(self, data):
        for conn_handle in self._connections:
            self._ble.gatts_notify(conn_handle, self._handle_tx, data)
    #
    def is_connected(self):
        return len(self._connections) > 0
    #
    def _advertise(self, interval_us=1_000_000):
        print("Starting advertising")
        self._ble.gap_advertise(interval_us, adv_data=self._payload)
    #
    def on_write(self, callback):
        self._write_callback = callback

def main():
    ble = bluetooth.BLE()
    p = BLE_send_sequence(ble)
    #
    i = 0
    while True:
        if p.is_connected():
            # Short burst of queued notifications.
            for _ in range(3):
                data = str(i) + "_"
                print(f"TX: {data}" )
                p.send(data)
                i += 1
        time.sleep_ms(100)
#
if __name__ == "__main__":
    main()