import gdb
import re

class ArrayPrinter:
    def __init__(self, val, name):
        self.val = val
        self.name = name
        self.size = self.val['size']

    def to_string(self):
        capacity = self.val['data']['capacity']
        return '%s of size %d, capacity %d' % (self.name, self.size, capacity)

    def children(self):
        return self.iterator(self)

    class iterator:
        def __init__(self, parent):
            self.parent = parent
            self.data = parent.val['data']['h_ptr']
            self.pos = 0

        def __iter__(self):
            return self

        def next(self):
            pos = self.pos
            if self.pos >= self.parent.size:
                raise StopIteration
            self.pos = self.pos + 1
            return ('[%d]' % pos, self.data[pos])


class MatrixPrinter:
    def __init__(self, val):
        self.val = val
        self.width = val['width']
        self.height = val['height']

    def to_string(self):
        capacity = self.val['capacity']
        return 'mfem::DenseMatrix of size %dx%d, capacity %d' % (self.height, self.width, capacity)

    def children(self):
        return self.iterator(self)

    class iterator:
        def __init__(self, parent):
            self.parent = parent
            self.data = parent.val['data']
            self.row = 0
            self.col = 0

        def __iter__(self):
            return self

        def next(self):
            row = self.row
            col = self.col

            if row >= self.parent.height:
                raise StopIteration

            self.col = self.col + 1
            if self.col >= self.parent.width:
                self.col = 0
                self.row = self.row + 1

            item = self.data[col*self.parent.height + row]
            return ('(%d,%d)' % (row, col), item)


def lookup_type(val):
    typename = str(val.type.tag)
    if re.match('^mfem::Array<.*>$', typename) is not None:
        return ArrayPrinter(val, typename)
    if typename == 'mfem::Vector':
        return ArrayPrinter(val, typename)
    if typename == 'mfem::DenseMatrix':
        return MatrixPrinter(val)
    return None


def register_mfem_printers(obj):
    if obj == None:
        obj = gdb
    obj.pretty_printers.append(lookup_type)
