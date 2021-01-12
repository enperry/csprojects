import io


class MeteredFile(io.BufferedRandom):
    """Implement using a subclassing model."""

    def __init__(self, *args, **kwargs):
        super(MeteredFile, self).__init__(*args, **kwargs)
        self._read_bytes = 0
        self._read_ops = 0
        self._write_bytes = 0
        self._write_ops = 0

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return super(MeteredFile, self).__exit__(exc_type, exc_val, exc_tb)

    def __iter__(self):
        return self

    def __next__(self):
        if(not(line := super(MeteredFile, self).readline())):
            raise StopIteration()
        self._read_bytes = self._read_bytes + len(line)
        self._read_ops = self._read_ops + 1
        return line

    def read(self, size=-1):
        read_bytes = super(MeteredFile, self).read(size)
        self._read_bytes += len(read_bytes)
        self._read_ops += 1
        return read_bytes

    @property
    def read_bytes(self):
        return self._read_bytes

    @property
    def read_ops(self):
        return self._read_ops

    def write(self, b):
        write_len = super(MeteredFile, self).write(b)
        self._write_bytes = self._write_bytes + write_len
        self._write_ops = self._write_ops + 1
        return write_len

    @property
    def write_bytes(self):
        return self._write_bytes

    @property
    def write_ops(self):
        return self._write_ops


class MeteredSocket:
    """Implement using a delegation model."""

    def __init__(self, socket):
        self._socket = socket
        self._recv_bytes = 0
        self._recv_ops = 0
        self._send_bytes = 0
        self._send_ops = 0

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return self._socket.__exit__(exc_type, exc_val, exc_tb)

    def recv(self, bufsize, flags = 0):
        data = self._socket.recv(bufsize, flags)
        self._recv_bytes = self._recv_bytes + len(data)
        self._recv_ops = self._recv_ops + 1
        return data

    @property
    def recv_bytes(self):
        return self._recv_bytes

    @property
    def recv_ops(self):
        return self._recv_ops

    def send(self, data, flags = 0):
        send_len = self._socket.send(data, flags)
        self._send_bytes = self._send_bytes + send_len
        self._send_ops = self._send_ops + 1
        return send_len

    @property
    def send_bytes(self):
        return self._send_bytes

    @property
    def send_ops(self):
        return self._send_ops